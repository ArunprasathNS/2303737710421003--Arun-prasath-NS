def sort_array_ascending(arr):
    arr.sort()

try:
    size = int(input("Enter how many values you want to read: "))
    array = []
    for i in range(size):
        array.append(int(input(f"Enter the value of a[{i}]: ")))

    sort_array_ascending(array)
    print("Array sorted in ascending order =", ' '.join(map(str, array)))
except ValueError:
    print("Invalid input")

