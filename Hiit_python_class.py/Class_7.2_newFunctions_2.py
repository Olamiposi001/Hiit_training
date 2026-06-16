from Class_7_newFunctions import get_radius, squared_radius, multiply_by_pi
import numpy as np

numbers = [2, 3, 4, 5]
average = np.mean(numbers)
print(f"The average of the numbers is: {average}")
def calculate_area(d):
    
    r = get_radius(d)
    
    r_squared = squared_radius(r)
    
    final_area = multiply_by_pi(r_squared)
    
    return final_area

result = calculate_area(10)
print(f"The area of the circle is: {result}")