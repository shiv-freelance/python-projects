# a voter (registration, vote)

# SDLC - Software Developement Life Cycle
# 1. requirement analysis
# 2. design
# 3. implmentation
# 4. validate/review it BA (demo)
# 5. raise a PR (pull requset) - reviewed (approve/change)
# 6. deployment - stg(QA) - validate/verify
# 7. production - UAT
# 8. Done.
import random
import time

from connectors import get_sql_connection


def get_all_voters(connection):
    # all voter details is in db
    cursor = connection.cursor() # cursor to execute queries

    query = "select * from voter"
    cursor.execute(query)

    all_voters = cursor.fetchall() # getting all the records

    return all_voters


def get_voter_details_by_id(connection):
    """getting voter details with voterId
    """
    voter_id = input("please enter your voterId: ")
    cursor = connection.cursor() # cursor to execute queries
    try:
        voter_id = int(voter_id)
        query = f"select * from voter where voter_id = {voter_id}"
        cursor.execute(query)
        return cursor.fetchone()
    except ValueError:
        print("Please enter valid input!")


def generate_voterId():
    return random.randint(100000, 100000000)


def create_voter_table(connection):
    try:
        query = """CREATE TABLE Voter(
                    voter_id INT PRIMARY KEY,
                    voter_name VARCHAR(255) NOT NULL,
                    voter_age INT,
                    voter_city VARCHAR(255)
        )"""
        cursor = connection.cursor()
        cursor.execute(query)
        connection.commit()

        return True
    except Exception as exce:
        print(str(exce))
        return False
    

def insert_voter_details(connection, query):
    cursor = connection.cursor()
    cursor.execute(query)
    connection.commit()
    


def vote_registration(connection):

    # db_check = create_voter_table(connection)
    # if not db_check:
    #     raise Exception("Database table creation failed.")

    name = input("Please enter your name: ")
    age = int(input(f"{name} your age please: "))
    city = input(f"{name} please enter the city name: ")
    try:
        # major and minor
        if age < 18:
            raise ValueError(f"{name} you are to young, registration failed!")
    except Exception as exce:
        print(f"Exception occured while registering: {exce}")
    else:
        voter_id = generate_voterId()
        voter = {"name": name, "age": age, "city": city}
        # voters[voter_id] = voter
        insert_query = f"""INSERT INTO Voter
                (voter_id, voter_name, voter_age, voter_city) 
                VALUES ({voter_id}, '{name}', {age}, '{city}')"""
        
        insert_voter_details(connection, insert_query)

        print("voter registration is done!")


def cast_vote(connection):
    try:
        print('please enter details to cast a vote....!')
        voter_details = get_voter_details_by_id(connection)
        if voter_details is None:
            print('voter details not found!')
        else:
            print(voter_details)
            print('please cast a vote...')
            time.sleep(10)
    except ValueError as exce:
        print(exce)
    else:
        print("voting is done!")


# template layer
def menu():
    print(
        """
    Welcome to the Voter registration platform:
          please choose
                1. registration
                2. voting
                3. get all voters
                4. get voter details by voter_id
                9. exit
"""
    )
    connection = get_sql_connection()
    while True:
        choice = input("please enter your choice: ")
        if choice == "1":
            vote_registration(connection)
        elif choice == "2":
            cast_vote(connection)
        elif choice == "3":
            print(get_all_voters(connection))
        elif choice == "4":
            voter_details = get_voter_details_by_id(connection)
            if voter_details is None:
                print('voter details not found!')
            else:
                print(voter_details)
        elif choice == "9":
            print("Please visit again!")
            break
        else:
            print("invalid choice, please try again")


menu()
