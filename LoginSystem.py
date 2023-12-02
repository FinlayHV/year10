
def RegisterUsername():
        PrevUser = str()

        username = input("Enter a username: ")

        
        with open('Logins.txt' , 'r') as f:
                for line in f:
                        PrevUser = line.strip()
                        while username == PrevUser:
                                username = input('This username already exists\nEnter a new username: ')
                        
        return username



def RegisterPassword():

        password = input("Enter a Password: ")
        
        return password

        

def EnterUsername():
        
        username = input("Enter a username: ")

        return username

                        

def EnterPassword():

        password = input("Enter a Password: ")
        
        return password


def StrengthChecker(Input):                                
        lower = False
        upper = False
        number = False
        for char in Input:
                if char.islower() == True:
                        lower = True
                elif char.isupper() == True:
                        upper = True
                elif char.isnumeric() == True:
                        number = True
        if lower == True and upper == True and number == True:
                return 'STRONG'
        elif (lower == True and upper == True) or (lower == True and number == True) or (upper == True and number == True):
                return 'MEDIUM'
        elif lower == True or upper == True or number == True:
                return 'WEAK'

                

def LengthChecker(Input):
        length = len(Input)
        
        if length < 6 or length > 12:
                return False

        else:
                return True
        







        



Username = str()
Password = str()
strength = str()
Pacceptable = bool()
Uacceptable = bool()
                          
Option = str()

with open('Logins.txt' , 'a') as f:
        f.write('File created')

with open('Logins.txt', 'r') as file:
        lines = file.readlines()
        print(lines)

with open('Logins.txt' , 'w') as file:
        file.writelines(lines[:-1])



while Option != '4':

        Option = input("what would you like to do?\nType '1' to register a new user\nType '2' to login to your account\nType '3' to change your login details\nType '4' to quit\n")
        
        if Option == '1':

                #Register User

                Uacceptable = bool(False)
                
                while Uacceptable == False:
                        Username = RegisterUsername()
                        Uacceptable = LengthChecker(Username)

                Pacceptable = bool(False)

                while Pacceptable == False:
                        Password = RegisterPassword()
                        Pacceptable = LengthChecker(Password)
                
                strength = StrengthChecker(Password)


                with open('Logins.txt' , 'a') as f:
                        f.write(Username)
                        f.write('\n')
                        f.write(Password)
                        f.write('\n')



                
                print('Your username and password have been saved!\nYour password strength is' , strength)
                if strength != 'STRONG':
                        print('To improve your password strength, make sure you have a:\n- lowercase caracter\n- uppercase caracter\n- number.\nE.G. exaMple7')







        elif Option == '2':

                #Login

                Uattempt = input('Enter your username: ')
                Pattempt = input('Enter your Password: ')
                Pline = int(0)

                
                

               
        
                print('Work In Progress')

                with open('Logins.txt' , 'r') as f:
                        for line in f:

                                line = line.strip()
                                print(line)
                                if Uattempt == line:
                                            print('accepted')
                                Pline = Pline + 1


                with open('Logins.txt' , 'r') as f:
                        for line in f:

                                line = line.strip()
                                print(line)
                                if Pattempt == line:
                                    print('accepted')
                





                        
                #LoginDetails = f.readline()
                #print(LoginDetails)
                                        







        elif Option == '3':

                #Change Login Details
                
                print('Work In Progress')
        
        elif Option == '4':

                #Quit
                
                print('Goodbye!')

        else:

                #Invalid Option
                
                print("That isn't a option!")


        





