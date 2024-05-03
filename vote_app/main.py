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

voters = {
    54968937: {"name": "Sita", "age": 26, "city": "Ayodhya"},
    9673267: {"name": "Rama", "age": 30, "city": "Ayodhya"},
}


def get_all_voters():
    return voters


def generate_voterId():
    return random.randint(100000, 100000000)


def vote_registration():
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
        voters[voter_id] = voter
        print("voter registration is done!")


def cast_vote():
    voter_id = int(input("please enter your voterid: "))
    try:
        if voter_id in voters:
            print("voterId is verified")
        else:
            raise ValueError("Verification failed!")
    except ValueError as exce:
        print(exce)
    else:
        print("voting is done!")


def menu():
    print(
        """
    Welcome to the Voter registration platform:
          please choose
                1. registration
                2. voting
                3. get all voters
                9. exit
"""
    )
    while True:
        choice = input("please enter your choice: ")
        if choice == "1":
            vote_registration()
        elif choice == "2":
            cast_vote()
        elif choice == "3":
            print(get_all_voters())
        elif choice == "9":
            print("Please visit again!")
            break
        else:
            print("invalid choice, please try again")


menu()
