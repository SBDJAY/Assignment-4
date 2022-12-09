#-----------------------------------------------------------
# Class Realtaionships and seperations of concerns
# Daniel Pius
# Muhammad Asif
# Class: 1229_4013: Programming Principles
# November 22, 2022
#-----------------------------------------------------------
#IMPORTS
import json, colorama
from colorama import Fore, Back
#-----------------------------------------------------------
#JSON
jl_data = 'Databases/JusticeLeagueDatabaseV2.json'
#-----------------------------------------------------------
#CREATE COPY of JSON
def write_json(data, filename= "JusticeLeagueDatabaseV2.json"):
    with open(filename, "w") as f:
        json.dump(data, f, indent=4)

with open (jl_data, 'r') as jl_file:
    data = json.load(jl_file)
    write_json(data)
    temp = data["Justice League Members"]
    temp.append("Copy")
#-----------------------------------------------------------
#ADD DATA
def add_jl(data , jl_data="JusticeLeagueDatabaseV2.json"):
    jl_memb_data = {}
    with open (jl_data, "r") as js_addfile:
        temp = json.load(js_addfile)
        temp = data["Justice League Members"]
    jl_memb_data["Member"] = input('Input JL Member #: ')
    jl_memb_data["Name"] = input("Enter JL Members Name: ")
    jl_memb_data["Real_Name"] = input("Enter JL Members Biological Name: ")
    jl_memb_data["Gender"] = input("Enter JL Members Gender (ex. Male, Female, N\A): ")
    jl_memb_data["Home_World"] = input("Enter JL Members Home World (Birthplace of Origin): ")
    jl_memb_data["Mother"] = input("Enter JL Members Mother: ")
    jl_memb_data["Father"] = input("Enter JL Members Father: ")
    jl_memb_data["Height"] = (input("Enter JL Members Height: "))
    jl_memb_data["Super_Suit_Color_1"] = input("Enter JL Members Super Suit Color 1 (Any Color or N/A): ")
    jl_memb_data["Super_Suit_Color_2"] = input("Enter JL Members Super Suit Color 2 (Any Coloror N/A): ")
    jl_memb_data["Super_Suit_Color_3"] = input("Enter JL Members Super Suit Color 3 (Any Coloror N/A): ")
    jl_memb_data["Super_Suit_Color_4"] = input("Enter JL Members Super Suit Color 4 (Any Coloror N/A): ")
    jl_memb_data["Skin_Color"] = input("Enter JL Members Skin Color: ")
    jl_memb_data["Eye_Color"] = input("Enter JL Members Eye Color: ")
    jl_memb_data["Hair_Color"] = input("Enter JL Members Hair Color: ")
    jl_memb_data["Powers"] = input("Enter JL Members Powers (Breif Description): ")
    jl_memb_data["Weapons"] = input("Enter JL Members Weapons (Breif Description): ")
    temp.append(jl_memb_data)
    with open (jl_data, "w") as js_addfile:
        json.dump(temp, js_addfile, indent=4)
    write_json(data)
#-----------------------------------------------------------
#DELETE FUNCTION
def delete_jl():
    printJL()
    new_jldata =[]
    with open (jl_data, 'r') as del_file:
        temp = json.load(del_file)
        database_legnth = len(temp)-1
    print("What JL Member Data index would you like to delete ")
    delete_ind = input(f"Select a Number 0-{database_legnth}>>>")
    i=0
    for userent in temp:
        if i ==int(delete_ind):
            pass
            i=i+1
        else:
            new_jldata.append(userent)
            i=i+1
    with open (jl_data, "w") as del_data:
        json.dump(new_jldata, del_data, indent=4)
#-----------------------------------------------------------
#EDIT JL MEMBER INFO

#-----------------------------------------------------------
#PRINT ORGANIZED
def printJL():
    with open (jl_data, 'r') as jl_file:
        data = json.load(jl_file)
        name_data = (data["Justice League Members"])
        for i in name_data:
            Member = (i["Member"])
            Name = (i["Name"])
            Real_Name = (i["Real Name"])
            Gender = (i["Gender"])
            Home_World = (i["Home World"])
            Mother = (i["Mother"])
            Father = (i["Father"])
            Height = (i["Height"])
            Super_Suit_Color_1 = (i["Super Suit Color 1"])
            Super_Suit_Color_2 = (i["Super Suit Color 2"])
            Super_Suit_Color_3 = (i["Super Suit Color 3"])
            Super_Suit_Color_4 = (i["Super Suit Color 4"])
            Skin_Color = (i["Skin Color"])
            Eye_Color = (i["Eye Color"])
            Hair_Color = (i['Hair Color'])
            Powers = (i['Powers'])
            Weapons = (i["Weapons"])
            print(f"""Member: {Member} \nName: {Name} \nReal Name: {Real_Name} \nGender: {Gender} \nHome World: {Home_World} \nMother: {Mother} \nFather: {Father} \nHeight: {Height} \nSuper_Suit_Color_1: {Super_Suit_Color_1} \nSuper_Suit_Color_2: {Super_Suit_Color_2} \nSuper_Suit_Color_3: {Super_Suit_Color_3} \nSuper_Suit_Color_4: {Super_Suit_Color_4} \nSkin_Color: {Skin_Color} \nEye_Color: {Eye_Color} \nHair_Color: {Hair_Color} \nPowers: {Powers} \nWeapons: {Weapons} \n""")
#-----------------------------------------------------------
#OPTIONS MENU
while True:
        choice = int(input("[1] Print Data\n[2] Update JL Memeber Info\n[3] Add New JL Member Info\n[4] Erase JL Member Data\n[5] Create copy of JL Members Data\n[6] Exit JL Database\n>>> "))
        if choice == 1:
            printJL()              
        elif choice == 2:
            printJL()
        elif choice == 3:
            add_jl(data)
        elif choice == 4:
            delete_jl()
        elif choice == 5:
            write_json(data, filename= "JusticeLeagueDatabaseV2.json")
        elif choice == 6:
            exit()
#-----------------------------------------------------------                
#THIS VERSION OF THE MAIN PROGRAM IS JSUT A TEST PLACE FOR THE FINAL PRODUCT USING A KEY 
#THE FILE NAMED application.py IS THE THE FULLY FINISHED FUNCTIONING CODE WITHOUT THE USE OF A KEY
