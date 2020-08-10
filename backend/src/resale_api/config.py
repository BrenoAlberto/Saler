"""Config settings for for development and testing environments."""
from resale_api.util.util import get_from_env


MYSQL_DEV = get_from_env("MYSQL_CONN")
MYSQL_TEST = get_from_env("MYSQL_CONN_TEST")


class Config:
    """Base configuration."""

    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SWAGGER_UI_DOC_EXPANSION = "list"
    RESTX_MASK_SWAGGER = False


class TestingConfig(Config):
    """Testing configuration."""

    TESTING = True
    SQLALCHEMY_DATABASE_URI = MYSQL_TEST


class DevelopmentConfig(Config):
    """Development configuration."""

    SQLALCHEMY_DATABASE_URI = MYSQL_DEV


ENV_CONFIG_DICT = dict(
    development=DevelopmentConfig, testing=TestingConfig
)


def get_config(config_name):
    """Retrieve environment configuration settings."""
    return ENV_CONFIG_DICT.get(config_name, DevelopmentConfig)
