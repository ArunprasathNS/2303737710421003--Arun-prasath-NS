def insert_delete_array():
    size = int(input("Enter size: "))
    arr = list(map(int, input(f"Enter {size} elements: ").split()))

    print("Array elements:", *arr)

    while True:
        print("1. Insert a number")
        print("2. Delete a number")
        print("3. Exit")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            loc = int(input("Location: "))
            num = int(input("Number: "))
            if loc < 1 or loc > len(arr) + 1:
                print("Invalid location")
            else:
                arr.insert(loc - 1, num)
                print(f"{num} inserted at location {loc}")
                print("Array elements:", *arr)
        elif choice == 2:
            loc = int(input("Location: "))
            if loc < 1 or loc > len(arr):
                print("Invalid location")
            else:
                deleted = arr.pop(loc - 1)
                print(f"{deleted} deleted from location {loc}")
                print("Array elements:", *arr)
        else:
            break

insert_delete_array()

