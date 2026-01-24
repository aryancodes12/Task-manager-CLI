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

user_id = f"u{counter:03d}"

def names():
    first_name = input("Enter your First name: ")
    last_name = input("Enter your Last name: ")
    full_name = f"{first_name} {last_name}"
    return full_name

def username():
    username = input("Create username:")
    if username in user_id:
        console.print(f"Username is already taken.", style= "bold red")
    else:
        return username


#Adding the DATA in Dict user_info
def email_ids():
    flag = True
    while flag:
        email_id = input("Enter email id:")
        if "@" and "." in email_id:
            return email_id
        else:
            console.print(f"\nInvalid Email.\n", style= "bold red")

#Registeration main fuction
# def user_registeration():
#     console.print("Registeration Section", style="bold cyan")
#     first_name = input("Enter First Name:").title()
#     last_name = input("Enter Last Name:").title()
    
    
#     password = input("Create a password:")
#     re_enter = input("Re-Enter the password:")

    
    








#Asking for permission to begin registeration
active = True
while active:
    register = input("Enter 'y/n' for registeration: ").lower()
    if register == "y":
        names()
        print(full_name)
        email_ids()
        username()
    elif register == "n":
        active = False



user_info[user_id] = {
    "Full_Name" : full_name,
    "Email" : email,
    "Username" : username,
    "Password" : re_enter,
}


try:
    with open(file_name, "w") as f:
        json.dump(user_info, f)
except FileNotFoundError:
    pass
else:
    print("DATA IS SAVED")

print("User DATA:")
for k, v in user_info.items():
    print(k)
    for k1, v1 in v.items():
        print(k1, ":", v1)
