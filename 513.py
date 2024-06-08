n = int(input("Enter number of elements: "))
elements = []
for i in range(n):
    elements.append(int(input(f"Enter element {i+1}: ")))

l = max(elements)
s = min(elements)
print(f"Largest element: ",l)
print(f"Smallest element: ",s)


