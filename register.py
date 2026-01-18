while True:
    def user_register():
        user_info = {}
        print("\n\033[35mRegister Here\033[0m\n")
        first_name = input("Enter your First name: ").title()
        user_info["first_name"] = first_name
        last_name = input("Enter your Last name: ").title()
        user_info["last_name"] = last_name
        email = input("Enter your Email-Id: ")
        if "@" and "." in email:
            continue
        else:
            print("Invalid email id")
        user_info["email"] = email
        username = input("Create your username: ")
        user_info["username"] = username
        is_password = True
        password = input("Create password: ")
        while is_password:
            if password == username:
                print("\033[1;91mUsername and password cannot be same.\033[0m]")
                password = input("Try creating again: ")
            elif password != username:
                re_enter = input("Enter password again: ")
                user_info["Password"] = re_enter
                break
        print("Registeration Successful")

    register = input("Enter 'Yes' for registeration: ").lower()
    if register == "yes":
        user_register()
    elif register == "n":
        break
