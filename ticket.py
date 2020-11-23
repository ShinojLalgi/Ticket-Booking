name = []
seat_num = []
ask_name = ""
ask_seat = ""
while True:
    ask_name = input("Please enter your name: ")
    if ask_name == 'exit':
        print("Thank you for using our services.")
        break
    
    ask_seat = input("Please enter your seat number: ")
    if ask_seat == 'exit':
        print("Thank you for using our services.")
        break
    
    if ask_name not in name and ask_seat not in seat_num:
        name.append(ask_name)
        seat_num.append(int(ask_seat))
        print(f"{ask_name.title()} your seat number is {int(ask_seat)}.")
    else:
            if ask_seat in seat_num:
                print(f"Sorry {ask_name.title()} your desired seat is already booked")
            else:
                print(f"Sorry {ask_name.title()} you have already booked a seat")
