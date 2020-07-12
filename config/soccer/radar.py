class RadarConfig:
    status_map = {
        'not_started': 'Fixture',
        'live': 'Playing',
        'ended': 'Played',
        'closed': 'Played',
        'canceled': 'Cancelled',
        'delayed': 'Suspended',
        'start_delayed': 'Suspended',
        'postponed': 'Postponed',
    }


radar_cfg = RadarConfig()
