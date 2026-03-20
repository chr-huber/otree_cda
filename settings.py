from os import environ

SESSION_CONFIGS = [
    dict(
        name="teaching",
        display_name="Teaching - Full (with tasks)",
        app_sequence=[
            "intro",
            "cda_practice",
            "cda_rep1",
            "crt7",
            "apm",
            "egt",
            "demographics"
        ],
        num_demo_participants=4,
        experiment="teaching",
        trading_seconds=120,
        trading_summary_seconds=20,
        dividend_high=10,
        dividend_low=0,
        endowment_high_cash=(3000, 20),
        endowment_low_cash=(1000, 60),
    ),
    dict(
        name="teaching_slim",
        display_name="Teaching - Slim (market only)",
        app_sequence=[
            "intro",
            "cda_practice",
            "cda_rep1",
            "demographics"
        ],
        num_demo_participants=4,
        experiment="teaching",
        trading_seconds=120,
        trading_summary_seconds=20,
        dividend_high=10,
        dividend_low=0,
        endowment_high_cash=(3000, 20),
        endowment_low_cash=(1000, 60),
    ),
    dict(
        name="crt7",
        display_name="Cognitive Reflection Test",
        app_sequence=["crt7"],
        num_demo_participants=4,
    ),
    dict(
        name="apm",
        display_name="Advanced Progressive Matrices",
        app_sequence=["apm"],
        num_demo_participants=4,
    ),
    dict(
        name="egt",
        display_name="Eye Gaze Test",
        app_sequence=["egt"],
        num_demo_participants=4,
    ),
    dict(
        name="demographics",
        display_name="Demographics + Payments",
        app_sequence=["demographics"],
        num_demo_participants=4,
    ),
]

# if you set a property in SESSION_CONFIG_DEFAULTS, it will be inherited by all configs
# in SESSION_CONFIGS, except those that explicitly override it.
# the session config can be accessed from methods in your apps as self.session.config,
# e.g. self.session.config['participation_fee']

SESSION_CONFIG_DEFAULTS = dict(
    real_world_currency_per_point=1/160, participation_fee=6.00, doc="",
    # Market grouping: set one of these to override automatic grouping.
    # traders_per_market: all markets have equal size (must divide num_players evenly).
    # num_markets: split players into this many markets as evenly as possible.
    # If both are set, traders_per_market takes priority.
    # Leave both as None to use automatic grouping based on player count.
    traders_per_market=10,
    num_markets=2,
)

PARTICIPANT_FIELDS = ['crt_points', 'crt_num_correct', 'part1_points', 'part2_points']
SESSION_FIELDS = ['repetition', 'pay_repetition']

# ISO-639 code
# for example: de, fr, ja, ko, zh-hans
LANGUAGE_CODE = 'en'

# e.g. EUR, GBP, CNY, JPY
REAL_WORLD_CURRENCY_CODE = 'EUR'
USE_POINTS = True

ADMIN_USERNAME = 'admin'
# for security, best to set admin password in an environment variable
ADMIN_PASSWORD = environ.get('OTREE_ADMIN_PASSWORD')

DEMO_PAGE_INTRO_HTML = """ """

SECRET_KEY = '4324687630047'

ROOMS = [
    dict(
        name='berlin',
        display_name='Berlin Lab - Labels S01 - S24',
        participant_label_file='_rooms/econlab.txt',
    ),
    dict(
        name='innsbruck',
        display_name='Innsbruck EconLab - Labels S01 - S24',
        participant_label_file='_rooms/econlab.txt',
    ),
    dict(
        name='vcee',
        display_name='VCEE Lab - Labels S01 - S28',
        participant_label_file='_rooms/vcee.txt',
    ),
    dict(
        name='vcee_any',
        display_name='VCEE Lab - Any Label',
    ),
    dict(
        name='wu',
        display_name='WU Lab - Labels S01 - S32',
        participant_label_file='_rooms/wu.txt',
    ),
    dict(
        name='wu_any',
        display_name='WU Lab - Any Label',
    ),
    dict(
        name='jvi2024',
        display_name='JVI 2024',
        participant_label_file='_rooms/jvi.txt',
    ),    
    dict(
        name='aecf2026',
        display_name='AECF 2026',
        participant_label_file='_rooms/aecf2026.txt',
    ),        
]
