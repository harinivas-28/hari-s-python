#username=input("Enter Username:")
def check_password():
    password=input("Enter Password:")
    confirm=input("Confirm Password:")
    a=password.count('#')
    b=password.count('$')
    if password==confirm:
        if len(password)<9:
            if len(password)>4:
                if password[0] is not password.isdigit():
                    if '#' or '$' in password:
                        if a==b:
                            print("Password must contain \'#\' or \'$\'")
                        elif a>0 and b>0:
                            print("Password must contain only one symbol")
                        elif a>1 or b>1:
                            print("Password must contain only one symbol")
                        else:
                            for x in password:
                                if x.isupper():
                                    break
                            print(f"{password} is Valid Password")
                            exit()
                    else:
                        print("Password must contain \'#\' or \'$\'")
                else:
                    print('Password does not start with a number')
            else:
                print("Password should contain more than 4 charcters")
        else:
            print("Password does not execede 8 characters")
    else:
        print("Password must be equal to Confirm Password")
check_password()

