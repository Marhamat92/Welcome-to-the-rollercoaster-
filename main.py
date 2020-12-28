print("Welcome to the rollercoaster")
height=int(input(" What is your height in cm? "))
bill=0

if height >= 120:
  print("You can ride rollercoaster")
  age=int(input("What is your age? "))
  if age <=12:
   bill=5
   print("child tickets are 5$")
  elif age <= 18:
   bill=7
   print("teen tickets are 7$") 
  elif age>= 45 and age<= 55:
    print("No worries, Have a free ride with us")
  else:
    bill=12
    print("Adult tickets are 12$")
  photo=input("do you want to take photo? Y or N ")
  if photo == "Y":
   bill += 3 
  print(f"your final bill is $ {bill}")

else:
  print("Sorry, you need to be taller to ride rollercoaster")
