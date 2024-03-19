import psycopg

# The studentExists function is a helper function which takes a student_id as a parameter.
# The function executes a query to the database to check if there exists a Student with the given student_id.
# The function returns True if there exists a Student with the given student_id and False if there doesn't exist a Student with the given student_id.
def studentExists(student_id):
    # Connecting to the database.
    connection = psycopg.connect("dbname=COMP3005Assignment3 user=postgres host=localhost port=5432 password=postgres")
    cur = connection.cursor()

    # Executing a query to retrieve the Student with the given student_id.
    cur.execute(""" SELECT *
                    FROM STUDENTS
                    WHERE student_id = %d;
                """ % (student_id))

    # Storing an array containing the query results in a variable.
    result = cur.fetchall()

    # Checking the size of the array containing the query results.
    # If the array size is 0, the function returns False as it means there doesn't exist a Student with the given student_id.
    # Otherwise, the function will return True.
    if(len(result) == 0):
        return False
    return True


# The getAllStudents function makes a query to retrieve all the tuples in the Students relation.
def getAllStudents():

    # Trying to connect the database and retrieve all the tuples from the Students relation.
    try:
        # Connecting to the database.
        connection = psycopg.connect("dbname=COMP3005Assignment3 user=postgres host=localhost port=5432 password=postgres")

        cur = connection.cursor()

        # Executing the query to get all the student tuples
        cur.execute("""
                        SELECT *
                        FROM STUDENTS;
                        """)
        # Storing an array containing the query results in a variable.
        results = cur.fetchall()

        # Outputting the results stored in the array.
        for i in range(0, len(results)):
            print(results[i])

        connection.commit()

    # If the database does not exist
    except psycopg.OperationalError:
        print("The database does not exist or connection to database has failed")
    # If the Students relation hasn't been made yet.
    except psycopg.errors.UndefinedTable:
        print("The relation you are trying to access does not exist")


# The addStudent function is used to add a new Student to the Students table.
# The function sends a query to the database to insert a new Student tuple in the Students table.
# A try-except block is being used to help deal with potential errors in the values passed into the function.
def addStudent(first_name, last_name, email, enrollment_date):


    # Trying to connect to the database and execute the query for inserting the new Student into the Students table.
    try:
        # Connecting to the database.
        connection = psycopg.connect("dbname=COMP3005Assignment3 user=postgres host=localhost port=5432 password=postgres")

        cur = connection.cursor()

        # Executing the query to insert into the table
        cur.execute("INSERT INTO students (first_name, last_name, email, enrollment_date) VALUES (%s, %s, %s, %s);",
                    (first_name, last_name, email, enrollment_date))
        connection.commit()

    # When there already exists a student with the given email/information.
    except psycopg.errors.UniqueViolation:
        print("Student already exists")

    # When an invalid date has been entered for the to-be added student.
    except psycopg.errors.InvalidDatetimeFormat:
        print("Verify that the right date has been inserted")

    # If the database we are trying to connect to doesn't exist/isn't successful.
    except psycopg.OperationalError:
        print("The database does not exist or connection to database has failed")

    # If the Students relation hasn't been made yet.
    except psycopg.errors.UndefinedTable:
        print("The relation you are trying to access does not exist")






# The updateStudentEmail function is used to update the email of an existing student with the given student_id.
# The function takes in a student_id and an email address as the parameters.
def updateStudentEmail(student_id, new_email):

    # Trying to connect to the database and update the students email with new_email.
    try:
        # Connecting to the database.
        connection = psycopg.connect("dbname=COMP3005Assignment3 user=postgres host=localhost port=5432 password=postgres")
        cur = connection.cursor()


        # If the given student_id is not a number or is a string containing a number, a message is printed indicating the function's input is invalid.
        if (str(student_id).isnumeric()==False):
            print("Make sure student_id is a number")
        elif(studentExists(student_id)==False):
            print("No student exists with this given ID")

        # Updating the table with this new Students tuple.
        else:
            cur.execute("""
                                   UPDATE students
                                   SET email = (%s)
                                   WHERE student_id = (%s);
                                   """,(new_email, student_id))

        connection.commit()
    # If the Students relation hasn't been made yet.
    except psycopg.errors.UndefinedTable:
        print("The relation you are trying to access does not exist")

    # If the database we are trying to connect to doesn't exist/isn't successful.
    except psycopg.OperationalError:
        print("The database does not exist or connection to database has failed")



# The deleteStudent function is used to delete a student by finding using the given student_id.
# The function takes in a student_id as a parameter.
def deleteStudent(student_id):

    # Trying to connect to the database and delete the student with the given student_id.
    try:
        # Connecting to the database
        connection = psycopg.connect("dbname=COMP3005Assignment3 user=postgres host=localhost port=5432 password=postgres")
        cur = connection.cursor()

        # If the entered student_id is not a number.
        if (str(student_id).isnumeric() == False):
            print("Make sure student_id is a number")

        # If there doesn't exist a Student with the given student_id.
        elif(studentExists(student_id)==False):
            print("No student exists with the given ID or that student has already been deleted.")

        # Finding the student with the given student_id and deleting them from the table.
        else:
            cur.execute("""
                        DELETE FROM students
                        WHERE student_id = %d
                        """ %(student_id))

        connection.commit()

    # If the Students relation hasn't been made yet
    except psycopg.errors.UndefinedTable:
        print("The relation you are trying to access does not exist")

    # If the database we are trying to connect to doesn't exist/isn't successful
    except psycopg.OperationalError:
        print("The database does not exist or connection to database has failed")

#Function calls(These calls were used in the video for testing)

#getAllStudents()

#addStudent("Ash","Win","as@gmail.com","2023-09-01")

#updateStudentEmail(1,"JDoe@hotmail.com")

#deleteStudent(4)

