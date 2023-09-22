import getpass

def authenticate():
    try:
        while True:
            username = input("Enter username (type 'exit' to quit): ")
            
            if username.lower() == 'exit':
                print("Exiting...")
                break
            
            if username.lower() == 'haavard':
                password_prompt = "[admin] password for {}: ".format(username)
            else:
                password_prompt = "[user] password for {}: ".format(username)
                
            password = getpass.getpass(password_prompt)

            # Add your authentication logic here
            # For example, you can check if the entered username and password are valid
            if username == "haavard" and password == "admin":
                print("Logged in as admin. Welcome back haavard.")
                break
            
            failed_attempts = 1
            
            while True:
                try:
                    password = getpass.getpass(password_prompt)
                    
                    # Add your authentication logic here
                    # For example, you can check if the entered password is valid for the given username
                    if username == "haavard" and password == "admin":
                        print("Logged in as admin. Welcome back haavard.")
                        break
                    
                    failed_attempts += 1
                    print("Sorry, try again.")
                
                except KeyboardInterrupt:
                    print("\nuser: {} incorrect password attempts".format(failed_attempts))
                    raise
            
    except KeyboardInterrupt:
        print("\nExiting...")
        exit()

# Call the authenticate function
authenticate()
