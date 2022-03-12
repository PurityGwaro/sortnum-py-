#Name: 
#Programming Assignment #5. 
#A Python program that displays the highest and lowest value in a given tuple
#when run,the program loops throught the tuple provided to find the minimum and maximum values and produces an ouput of these two values


#variable declaration
my_tuple= (701, -487, 8159, 1659, 9065, 6528, 3949, 7467, 3912, 7260, 7641, 8825, 5063, 9173, 352, 9855, 7047, 5648, 135, 213, 5224, 8741, 4864, 7295, 8646, 2915, 4400, 7487, 6394, 5883, 1244, -522, 796, 6546, 8226, 9474, 9540, 2010, 3472, 4210, 8748, 3043, 3660, 1426, 5328, 7446, 1031, -589, 7724, 8924, )

def sort_through(tuple):  #function to find the maximum and minimum value

    min = tuple[0]
    max = tuple[0]

    for value in tuple:  #loop through the tuple and select max and min values
        if value < min:
            min = value           
        elif value > max:
            max = value
    return max, min  #return a tuple with max and min 

result = sort_through(my_tuple)  #store the returned tuple in a temporary variable

#printing the max and min values
print("The maximum value is: ",result[0])
print("The minimum value is: ",result[1])