import numpy as np

n = int(input("Enter the number of values: "))
values = list(map(float, input("Enter values: ").split()))

m = np.mean(values)
v = np.var(values)
d = np.sqrt(variance)

print(f"Mean = ",m)
print(f"Variance = ",v)
print(f"Deviation = ",d)
