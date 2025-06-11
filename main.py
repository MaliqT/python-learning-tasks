# The focal point of orchestrating the tasks together, combining the logic and weaving it to do what we need it to do

from user_information import get_user_info, user_summary


def main():
    accounts = get_user_info()

    user_summary(accounts)


if __name__ == "__main__":
    main()