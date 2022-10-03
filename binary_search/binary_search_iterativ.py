# Binary Search Interative.
    # 1. Read input and sort.
    # 2. Loop for binary search.

# 1. Read input and sort.
length = int(input("Enter list length: "))
int_list = []
# Read element of list.
for i in range(length):
    element = int(input("Enter element: "))
    int_list.append(element)
# Sort the list.
int_list = sorted(int_list)
print("Your list is: " + str(int_list))
# Read target element to be found.
target = int(input("Enter target element: "))

# 2. Loop for binary search.
# Define variables.
start = 0
end = length-1
position = -1  # If position remains unchanged at -1, element not present.
                # If position is updated, then position+1 is printed.

while(start <= end):
    mid = (start + end) // 2
    if int_list[mid] == target:
        position = mid
        break
    # If not, check if lesser than mid element.
    # Change range from start to mid-1, since less than mid.
    elif target < int_list[mid]:
        end = mid-1
    # Check if greater than mid element.
    # Change range from mid+1 to end, since greater than mid.
    elif target > int_list[mid]:
        start = mid+1

if position == -1:
    print("Element is not in the list.")
else:
    print("Element is found at position: " + str(position+1))


    