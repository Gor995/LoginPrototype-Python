import os

class page1:
    def __init__(self, login = "", password = ""):
        self.login = login
        self.password = password
        self.checkoption() # Calls user choice function 
        pass

    def checkoption(self):
       with open('log.txt', "r") as self.file_obj: # Set log.txt as a variable
        first_line = self.file_obj.readline()  # Read the first line
        if not first_line:  # Check for empty line
            print("No login credentials found in local file\n")
        else:
            self.login = first_line.strip()  # Remove trailing newline
            self.password = str(self.file_obj.readline()).strip()
            print("Login credentials found in local file\n")
            
        while True:
            print("Do you wish to login or register?")
            self.checkinp = input("Register/Login: ")
            print("")

            if self.checkinp.upper() == "REGISTER":
                self.register()
                break
            elif self.checkinp.upper() == "LOGIN":
                self.loginFunc()
                break   
            else:
                print("This is not a option...\n")
                continue

    def register(self):
        while True: #Logging registration
            print("Warning, logging is only saved locally after first logging to file.\n")
            self.registerlogin = input("Register Login: ")
            print("Your login is: ", self.registerlogin, "Is this correct? (Y/N)")
            self.loginconfirmation = input()

            if self.loginconfirmation.upper() == "Y":
                print("")
                break
            elif self.loginconfirmation.upper() == "N":
                print("")
                continue
            else:
                print("\nInvalid input. Please enter Y or N.\n")

        while True: #Password registration
            self.registerpassword = input("Register Password: ")
            print("Your password is: ", self.registerpassword, " Is this correct? (Y/N)")
            self.passwordconfirmation = input()    
            
            if self.passwordconfirmation.upper() == "Y":
                print("\nLogin: ", self.registerlogin, "Password: ", self.registerpassword,"\n")
                self.login = self.registerlogin
                self.password = self.registerpassword
                self.loginFunc()
                return
            elif self.passwordconfirmation.upper() == "N":
                print("")
                continue
            else:
                print("\nInvalid input. Please enter Y or N.\n")
            
    def loginFunc(self):

        print("System Protype V0.01 Login:")
        print("Login and password are case sensitive!\n")

        if not self.login or not self.password: # Anti-crash in case there are no logins in log 
            print("There is no logged logins.\n")
            self.checkoption()
            return

        while True: # Checks if Login is correct
            self.dologin = input("Login: ")
            if self.dologin == self.login:
                print("Login correct...\n")
                break
            else:
                print("Login incorrect, try again.\n")

        while True: # Checks if Password is correct
            self.dopassword = input("Password: ")
            if self.dopassword == self.password and self.dologin == self.login:
                print("Password correct, proceeding to page...\n")
                user2 = page2(self)
                user2.PageFunc()
                with open("log.txt", "w") as f:  # Open in write mode to overwrite
                    f.write(str(self.login) + "\n" + str(self.password)) # Writes new log
                return self.login, self.password  # Return login/password for page2   
            else:
                print("Password incorrect, try again.\n")

class page2:
    def __init__(self, self_obj):
        self.self_obj = self_obj  # Store the page1 instance
        self.PageFunc()
        pass

    def PageFunc(self):
        self.x = open("log.txt", "r")
        print("Last saved login (does not show currently saved login):", self.x.read()) # Debug printing

user1 = page1()