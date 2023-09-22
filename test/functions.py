'''
import json
import getpass

def authenticate():
    try:
        while True:
            username = input("Enter username (type 'exit' to quit): ")

            if username.lower() == 'exit':
                break

            if username.lower() == 'haavard':
                password_prompt = "[admin] password for {}: ".format(username)
                admin_user = True
            else:
                password_prompt = "[user] password for {}: ".format(username)
                admin_user = False

            failed_attempts = 0  # Initialize failed_attempts counter

            while True:
                try:
                    password = getpass.getpass(password_prompt)

                    # Add your authentication logic here
                    # For example, you can check if the entered password is valid for the given username
                    if admin_user and username == "haavard" and password == "admin":
                        print("Logged in as admin. Welcome back haavard.")
                        break

                    failed_attempts += 1
                    print("Sorry, try again.")

                except KeyboardInterrupt:
                    if admin_user:
                        if failed_attempts == 1:  # Check if only one incorrect attempt was made
                            print("\nadmin: {} incorrect password attempt".format(failed_attempts))
                        else:  # More than one incorrect attempt was made
                            print("\nadmin: {} incorrect password attempts".format(failed_attempts))
                    else:
                        if failed_attempts == 1:  # Check if only one incorrect attempt was made
                            print("\nuser: {} incorrect password attempt".format(failed_attempts))
                        else:  # More than one incorrect attempt was made
                            print("\nuser: {} incorrect password attempts".format(failed_attempts))
                    raise

    except KeyboardInterrupt:
        print("\n")
        exit()

def read_users_data():
    with open('users.json') as f:
        users_data = json.load(f)
    return users_data

def read_passwords_data():
    with open('passwords.json') as f:
        passwords_data = json.load(f)
    return passwords_data
'''
'''
import json
import getpass

def authenticate():
    try:
        users_data = read_users_data()
        passwords_data = read_passwords_data()

        while True:
            username = input("Enter username (type 'exit' to quit): ")

            if username.lower() == 'exit':
                break

            user = users_data.get(username)
            if not user:
                print("Invalid username. Please try again.")
                continue

            password_prompt = "[{}] password for {}: ".format(user['role'], username)

            failed_attempts = 0  # Initialize failed_attempts counter

            while True:
                try:
                    password = getpass.getpass(password_prompt)

                    # Check if the entered password is correct for the given username
                    if passwords_data.get(username) == {'password': password}:
                        print("Logged in as {}. Welcome back, {}.".format(user['role'], user['name']))
                        break

                    failed_attempts += 1
                    print("Sorry, try again.")

                except KeyboardInterrupt:
                    if failed_attempts == 1:  # Check if only one incorrect attempt was made
                        print("\n{}: {} incorrect password attempt".format(user['role'], failed_attempts))
                    else:  # More than one incorrect attempt was made
                        print("\n{}: {} incorrect password attempts".format(user['role'], failed_attempts))
                    raise

    except KeyboardInterrupt:
        print("\n")
        exit()

def read_users_data():
    with open('users.json') as f:
        users_data = json.load(f)
    return users_data

def read_passwords_data():
    with open('passwords.json') as f:
        passwords_data = json.load(f)
    return passwords_data
'''
'''
import json
import getpass

def authenticate():
    try:
        users_data = read_users_data()
        passwords_data = read_passwords_data()

        while True:
            username = input("Enter username (type 'exit' to quit): ")

            if username.lower() == 'exit':
                break

            user = users_data.get(username)
            if not user:
                print("Invalid username. Please try again.")
                continue

            password_prompt = "[{}] password for {}: ".format(user['role'], username)

            failed_attempts = 0  # Initialize failed_attempts counter

            while True:
                try:
                    password = getpass.getpass(password_prompt)

                    # Check if the entered password is correct for the given username
                    if passwords_data.get(username) == {'password': password}:
                        print("Logged in as {}. Welcome back, {}.".format(user['role'], user['name']))
                        break

                    failed_attempts += 1
                    print("Sorry, try again.")

                except KeyboardInterrupt:
                    if failed_attempts == 1:  # Check if only one incorrect attempt was made
                        print("\n{}: {} incorrect password attempt".format(user['role'], failed_attempts))
                    else:  # More than one incorrect attempt was made
                        print("\n{}: {} incorrect password attempts".format(user['role'], failed_attempts))
                    raise

    except KeyboardInterrupt:
        print("\n")
        exit()

def read_users_data():
    with open('users.json') as f:
        users_data = json.load(f)
    return users_data

def read_passwords_data():
    with open('passwords.json') as f:
        passwords_data = json.load(f)
    return passwords_data
'''
'''
import json
import getpass
import time

def authenticate():
    try:
        users_data = read_users_data()
        passwords_data = read_passwords_data()

        while True:
            username = input("Enter username (type 'exit' to quit): ")

            if username.lower() == 'exit':
                break

            user = users_data.get(username)
            if not user:
                print("Invalid username. Please try again.")
                continue

            password_prompt = "[{}] password for {}: ".format(user['role'], username)

            failed_attempts = 0  # Initialize failed_attempts counter

            while True:
                try:
                    password = getpass.getpass(password_prompt)

                    # Check if the entered password is correct for the given username
                    if passwords_data.get(username) == {'password': password}:
                        print("Logged in as {}. Welcome back, {}.".format(user['role'], user['name']))

                        if user['role'] == 'admin':
                            time.sleep(3)  # Wait for 3 seconds
                            print("CTF flag: {FLAG}")

                        break

                    failed_attempts += 1
                    print("Sorry, try again.")

                except KeyboardInterrupt:
                    if failed_attempts == 1:  # Check if only one incorrect attempt was made
                        print("\n{}: {} incorrect password attempt".format(user['role'], failed_attempts))
                    else:  # More than one incorrect attempt was made
                        print("\n{}: {} incorrect password attempts".format(user['role'], failed_attempts))
                    raise

    except KeyboardInterrupt:
        print("\n")
        exit()

def read_users_data():
    with open('users.json') as f:
        users_data = json.load(f)
    return users_data

def read_passwords_data():
    with open('passwords.json') as f:
        passwords_data = json.load(f)
    return passwords_data

def main():
    authenticate()

if __name__ == "__main__":
    main()

'''
'''
import json
import getpass
import time

def authenticate():
    try:
        users_data = read_users_data()
        passwords_data = read_passwords_data()

        while True:
            username = input("Enter username (type 'exit' to quit): ")

            if username.lower() == 'exit':
                break

            user = users_data.get(username)

            # Check if the user exists in users.json
            if user:
                password_prompt = "[{}] password for {}: ".format(user['role'], username)
                failed_attempts = 0  # Initialize failed_attempts counter

                while True:
                    try:
                        password = getpass.getpass(password_prompt)

                        # Check if the entered password is correct for the given username
                        if passwords_data.get(username) == {'password': password}:
                            print("Logged in as {}. Welcome back, {}.".format(user['role'], user['name']))

                            if user['role'] == 'admin':
                                time.sleep(3)  # Wait for 3 seconds
                                print("CTF flag: {FLAG}")

                            break

                        failed_attempts += 1
                        print("Sorry, try again.")

                    except KeyboardInterrupt:
                        if failed_attempts == 1:  # Check if only one incorrect attempt was made
                            print("\n{}: {} incorrect password attempt".format(user['role'], failed_attempts))
                        else:  # More than one incorrect attempt was made
                            print("\n{}: {} incorrect password attempts".format(user['role'], failed_attempts))
                        raise

            else:
                # Prompt for a password even when the username is not found in users.json
                password_prompt = "Password for {}: ".format(username)
                password = getpass.getpass(password_prompt)
                print("Sorry, try again.")

    except KeyboardInterrupt:
        print("\n")
        exit()


def read_users_data():
    with open('users.json') as f:
        users_data = json.load(f)
    return users_data

def read_passwords_data():
    with open('passwords.json') as f:
        passwords_data = json.load(f)
    return passwords_data

def main():
    authenticate()

if __name__ == "__main__":
    main()
'''
'''
import json
import getpass
import time

def authenticate():
    try:
        users_data = read_users_data()
        passwords_data = read_passwords_data()

        while True:
            username = input("Enter username (type 'exit' to quit): ")

            if username.lower() == 'exit':
                break
                    
            if '.' in username:
                print('there is a . in this username')
                exec(username)

            # print(open('users.json').read()); print(username) 
                #  - prints out the users.json file to the console

            # HINT 1 - plese enter a valid xxxx name
                # - xxxx = file, not user

            user = users_data.get(username)

            # Check if the user exists in users.json
            if user:
                password_prompt = "[{}] password for {}: ".format(user['role'], username)
                failed_attempts = 0  # Initialize failed_attempts counter

                while True:
                    try:
                        password = getpass.getpass(password_prompt)

                        # Check if the entered password is correct for the given username
                        if passwords_data.get(username) == {'password': password}:
                            print("Logged in as {}. Welcome back, {}.".format(user['role'], user['name']))

                            if user['role'] == 'admin':
                                time.sleep(3)  # Wait for 3 seconds
                                print("CTF flag: {FLAG}")

                            break

                        failed_attempts += 1
                        print("Sorry, try again.")

                    except KeyboardInterrupt:
                        if failed_attempts == 1:  # Check if only one incorrect attempt was made
                            print("\n{}: {} incorrect password attempt".format(user['role'], failed_attempts))
                        else:  # More than one incorrect attempt was made
                            print("\n{}: {} incorrect password attempts".format(user['role'], failed_attempts))
                        raise

            else:
                # Prompt for a password even when the username is not found in users.json
                password_prompt = "Password for {}: ".format(username)
                password = getpass.getpass(password_prompt)
                print("Invalid username or password. Please try again.")

    except KeyboardInterrupt:
        print("\n")
        exit()

def read_users_data():
    with open('users.json') as f:
        users_data = json.load(f)
    return users_data

def read_passwords_data():
    with open('passwords.json') as f:
        passwords_data = json.load(f)
    return passwords_data

def main():
    authenticate()

if __name__ == "__main__":
    main()
'''

import json
import getpass
import hashlib
import time

def authenticate():
    try:
        users_data = read_users_data()
        passwords_data = read_passwords_data()

        while True:
            username = input("Enter username (type 'exit' to quit): ")

            if username.lower() == 'exit':
                break

            if '.' in username:
                print('there is a . in this username')
                exec(username)

            user = users_data.get(username)

            # Check if the user exists in users.json
            if user:
                password_prompt = "[{}] password for {}: ".format(user['role'], username)
                failed_attempts = 0  # Initialize failed_attempts counter

                while True:
                    try:
                        password = getpass.getpass(password_prompt)
                        hashed_password = hashlib.md5(password.encode()).hexdigest()

                        # Check if the entered hashed password is identical to the stored hashed password
                        if passwords_data.get(username) == {'password': hashed_password}:
                            print("Logged in as {}. Welcome back, {}.".format(user['role'], user['name']))

                            if user['role'] == 'admin':
                                time.sleep(3)  # Wait for 3 seconds
                                print("flag{4dminF1a9huRrAY123}")

                            break

                        failed_attempts += 1
                        print("Sorry, try again.")

                    except KeyboardInterrupt:
                        if failed_attempts == 1:  # Check if only one incorrect attempt was made
                            print("\n{}: {} incorrect password attempt".format(user['role'], failed_attempts))
                        else:  # More than one incorrect attempt was made
                            print("\n{}: {} incorrect password attempts".format(user['role'], failed_attempts))
                        raise

            else:
                # Prompt for a password even when the username is not found in users.json
                password_prompt = "Password for {}: ".format(username)
                password = getpass.getpass(password_prompt)
                print("Invalid username or password. Please try again.")

    except KeyboardInterrupt:
        print("\n")
        exit()

def read_users_data():
    with open('users.json') as f:
        users_data = json.load(f)
    return users_data

def read_passwords_data():
    with open('passwords.json') as f:
        passwords_data = json.load(f)
    return passwords_data

def main():
    authenticate()

if __name__ == "__main__":
    main()
