def area (Length,Height ):
     Area = Length*Height
     return(Area)

def Surround(Length,Height):
     Perimeter = 2*(Length+Height)
     return(Perimeter)

while True:
    try:
        Height = int(input("Enter the height of the rectangle :"))
        Length = int(input("Enter the length of the rectangle :"))
    except ValueError:
     print("Enter the appropriate data type !")
    else:
    # Calculation and output only happen when valid input is received
     rectangle_area = area(Length, Height)
     rectangle_perimeter = Surround(Length, Height)
     print(f"Area of the rectangle: {rectangle_area}")
     print(f"Perimeter of the rectangle: {rectangle_perimeter}")
     break 







    
