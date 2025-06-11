# The focal point of orchestrating the tasks together, combining the logic and weaving it to do what we need it to do

import user_information


def main():
    info = []

    while info == []:
        accounts = user_information.get_user_info()
        user_information.save_user_info(accounts)
        info = user_information.load_user_info()


    user_information.user_summary(info)

if __name__ == "__main__":
    main()