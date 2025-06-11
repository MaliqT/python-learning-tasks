# Prompt the user for their information:
# Full name
# Age
# Favorite programming language

def get_user_info():

    # Empty dict to store user information and empty list to store information of each user
    user_info = {}
    accounts = []
    new_user = "yes"

    while new_user == "yes":
        user_info["name"] = input("Enter your full name: ")
        while True:
            age = input("Enter your age: ")
            if age.isdigit() and int(age) > 0:
                user_info["age"] = int(age)
                break
            else:
                print("Enter a number please and must be greater than 0")
        
        user_info["programming_language"] = input("What is your favorite programming language? : ")
        accounts.append(user_info)
        user_info = {}

        new_user = input("Add another user? (yes/no): ")

        while new_user != "yes" and new_user != "no":
            new_user = input("Add nother user? (yes/no): ")

        if new_user == "no":
            break



    return accounts



def user_summary(user_accounts):
    # Extract user data from the list of dictionaries user_accounts and print them

    print("Summary of users:\n")
    counter = 1

    for account in user_accounts:
        username = account["name"]
        age = account["age"]
        prog_lang = account["programming_language"]

        print(str(counter) + ". " + f"{username}, {age} years old, favorite language: {prog_lang}")
        counter += 1
