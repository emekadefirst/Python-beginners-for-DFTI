import sys
import random as r

list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
r.shuffle(list)

for x in list:
    for y in list:
        # # print(f"{x} - {x}")
        result = f"{x} - {y}"
        # print(result)          
      
max_booking = 20
initial_booking = 0

num_booking = int(input("Enter the number of booking\n>> "))
if num_booking > max_booking:
    print("Number of booking exceeds the maximum limit.\n>> ")
    num_booking = max_booking
    sys.exit()
   

while initial_booking <= num_booking:
    
    # booking_count = initial_booking + 1
    predicts = str(input("Enter Home & Away teams score\n>> "))

    if predicts == result:
        print(result)
        print(predicts)
        print("You win!!!")
    else:
        print(result)
        print("You loose")   
    initial_booking += 1
# print(result)
 
print("All bookings completed.")