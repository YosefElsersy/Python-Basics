grades = [10, 5, 6, 20, 15, -3] # => [5 ,6, 10, 15, 20]
print(grades)
print("==================")
# bubble sort algoritm
# 1) Length for the array

length = len(grades)


#2) loop on elements in array
for index in range(0, length-1):
    for compare in range(0, length - index - 1):
        first = grades[compare]
        second = grades[compare + 1]
        if  first > second:
            grades[compare] = second
            grades[compare + 1] = first


print(grades)   