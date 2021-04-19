import connection
import students
import teachers
import courses
import grades

def main():
    db = connection.connect_to_db()
    # do some stuff
    db.close()

def execute_operation(db, operation):
    print("Execute")
    cursor = db.cursor()
    cursor.execute(operation)

if __name__ == "__main__":
    main()