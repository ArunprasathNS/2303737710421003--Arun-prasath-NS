def rem(n):
    c = ""
    for char in n:
        if char not in c:
            c += char
    return c

n = input("Enter the string: ")
r=rem(n)
print(r)

