# Clients  = Harry , Person1 , Person2
# Make 6 files to monitor exercise and diet
# 'w ' mode creates a new file if it doesnt exist.
import time
import datetime
def monitor(name = input("Enter your name\t")):
    number = str(input("Enter 1 for diet and 2 for exercise updates\t"))
    if name.lower() != "harry" and name.lower() != "persona" and name.lower() != "personb":
        print("You are not authorised to use this.")
    elif name.lower() == "harry" and number == "1":
        what_i_ate = str(input("Please enter what you ate\t"))
        with open("Harry_diet.txt" , "r+") as hd:
            hd.write(f"[{datetime.datetime.now()}] -> {what_i_ate}")
            print("Your previous  logs : ")
            time.sleep(1)
            print(hd.readlines())
    elif name.lower()=="harry" and number =="2":
        with open("Harry_exercise.txt" , "r+") as he:
            what_i_did = str(input("Please enter what you did\t"))
            he.write(f"[{datetime.datetime.now()}] -> {what_i_did}")
            print("Your previous  logs : ")
            time.sleep(1)
            print(he.readlines())
    elif name.lower()=="persona" and number =="1":
        with open("Persona_diet.txt" , "r+") as pd:
            what_i_did = str(input("Please enter what you ate\t"))
            pd.write(f"[{datetime.datetime.now()}] -> {what_i_did}")
            print("Your previous  logs : ")
            time.sleep(1)
            print(pd.readlines())
    elif name.lower()=="persona" and number =="2":
        with open("Persona_exercise.txt" , "r+") as pe:
            what_i_did = str(input("Please enter what you did\t"))
            pe.write(f"[{datetime.datetime.now()}] -> {what_i_did}")
            print("Your previous  logs : ")
            time.sleep(1)
            print(pe.readlines())
    elif name.lower()=="personb" and number =="1":
        with open("Personb_diet.txt" , "r+") as p_d:
            what_i_did = str(input("Please enter what you ate\t"))
            p_d.write(f"[{datetime.datetime.now()}] -> {what_i_did}")
            print("Your previous  logs : ")
            time.sleep(1)
            print(p_d.readlines())
    elif name.lower()=="personb" and number =="2":
        with open("Personb_exercise.txt" , "r+") as p_e:
            what_i_did = str(input("Please enter what you did\t"))
            p_e.write(f"[{datetime.datetime.now()}] -> {what_i_did}")
            print("Your previous  logs : ")
            time.sleep(1)
            print(p_e.readlines())
monitor()

