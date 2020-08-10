from pathlib import Path
from setuptools import setup, find_packages

APP_ROOT = Path(__file__).parent
INSTALL_REQUIRES = [
    "Flask",
    "Flask-Cors",
    "Flask-Migrate",
    "flask-restx",
    "Flask-SQLAlchemy",
    "python-dotenv",
    "pymysql",
    "werkzeug==0.16.1",
]
EXTRAS_REQUIRE = {
    "dev": [
        "autopep8"
    ]
}

setup(
    name="resale-api",
    version="0.1",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    python_requires=">=3.8",
    install_requires=INSTALL_REQUIRES,
    extras_require=EXTRAS_REQUIRE,
)
