import os
from dotenv import load_dotenv

load_dotenv(".env")


def get_from_env(variable):
    return os.getenv(variable)
