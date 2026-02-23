import time

numbers = list(range(1, 10000001))

target = 87877

# Linear search

start_time = time.time()

found = False
for i in numbers:
    if i == target:
        found = True 
        break

end_time = time.time()

linear_time = end_time - start_time
print("Linear Search Time: ", linear_time)
print("Element found at index: ", i)

if not found:
    print("Element not found!")

start_time = time.time()

low = 0
high = len(numbers) - 1
found = False

while low <= high:
    mid = (low+high) // 2

    if numbers[mid] == target:
        found = True
        break
    elif numbers[mid] < target:
        low = mid+1
    else:
        high = mid-1

end_time = time.time()
binary_time = end_time - start_time
print("Binary Search Time: ", binary_time)
print("Element found at index: ", i)
if not found:
    print("Element not found!")
    