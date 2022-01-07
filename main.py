# Write a program to find the quadrant of a given point
x=int(input())
y=int(input())
if(x>0 and y>0):
  print("FIRST quadrant")
if(x<0 and y>0):
  print("SECOND quadrant")
if(x<0 and y<0):
  print("THIRD quadrant")
if(x>0 and y<0):
  print("FOURTH quadrant")
