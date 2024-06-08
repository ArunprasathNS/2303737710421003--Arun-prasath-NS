def remove_duplicates(arr):
    unique_elements = []
    for num in arr:
        if num not in unique_elements:
            unique_elements.append(num)
    return unique_elements


    size = int(input("Enter the array size: "))
    elements = list(map(int, input(f"Input {size} elements in an array separated by space: ").split()))
    

    unique_elements = remove_duplicates(elements)
    

    print("The unique elements found in the array are:")
    for num in unique_elements:
        print(num, end=" ")

