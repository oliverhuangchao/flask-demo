import os

WORKING_DIR = os.environ.get("FLASK_WORKING_DIR")
DB_PATH = os.path.join(WORKING_DIR, "var/data/main.db")
USER_TABLE = "users"
TEMPLATE_DIR = os.path.join(WORKING_DIR, "templates")
STATIC_DIR = os.path.join(WORKING_DIR, "static")

