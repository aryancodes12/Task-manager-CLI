import json
from rich.console import Console

console = Console()

#Loading the DATA from JSON
file_name = "user_data.json"
try:
    with open(file_name) as f:
        user_info = json.load(f)
except FileNotFoundError:
    console.print("File does not exist", style="bold red")
else:
    print("Previous data is loaded")

#Tracking the current user id from the JSON file
user_info = {}
if user_info:
    counter = max(int(uid[1:]) for uid in user_info.keys()) + 1
else:
    counter = 1



#Registeration main fuction
def user_registeration():
    console.print("Registeration Section", style="bold cyan")
    first_name = input("Enter First Name:").title()
    last_name = input("Enter Last Name:").title()
    email_id = input("Enter email id:")
    username = input("Create username:")
    password = input("Create a password:")
    re_enter = input("Re-Enter the password:")

    #Adding the DATA in Dict user_info

    user_id = f"u{counter:03d}"
    user_info[user_id] = {
        "First_Name": first_name,
        "Last_Name": last_name,
        "Email_id": email,
        "Username": username,
        "Password": re_enter,
        }
    

#Asking for permission to begin registeration
active = True
while active:
    register = input("Enter 'y/n' for registeration: ").lower()
    if register == "y":
        user_registeration()
    elif register == "n":
        active = False






try:
    with open(file_name, "w") as f:
        json.dump(user_info, f)
except FileNotFoundError:
    pass
else:
    print("DATA IS SAVED")

print("User DATA:")
for k, v in user_info.items():
    print(k, ":", v)
