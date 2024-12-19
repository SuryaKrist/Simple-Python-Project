umur = int(input("Enter your age :"))

if umur >= 0 and umur <= 2:
    categori = "Baby"
elif umur >= 3 and umur <= 12:
    categori = "Child"
elif umur >= 13 and umur <= 19:
    categori = "Teens"
elif umur >= 20 and umur <= 35:
    categori = "Adults"
elif umur >= 36 and umur <= 50:
    categori = "Middle-aged"
else:
    categori = "Elderly"

print("You are now in the age category :", categori)

