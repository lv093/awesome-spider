from concurrent.futures import ThreadPoolExecutor
import concurrent.futures
from flask import copy_current_request_context, _request_ctx_stack
from flask.globals import _app_ctx_stack
from collections import OrderedDict
from flask import current_app


class ThreadPool:
    def __init__(self, max_workers=10):
        self.app = current_app
        self._executor = None
        self.futures = FutureCollection()
        self._executor = ThreadPoolExecutor(max_workers=max_workers)

    def submit(self, func, *args, **kwargs):
        func = self._prepare_func(func)
        return self._executor.submit(func, *args, **kwargs)

    def submit_stored(self, future_key, func, *args, **kwargs):
        future = self.submit(func, *args, **kwargs)
        self.futures.add(future_key, future)
        return future

    def shutdown(self):
        return self._executor.shutdown()

    def map(self, func, *iterables, **kwargs):
        func = self._prepare_func(func)
        return self._executor.map(func, *iterables, **kwargs)

    def job(self, func):
        return ThreadPoolJob(executor=self, func=func)

    def _copy_current_app_context(self, func):
        app_context = _app_ctx_stack.top

        def wrapper(*args, **kwargs):
            with app_context:
                return func(*args, **kwargs)

        return wrapper

    def _prepare_func(self, func):
        if isinstance(self._executor, concurrent.futures.ThreadPoolExecutor):
            if _request_ctx_stack.top is not None:
                func = copy_current_request_context(func)
            func = self._copy_current_app_context(func)
        return func


class ThreadPoolJob:
    def __init__(self, executor, func):
        self.executor = executor
        self.func = func

    def submit(self, *args, **kwargs):
        future = self.executor.submit(self.func, *args, **kwargs)
        return future

    def submit_stored(self, future_key, *args, **kwargs):
        future = self.executor.submit_stored(future_key, self.func, *args, **kwargs)
        return future

    def map(self, *iterables, **kwargs):
        results = self.executor.map(self.func, *iterables, **kwargs)
        return results


class FutureCollection:
    def __init__(self, max_length=50):
        self.max_length = max_length
        self._futures = OrderedDict()

    def __contains__(self, future):
        return future in self._futures.values()

    def __len__(self):
        return len(self._futures)

    def __getattr__(self, attr):
        def _future_attr(future_key, *args, **kwargs):
            if future_key not in self._futures:
                return None
            future_attr = getattr(self._futures[future_key], attr)
            if callable(future_attr):
                return future_attr(*args, **kwargs)
            return future_attr

        return _future_attr

    def _check_limits(self):
        if self.max_length is not None:
            while len(self._futures) > self.max_length:
                self._futures.popitem(last=False)

    def add(self, future_key, future):
        if future_key in self._futures:
            raise ValueError("future_key {} already exists".format(future_key))
        self._futures[future_key] = future
        self._check_limits()

    def pop(self, future_key):
        return self._futures.pop(future_key, None)


thread_pool = ThreadPool(30)
