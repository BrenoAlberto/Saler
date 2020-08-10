import os
from resale_api import create_app, db
from resale_api.util.util import get_from_env

app = create_app(get_from_env("FLASK_ENV"))


@app.shell_context_processor
def shell():
    return {
        "db": db,
    }
