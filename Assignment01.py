#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Python Registration and Login System

import re


# create a function for registration of new user
def register():
    
    Users = open(r"D:\Data_Science\Users.txt", "r")
    Username = input("(example: abc123@yahoo.in) \nCreate Username: ")
    Password = input("(password length should be between 8 to 16, Must have minimum one special character(/,@,#,$,%,^,&,!), one digit, one uppercase, one lowercase character)\nCreate Password: ")
    Confirm_Password = input("Confirm Password: ")
    Pattern = "^[a-z][0-9,.!$%*<>:|\]*@[a-z]*.[a-z]{2,3}"
    un = re.findall(Pattern, Username)
    Pattern2 = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{6,15}$"
    pw = re.findall(Pattern2, Password)
    
    
    if Username not in un:
        print("Refer to the example given, Try again")
        register()
    elif Password not in pw:
        print("Refer to the Password description, Try again")
        register()
    else:
        pass
        
    U = []
    P = []
    for i in Users:
        a,b = i.split(",")
        b = b.strip()
        U.append(a)
        P.append(b)
        
    data = dict(zip(U, P))

    
    if Password != Confirm_Password:
        print("Passwords does not match, Try again")
        register()
        
    else:
        if len(Password) < 5 and len(Password) > 16:
            print("Password is too short or too long, Try again")
            register()
            
        elif Username in U:
            print("Username already exist, Try again")
            register()
      
        else:
            Users = open(r"D:\Data_Science\Users.txt", "a")
            Users.write(Username + " , " + Password + "\n")
            print("You have been successfully registered")
            print("You can Login to your account now.")
            Home()




# create a function to login into existing user
def login():
    Users = open(r"D:\Data_Science\Users.txt", "r")
    Username = input("Enter Username : ")
    Password = input("Enter Password : ")


    if not len(Username or Password) < 1:
        U = []
        P = []
        for i in Users:
            a,b = i.split(", ")
            b = b.strip()
            U.append(a)
            P.append(b)
        data = dict(zip(U, P))

        try:
            if data[Username]:
                try:
                    if Password == data[Username]:
                        print("Login Success")
                        print("Hi, " + Username)
                    else:
                        print("Username or Password incorrect, Try again")
                        login()
                except:
                    print("Username or Password incorrect, Try again")
                    login()
            else:
                print("Username does not exist, Register first")
                register()
        except:
            print("Login error")
            register()
    else:
        print("Please enter a value")
        login()


def Home():
    option = input("Login | Signup : ")
    if option == "Login":
        login()
    elif option == "Signup":
        register()
    else:
        print("Please enter an option")

Home()

