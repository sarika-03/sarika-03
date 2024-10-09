print("\n..........WELCOME TO SARIKA TOUR AND TRAVEL AGENCY..........")
print("\n..........सारिका टूर एंड ट्रैवल एजेंसी में आपका स्वागत है...........")

def view_packages():
    print("\nALL AVAILABLE PACKAGES ARE : ")
    package = [
        {"Destination": "Maldives", "Prices": 80000, "Days": "5 days", "Slots":6},
        {"Destination": "Bali", "Prices": 75000, "Days": "5 days", "Slots":4},
        {"Destination": "Tokyo", "Prices": 60000, "Days": "4 days", "Slots":5},
        {"Destination": "Paris", "Prices": 64000, "Days": "6 days", "Slots":13},
        {"Destination": "Thailand", "Prices": 55000, "Days": "6 days", "Slots":14},
        {"Destination": "London", "Prices": 60000, "Days": "7 days", "Slots":9}
    ]
    
    for pkg in package:
        print(pkg)
      
dict1={"Destination": "Maldives", "Prices": 80000, "Days": "5 days", "Slots":6}
dict2={"Destination": "Bali", "Prices": 75000, "Days": "5 days", "Slots":4}
dict3={"Destination": "Tokyo", "Prices": 60000, "Days": "4 days", "Slots":5}
dict4={"Destination": "Paris", "Prices": 64000, "Days": "6 days", "Slots":13}
dict5={"Destination": "Thailand", "Prices": 55000, "Days": "6 days", "Slots":14}
dict6={"Destination": "London", "Prices": 60000, "Days": "7 days", "Slots":9}

maldives_traveller_list = []
bali_traveller_list = []
tokyo_traveller_list = []
paris_traveller_list = []
thailand_traveller_list = []
london_traveller_list = []

def view_booking():
    print("\nwhich tour booking do you want to view")
    print("\n1. Maldives\n2. Bali\n3. Tokyo\n4. Paris\n5. Thailand\n6. London")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        print(maldives_traveller_list)
        print("\nNow available slots are only", dict1["Slots"])
    elif choice == 2:
        print(bali_traveller_list)
        print("\nNow available slots are only", dict2["Slots"])
    elif choice == 3:
        print(tokyo_traveller_list)
        print("\nNow available slots are only", dict3["Slots"])
    elif choice == 4:
        print(paris_traveller_list)
        print("\nNow available slots are only", dict4["Slots"])
    elif choice == 5:
        print(thailand_traveller_list)
        print("\nNow available slots are only", dict5["Slots"])
    elif choice == 6:
        print(london_traveller_list)
        print("\nNow available slots are only", dict6["Slots"])
    else:
        print("\nInvalid selection.")
        
def tour_book():
    view_packages()
    choice=int(input("\nenter your choice from 1 to  6 "))
    if(choice==1):
        dict1={"Destination": "Maldives", "Prices": 80000, "Days": "5 days", "Slots":6}
        print(dict1)
        if(dict1["Slots"]>0):
            print("\nyes slots are avilable for booking")
            seat=int(input("\nenter for slot booking"))
            if(seat>dict1["Slots"]):
                print("\nsorry ! Not available")
            else:
                for i in range(seat):
                    name=input("\nenter member name : ")
                    age=int(input("\nenter age of member : "))
                    passport_number=int(input("\nenter your passport number : "))
                    traveller={
                    "name":name,
                    "age":age,
                    "passport_number":passport_number
                    }
                    maldives_traveller_list.append(traveller)
                    dict1["Slots"]-=seat
                    
    elif(choice==2):
        dict2={"Destination": "Bali", "Prices": 75000, "Days": "5 days", "Slots":4}
        print(dict2)
        if(dict2["Slots"]>0):
            print("\nyes slots are avilable for booking")
            seat=int(input("\nenter for slot booking"))
            if(seat>dict2["Slots"]):
                print("\nsorry ! Not available")
            else:
                for i in range(seat):
                    name=input("\nenter member name : ")
                    age=int(input("\nenter age of member : "))
                    passport_number=int(input("\nenter your passport number : "))
                    traveller={
                        "name":name,
                        "age":age,
                        "passport_number":passport_number
                        
                    }
                    bali_traveller_list.append(traveller)
                dict2["Slots"]-=seat
                
            
    elif(choice==3):
        dict3={"Destination": "Tokyo", "Prices": 60000, "Days": "4 days", "Slots":5}
        print(dict3)
        if(dict3["Slots"]>0):
            print("\nyes slots are avilable for booking")
            seat=int(input("\nenter for slot booking"))
            if(seat>dict3["Slots"]):
                print("\nsorry ! Not available")
            else:
                for i in range(seat):
                    name=input("\nenter member name : ")
                    age=int(input("\nenter age of member : "))
                    passport_number=int(input("\nenter your passport number : "))
                    traveller={
                        "name":name,
                        "age":age,
                        "passport_number":passport_number
                        }
                    tokyo_traveller_list.append(traveller)
                dict3["Slots"]-=seat
                
               
    elif(choice==4):
        dict4={"Destination": "Paris", "Prices": 64000, "Days": "6 days", "Slots":13}
        print(dict4)
        if(dict4["Slots"]>0):
            print("\nyes slots are avilable for booking")
            seat=int(input("\nenter for slot booking"))
            if(seat>dict4["Slots"]):
                print("\nsorry ! Not available")
            else:
                for i in range(seat):
                    name=input("\nenter member name : ")
                    age=int(input("\nenter age of member : "))
                    passport_number=int(input("\nenter your passport number : "))
                    traveller={
                        "name":name,
                        "age":age,
                        "passport_number":passport_number
                        }
                    paris_traveller_list.append(traveller)
                dict4["Slots"]-=seat
                
                
    elif(choice==5):
        dict5={"Destination": "Thailand", "Prices": 55000, "Days": "6 days", "Slots":14}
        print(dict5)
        if(dict5["Slots"]>0):
            print("\nyes slots are avilable for booking")
            seat=int(input("\nenter for slot booking"))
            if(seat>dict5["Slots"]):
                print("\nsorry ! Not available")
            else:
                for i in range(seat):
                    name=input("\nenter member name : ")
                    age=int(input("\nenter age of member : "))
                    passport_number=int(input("\nenter your passport number : "))
                    traveller={
                        "name":name,
                        "age":age,
                        "passport_number":passport_number
                    }
                    thailand_traveller_list.append(traveller)
                dict5["Slots"]-=seat
                
               
    elif(choice==6):
        dict6={"Destination": "London", "Prices": 60000, "Days": "7 days", "Slots":9}
        print(dict6)
        if(dict6["Slots"]>0):
            print("\nyes slots are avilable for booking")
            seat=int(input("\nenter for slot booking"))
            if(seat>dict6["Slots"]):
                print("\nsorry ! No slots are available")
            else:
                for i in range(seat):
                    name=input("\nenter member name : ")
                    age=int(input("\nenter age of member : "))
                    passport_number=int(input("\nenter your passport number : "))
                    traveller={
                        "name":name,
                        "age":age,
                        "passport_number":passport_number
                        }
                    london_traveller_list.append(traveller)
                dict6["Slots"]-=seat

    else:
        print("wrong selection")

      
def cancel_booking():
    destination = input("\nEnter destination you want to cancel: ")

    if destination == dict1["Destination"]:
        travellers = maldives_traveller_list
        slots_dict = dict1
    elif destination == dict2["Destination"]:
        travellers = bali_traveller_list
        slots_dict = dict2
    elif destination == dict3["Destination"]:
        travellers = tokyo_traveller_list
        slots_dict = dict3
    elif destination == dict4["Destination"]:
        travellers = paris_traveller_list
        slots_dict = dict4
    elif destination == dict5["Destination"]:
        travellers = thailand_traveller_list
        slots_dict = dict5
    elif destination == dict6["Destination"]:
        travellers = london_traveller_list
        slots_dict = dict6
    else:
        print("\nYou selected the wrong destination")
        return
    
    print(travellers)  
    name = input("\nWhich traveller's booking do you want to cancel? Enter the name: ")

    for traveller in travellers:
        if traveller["name"] == name:
            travellers.remove(traveller)
            print("Booking cancelled for", traveller["name"])
            slots_dict["Slots"] += 1  
            break
    else:
        print("\nThe entered name is not booked.")
            
print("\nSELECT YOUR CHOICE")
while True:
    print("\n1. View  Available Packages")
    print("\n2. Tour Booking")
    print("\n3. View Booking")
    print("\n4. Cancel Booking")
   
    choice=int(input("\nenter your choice....... : "))
    
    if(choice==1):
        view_packages()
    elif(choice==2):
        tour_book()
    elif(choice==3):
        view_booking()
    elif(choice==4):
        cancel_booking()
    else:
        print("\nwrong choice")







        
