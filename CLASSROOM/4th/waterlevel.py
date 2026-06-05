#A water tank is being filled with water at a constant rate of 10 liters per minute. Initially, the tank contains 0 liters of water. Write a program that displays the amount of water in the tank after each minute and continues until the tank reaches 100 liters. 
water_level=0
while water_level<=100:
    water_level+=10
    print("Water level: ",water_level,"liters")


print("The tank is full.")   