import json

file_name = "user_data.json"
try:
    with open(file_name) as f:
        user_info = json.load(f)
except FileNotFoundError:
    print("File does not exist")
else:
    print("Previous data is loaded")

user_info = {}
counter = 1
while True:
    user_id = f"u{counter:03d}"

    def user_register():
        print("\n\033[35mRegister Here\033[0m\n")
        first_name = input("Enter your First name: ").title()
        last_name = input("Enter your Last name: ").title()
        email = input("Enter your Email-Id: ")
        username = input("Create your username: ")
        is_password = True
        password = input("Create password: ")
        while is_password:
            if password == username:
                print("\033[1;91mUsername and password cannot be same.\033[0m")
                password = input("Try creating again: ")
            elif len(password) < 8:
                print("Password should be greater than 8 character")
                password = input("Enter password: ")
            else:
                re_enter = input("Enter password again: ")
                is_password = False 
        user_info[user_id] = {
            "First_Name": first_name,
            "Last_Name": last_name,
            "Email_Id": email,
            "Username": username,
            "Password": re_enter,
            }
        print("Registeration Successful")


    register = input("Enter 'y/n' for registeration: ").lower()
    if register == "y":
        user_register()
        counter += 1
    elif register == "n":
        break

try:
    with open(file_name, "w") as f:
        json.dump(user_info, f)
except FileNotFoundError:
    pass
else:
    print("DATA IS SAVED")

print("\nUser DATA:\n")
for uid, infos in user_info.items():
    print(f"\033[1;92mUser ID->\033[0m {uid}")
    for k, v in infos.items():
        print(f"\t{k} ->\033[1;93m{v}\033[0m")
        print()
