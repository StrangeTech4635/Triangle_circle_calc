"""
    Calculate the area, circumference, and perimeter
"""

import math

def circle(r:float):
    #Annotate variables
    r:float
    calculate_area_circle(r)
    calculate_circumference(r)

    area = calculate_area_circle(r)
    circumference = calculate_circumference(r)
    print("The area is '{:.2f}', and the circumference is '{:.2f}'.".format(area,circumference))



def triangle(length:float, width:float) -> float:
    length: float
    width: float
    calculate_area_triangle(length,width)
    calculate_perimeter(length,width)

    area = calculate_area_triangle(length,width)
    perimeter = calculate_perimeter(length,width)
    print("The area is '{:.2f}', and the perimeter is '{:.2f}'.".format(area, perimeter))
   


#calculate the area and circumference for the circle
def calculate_area_circle(radius:float)->float:
    #Annotate variables
    radius: float
    area_circle: float

    #calculate the area for the circle
    area_circle = math.pi*radius**2
    return area_circle


def calculate_circumference(radius:float)->float:
    #Annotate variables
    radius: float
    circumference:float

    #calculate the circumference
    circumference = 2*math.pi*radius
    return circumference
   



#Gather the area and perimeter for the triangle
   
def calculate_area_triangle(length:float,width:float)->float:
    #Annotate variables
    legnth:float
    width:float
    area_triangle: float

    #calculate the area for the triangle
   
    area_triangle = length * width
    return area_triangle

def calculate_perimeter(length:float,width:float)->float:
    #Annotate variables
    lenght:float
    width:float
    perimeter:float

    #Calculate the perimeter for the triangle
    perimeter = 2*(length + width)
    return perimeter


def main():
    #annotate variables
    user_input: str
    r: float
    length:float
    width:float

    user_input = input("Would you like to do Circle or Triangle: ")

    if user_input.lower() == "circle":
        #gather the radius from user for the circle
        r = float(input("Hi, can you give me a radius?: "))
        circle(r)
    elif user_input.lower() == "triangle": 
        #gather the length and width for the triangle
        length = float(input("May I please get the length?: "))
        width = float(input("And width please? "))
        triangle(length,width)
    else:
        print("I do not understand that")
        main()


   
main()