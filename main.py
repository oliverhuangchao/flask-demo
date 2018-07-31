from app import app
from db_action import DBActionHandler

if __name__ == "__main__":
    dbhandler = DBActionHandler()
    dbhandler.init_db()
    app.run()
