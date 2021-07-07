# In this project we will make an fucntion in will ask the name of the client and asking for what you have diet and what you
# done for exercise and print the date 

def getdate():
    import datetime
    return datetime.datetime.now()
print("                                         Welcome! This is the Health Management System")
print("                                              Our Clients are (Harry,Rohan,Hammad)\n\n")
retrive_log = input("Do you want to retrive or log: ")

def HealthReport():
    if retrive_log == "log":
        while True:
            name_client = input("Please Enter the name of client: ")
            try:
                if name_client == "Harry" or name_client == "harry":
                    client_Log = input("You have to Log for Diet or Exercise: ")
                    try:
                        if client_Log == "Diet" or client_Log == "diet":
                            Harrry_Diet = input("What you have eat Harry: ")
                            with open("D:\\A PYTHON_BEGGINER\\Projects\\Health_Management_System\\Harry_Diet.txt",'w') as f:
                                f.write(Harrry_Diet)
                            print(f"{getdate()}     You have succesfully entered Health Report")
                            break
                        elif client_Log == "Exercise" or client_Log == "exercise":
                            Harrry_Exercise = input("What you have exercise: ")
                            with open("D:\\A PYTHON_BEGGINER\\Projects\\Health_Management_System\\Harry_Exercise.txt",'w') as f:
                                f.write(Harrry_Exercise)
                            print(f"{getdate()}     You have succesfully entered Health Report")
                            break
                    except Exception as e:
                        print(e)


                elif name_client == "Rohan" or name_client == "rohan":
                    client_Log = input("You have to Log for Diet or Exercise: ")
                    try:
                        if client_Log == "Diet" or client_Log == "diet":
                            Rohan_Diet = input("What you have eat Rohan: ")
                            with open("D:\\A PYTHON_BEGGINER\\Projects\\Health_Management_System\\Rohan_Diet.txt",'w') as f:
                                f.write(Rohan_Diet)
                            print(f"{getdate()}     You have succesfully entered Health Report")
                            break
                        elif client_Log == "Exercise" or client_Log == "exercise":
                            Rohan_Exercise = input("What you have exercise: ")
                            with open("D:\\A PYTHON_BEGGINER\\Projects\\Health_Management_System\\Rohan_Exercise.txt",'w') as f:
                                f.write(Rohan_Exercise)
                            print(f"{getdate()}     You have succesfully entered Health Report")
                            break
                    except Exception as e:
                        print(e)

                elif name_client == "Hammad" or name_client == "hammad":
                    client_Log = input("You have to Log for Diet or Exercise: ")
                    try:
                        if client_Log == "Diet" or client_Log == "diet":
                            Hammad_Diet = input("What you have eat Hammad: ")
                            with open("D:\\A PYTHON_BEGGINER\\Projects\\Health_Management_System\\Hammad_Diet.txt",'w') as f:
                                f.write(Hammad_Diet)
                            print(f"{getdate()}     You have succesfully entered Health Report")
                            break
                        elif client_Log == "Exercise" or client_Log == "exercise":
                            Hammad_Exercise = input("What you have exercise: ")
                            with open("D:\\A PYTHON_BEGGINER\\Projects\\Health_Management_System\\Hammad_Exercise.txt",'w') as f:
                                f.write(Hammad_Exercise)
                            print(f"{getdate()}     You have succesfully entered Health Report")
                            break
                    except Exception as e:
                        print(e)
                        
            except Exception as e:
                print(e)

def Health_retrive():
    if retrive_log == "retrive" or retrive_log == "Retrive":
        while True:
            retrive_client = input("You have to retrive the data of which Client: ") 
            try:
                if retrive_client == "Harry" or retrive_client == "harry":
                    retrive_diet_exer = input("You wanna to retrive diet or exercise plan: ")
                    try:
                        if retrive_diet_exer == "Diet" or retrive_diet_exer == "diet":
                            with open("D:\\A PYTHON_BEGGINER\\Projects\\Health_Management_System\\Harry_Diet.txt") as f:
                                content = f.readlines()
                                print(content)
                                break
                        elif retrive_diet_exer == "Exercise" or retrive_diet_exer == "exercise":
                            with open("D:\\A PYTHON_BEGGINER\\Projects\\Health_Management_System\\Harry_Exercise.txt") as f:
                                content = f.readlines()
                                print(content)
                                break
                    except Exception as e:
                        print(e)

                if retrive_client == "Rohan" or retrive_client == "rohan":
                    retrive_diet_exer = input("You wanna to retrive diet or exercise plan: ")
                    try:
                        if retrive_diet_exer== "Diet" or retrive_diet_exer == "diet":
                            with open("D:\\A PYTHON_BEGGINER\\Projects\\Health_Management_System\\Rohan_Diet.txt") as f:
                                content = f.readlines()
                                print(content)
                                break
                        elif retrive_diet_exer == "Exercise" or retrive_diet_exer == "exercise":
                            with open("D:\\A PYTHON_BEGGINER\\Projects\\Health_Management_System\\Rohan_Exercise.txt") as f:
                                content = f.readlines()
                                print(content)
                                break
                    except Exception as e:
                        print(e)

                if retrive_client == "Hammad" or retrive_client == "hammad":
                    retrive_diet_exer = input("You wanna to retrive diet or exercise plan: ")
                    try:
                        if retrive_client == "Diet" or retrive_client == "diet":
                            with open("D:\\A PYTHON_BEGGINER\\Projects\\Health_Management_System\\Hammad_Diet.txt") as f:
                                content = f.readlines()
                                print(content)
                                break
                        elif retrive_diet_exer == "Exercise" or retrive_client == "exercise":
                            with open("D:\\A PYTHON_BEGGINER\\Projects\\Health_Management_System\\Hammad_Exercise.txt") as f:
                                content = f.readlines()
                                print(content)
                                break
                    except Exception as e:
                        print(e)
            except Exception as e:
                print("Client name is not defined")        
        
HealthReport()
Health_retrive()