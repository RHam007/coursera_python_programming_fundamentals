import json
import os
import getpass  # For secure password input

def load_users(filename="users.json"):
    """
    Loads user data from a JSON file.  Handles file not found and other errors.

    Args:
        filename (str, optional): The name of the JSON file. Defaults to "users.json".

    Returns:
        dict: A dictionary containing user data, or an empty dictionary if the file
              does not exist or an error occurs.  Returns None on critical error.
    """
    try:
        if not os.path.exists(filename):
            print(f"File '{filename}' not found. Creating a new one.")
            return {}  # Return empty dict, don't create file here.

        with open(filename, 'r') as f:
            try:
                data = json.load(f)
                if not isinstance(data, dict):
                    print(f"Error: '{filename}' content is not a dictionary.  Overwriting.")
                    return {}
                return data
            except json.JSONDecodeError:
                print(f"Error: '{filename}' is not valid JSON.  Overwriting.")
                return {}  # Return empty dict on JSONDecodeError
    except (IOError, OSError) as e:
        print(f"Error reading file '{filename}': {e}")
        return None  # Indicate a more serious error



def save_users(users, filename="users.json"):
    """
    Saves user data to a JSON file.  Handles potential errors.

    Args:
        users (dict): A dictionary containing user data.
        filename (str, optional): The name of the JSON file. Defaults to "users.json".

    Returns:
        bool: True if the data was saved successfully, False otherwise.
    """
    try:
        with open(filename, 'w') as f:
            json.dump(users, f, indent=4)
        return True
    except (IOError, OSError, TypeError) as e:
        print(f"Error writing to file '{filename}': {e}")
        return False

def validate_user(users, username, password):
    """
    Validates a username and password against the provided user data.

    Args:
        users (dict): A dictionary containing user data.
        username (str): The username to validate.
        password (str): The password to validate.

    Returns:
        bool: True if the username and password are valid, False otherwise.
               Returns False if users is None or empty.
    """
    if not users:  # Check for None or empty dict
        return False
    user_data = users.get(username)  # No need for .lower() here
    if user_data:
        # Use a constant-time comparison for security if you have a stored hash
        #  (which you should in a real application).  For this example, we'll
        #  just do a direct comparison.  In a real app, *NEVER* store passwords
        #  in plaintext.  Use bcrypt, scrypt, or argon2.
        return user_data == password #  Basic password check.
    return False

def create_user(users, filename="users.json"):
    """
    Creates a new user, prompts for username and password, and adds them to the
    user data.  It saves the updated data to the JSON file.

    Args:
        users (dict): The dictionary to update with the new user.
        filename: (str): The name of the file to save the users to.

    Returns:
         bool: True if user creation and save was successful, False otherwise.
    """
    while True:
        username = input("Enter new username: ")
        if not username:
            print("Username cannot be empty. Please try again.")
            continue
        if username in users:
            print("Username already exists. Please choose a different username.")
            continue  # Continue the loop to re-prompt
        break

    while True:
        password = getpass.getpass("Enter new password: ")
        confirm_password = getpass.getpass("Confirm new password: ")
        if not password:
            print("Password cannot be empty. Please try again.")
            continue
        if password != confirm_password:
            print("Passwords do not match. Please try again.")
            continue
        break

    users[username] = password  # Store the password
    if not save_users(users, filename):
        print("Failed to save new user.")
        return False
    print(f"User '{username}' created successfully.")
    return True

def main():
    """
    Main function to run the application.
    """
    filename = "users.json"
    users = load_users(filename)  # Load user data
    if users is None:
        print("Fatal error: Could not load user data.")
        return  # Exit if loading fails

    while True:
        username = input("Enter username (or 'exit' to quit): ")
        if username.lower() == 'exit':
            break

        password = getpass.getpass("Enter password: ")  # Use getpass

        if validate_user(users, username, password):
            print("Login successful!")
            break
        else:
            print("Invalid username or password.")
            choice = input("Do you want to create a new user? (yes/no): ")
            if choice.lower() == 'yes':
                if not create_user(users, filename):
                    print("User creation failed.") # create_user prints more specific error
                    #  No need to break here, the user can try again.
                else:
                  users = load_users(filename) # Reload users.json
            elif choice.lower() == 'no':
                continue
            else:
                print("Invalid choice. Please enter 'yes' or 'no'.")

if __name__ == "__main__":
    main()

