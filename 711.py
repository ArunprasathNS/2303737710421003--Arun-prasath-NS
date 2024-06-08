def coun(input_string):
    freq = {}
    
    for char in n:
        if char == ' ':
            continue
        
        if char in freq:
            freq[char] += 1
        else:
            freq[char] = 1
    
    for char, count in sorted(freq.items()):
        print(char, '=', count)


n = input("Enter the string: ")
coun(n)

