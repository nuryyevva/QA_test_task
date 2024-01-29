from pathlib import Path

from split_settings.tools import include, optional

include(
    "components/database.py",
    "components/drf.py",
    "components/hosts.py",
    "components/middleware.py",
    "components/templates.py",
    "components/consts.py",
    "components/validators.py",
    "components/djoser.py",
    "components/apps.py",
    "components/jwt.py",
)
