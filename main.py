from dbhelper.database import Database
def main():
    db = Database(
        host="localhost",
        user="root",
        password="eJx6985OK6Y7gX",
        database="testing"
    )
    db.connect()
    email = "94d5ous@gmail.com"
    passwd = "uzWC67"
    db.login_validation(email, passwd)
    db.disconnect()
main()

if __name__ == "__main__":     main()