print(" *** Finding circle area *** ")
diameter = input("Enter diameter : ")
diameter = float(diameter)/2
pi = 3.1415926538
circleArea = float(pi*(diameter**2))
print("Circle area =", circleArea)
print("Circle area = %.2f" %circleArea) # แสดงผลทศนิยม 2 ตำแหน่ง
print("whole number =>",int(circleArea)) # แสดงผลเฉพาะส่วนที่เป็นจำนวนเต็ม