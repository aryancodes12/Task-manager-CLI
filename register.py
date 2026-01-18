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
while True:
    def user_register():
        print("\n\033[35mRegister Here\033[0m\n")
        first_name = input("Enter your First name: ").title()
        user_info["first_name"] = first_name
        last_name = input("Enter your Last name: ").title()
        user_info["last_name"] = last_name
        while True:
            email = input("Enter your Email-Id: ")
            if "@" and "." in email:
                user_info["email"] = email
                break
            else:
                print("Invalid email id")
        username = input("Create your username: ")
        if username not in user_info:
            user_info["username"] = username
        elif username in user_info:
            print("\033[1;91mUsername is already taken.\033[0m")
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
            elif password != username:
                re_enter = input("Enter password again: ")
                if re_enter != password:
                    print("\033[1;92mPassword doesn't match.\033[0m")
                    re_enter = input("Enter password again: ")
                else:
                    user_info["Password"] = re_enter
                    break
        print("Registeration Successful")

        print(user_info)

    register = input("Enter 'y/n' for registeration: ").lower()
    if register == "y":
        user_register()
    elif register == "n":
        break

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
