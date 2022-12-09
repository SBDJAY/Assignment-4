#-----------------------------------------------------------
# Assignment 4
#CRUD Applications with Collections and Persistence
# Daniel Pius
# Muhammad Asif
# Class: 1229_4013: Programming Principles
# December 12, 2022
#-----------------------------------------------------------
#IMPORTS
import json
#-----------------------------------------------------------
#JSON
jl_data = 'JusticeLeagueDatabase.json'
#-----------------------------------------------------------
#CREATE COPY of JL DATA (EXTRA FUNCTION LIKELY TO BREAK PROGRAM)
def write_json(data, filename= "JusticeLeagueDatabase.json"):
    with open(filename, "w") as f:
        json.dump(data, f, indent=4)

with open (jl_data, 'r') as jl_file:
    data = json.load(jl_file)
    write_json(data)
    temp = data
    temp.append("Copy")
#-----------------------------------------------------------
#ADD DATA (ADD JL MEMBER)
def add_jl():
    jl_memb_data = {}
    with open (jl_data, "r") as js_addfile:
        temp = json.load(js_addfile)
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
#-----------------------------------------------------------
#DELETE FUNCTION (DELETE JL MEMBER), (USE 4 WHEN TESTING OUT FEATURE TO NOT REMOVE DATA THAT HAS WRITING IN IT)
def delete_jl():
    printJL()
    new_jldata =[]
    with open (jl_data, 'r') as del_file:
        temp = json.load(del_file)
        database_legnth = len(temp)-1
    print("What JL Member Data index would you like to delete ")
    delete_ind = input(f"Select a JL Member 0-{database_legnth}>>>")# 0 = Member 1
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
#UPDATE JL MEMBER INFO (Update JL MEMBER INFO BY INDEX)
def update_jl():
    new_jldata =[]
    with open (jl_data, 'r') as upd_file:
        temp = json.load(upd_file)
        database_legnth = len(temp)-1
    print("What JL Member Data index would you like to update ")
    update_ind = input(f"Select a JL Member 0-{database_legnth}>>>")# 0 = Member 1
    i=0
    for userent in temp:
        if i ==int(update_ind):
            Member = i["Member"]
            Name = i["Name"]
            Real_Name = i["Real Name"]
            Gender = i["Gender"]
            Home_World = i["Home World"]
            Mother = i["Mother"]
            Father = i["Father"]
            Height = i["Height"]
            Super_Suit_Color_1 = i["Super Suit Color 1"]
            Super_Suit_Color_2 = i["Super Suit Color 2"]
            Super_Suit_Color_3 = i["Super Suit Color 3"]
            Super_Suit_Color_4 = i["Super Suit Color 4"]
            Skin_Color = i["Skin Color"]
            Eye_Color = i["Eye Color"]
            Hair_Color = i['Hair Color']
            Powers = i['Powers']
            Weapons = i["Weapons"]

            Member = input('Input JL Member #: ')
            Name = input("Enter JL Members Name: ")
            Real_Name = input("Enter JL Members Biological Name: ")
            Gender = input("Enter JL Members Gender (ex. Male, Female, N\A): ")
            Home_World = input("Enter JL Members Home World (Birthplace of Origin): ")
            Mother = input("Enter JL Members Mother: ")
            Father = input("Enter JL Members Father: ")
            Height = input("Enter JL Members Height: ")
            Super_Suit_Color_1 = input("Enter JL Members Super Suit Color 1 (Any Color or N/A): ")
            Super_Suit_Color_2 = input("Enter JL Members Super Suit Color 2 (Any Coloror N/A): ")
            Super_Suit_Color_3 = input("Enter JL Members Super Suit Color 3 (Any Coloror N/A): ")
            Super_Suit_Color_4 = input("Enter JL Members Super Suit Color 4 (Any Coloror N/A): ")
            Skin_Color = input("Enter JL Members Skin Color: ")
            Eye_Color = input("Enter JL Members Eye Color: ")
            Hair_Color = input("Enter JL Members Hair Color: ")
            Powers = input("Enter JL Members Powers (Breif Description): ")
            Weapons = input("Enter JL Members Weapons (Breif Description): ")
            new_jldata.append({"Member": Member, "Name": Name, "Real Name": Real_Name, "Gender": Gender, 
            "Home World": Home_World,"Mother": Mother,"Father": Father,"Height": Height,"Super Suit Color 1": Super_Suit_Color_1, "Super Suit Color 2": Super_Suit_Color_2, 
            "Super Suit Color 3": Super_Suit_Color_3, "Super Suit Color 4": Super_Suit_Color_4,"Skin Color": Skin_Color, "Eye Color": Eye_Color, 
            "Hair Color": Hair_Color,"Powers": Powers, "Weapons": Weapons})
            i=i+1
        else:
            new_jldata.append(userent)
            i=i+1
    with open (jl_data, "w") as upd_data:
        json.dump(new_jldata, upd_data, indent=4)
#-----------------------------------------------------------
#PRINT ORGANIZED
def printJL():
    with open (jl_data, 'r') as jl_file:
        data = json.load(jl_file)
        for i in data:
            Member = i["Member"]
            Name = i["Name"]
            Real_Name = i["Real Name"]
            Gender = i["Gender"]
            Home_World = i["Home World"]
            Mother = i["Mother"]
            Father = i["Father"]
            Height = i["Height"]
            Super_Suit_Color_1 = i["Super Suit Color 1"]
            Super_Suit_Color_2 = i["Super Suit Color 2"]
            Super_Suit_Color_3 = i["Super Suit Color 3"]
            Super_Suit_Color_4 = i["Super Suit Color 4"]
            Skin_Color = i["Skin Color"]
            Eye_Color = i["Eye Color"]
            Hair_Color = i['Hair Color']
            Powers = i['Powers']
            Weapons = i["Weapons"]
            print(f"""Member: {Member} \nName: {Name} \nReal Name: {Real_Name} \nGender: {Gender} \nHome World: {Home_World} \nMother: {Mother} \nFather: {Father} \nHeight: {Height} \nSuper_Suit_Color_1: {Super_Suit_Color_1} \nSuper_Suit_Color_2: {Super_Suit_Color_2} \nSuper_Suit_Color_3: {Super_Suit_Color_3} \nSuper_Suit_Color_4: {Super_Suit_Color_4} \nSkin_Color: {Skin_Color} \nEye_Color: {Eye_Color} \nHair_Color: {Hair_Color} \nPowers: {Powers} \nWeapons: {Weapons} \n""")
#-----------------------------------------------------------
#OPTIONS MENU
while True:
        choice = int(input("[1] Print Data\n[2] Update JL Memeber Info\n[3] Add New JL Member Info\n[4] Erase JL Member Data\n[5] Create copy of JL Members Data\n[6] Exit JL Database\n>>> "))
        if choice == 1:
            printJL()#PRINT ORGANIZED              
        elif choice == 2:
            update_jl()#UPDATE JL MEMBER INFO
        elif choice == 3:
            add_jl()#ADD DATA
        elif choice == 4:
            delete_jl()#DELETE FUNCTION
        elif choice == 5:
            write_json(data, filename= "JusticeLeagueDatabase.json")#CREATE COPY of JL DATA
        elif choice == 6:
            exit()
        else:
            print("PLEASE SELECT A CORRECT DISPLAYED OPTION")
#-----------------------------------------------------------                
#THIS IS THE FUNCTIONING CODE THAT DOES NOT USE KEYS