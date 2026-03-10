import os

"""
Default runs in unsolved mode, where pages has empty main() func
If env variable SOLUTION is set then shows the solved mode (for teachers or just show case)
"""

if os.getenv("USE_SOLVED") == '1':
    from apps.solution import currency, password, weather, youtube
else:
    from apps import currency, password, weather, youtube


app_list = (
    password,
    currency,
    weather,
    youtube,
)
