def rep(n, c, r):
    string = list(n)
    for index, char in enumerate(string):
        if char == c:
            string[index] = r
            break
    
    return ''.join(string)


n = input("Enter the string: ")
c = input()
r = input()
result = rep(n,c,r)
print(result)

