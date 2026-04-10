
from dbhelper.database import Database
def main():
    db = Database(
        host="localhost",
        user="root",
        password="eJx6985OK6Y7gX",
        database="testing"
    )
    db.connect()
    db.disconnect()

main()