def linearSearch(array, query):
    for index in range(0,len(array)):
         if grades[index] == query:
             return index
    return -1

grades = [3, 5, 12, 10, 4]

# Allowing the user to input the search value
search = int(input("Enter the value you want to search for: "))

result = linearSearch(grades,search)

if result == -1:
    print("Not Found")
else:
    print("Found")