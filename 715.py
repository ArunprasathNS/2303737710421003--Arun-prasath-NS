def strlen(s):
    return len(s)
def strcpy(s):
    return s
def strcat(s1, s2):
    return s2 + s1
def strstr(s, substring):
    return s.find(substring)
def strrchr(s, char):
    return s.rfind(char)

string1 = input("Enter a string: ")
print("Length of the string:", strlen(string1))
copied_string = strcpy(string1)
print("Copied string:", copied_string)
string2 = input("Enter second string to concatenate: ")
print("Concatenated string:", strcat(string1, string2))
substring = input("Enter a substring: ")
position = strstr(string1, substring)
if position != -1:
    print("Substring found at position", position)
else:
    print("Substring not found")
char = input("Enter a character: ")
last_occurrence = strrchr(string1, char)
if last_occurrence != -1:
    print("Last occurrence is at index", last_occurrence)
else:
    print("Character not found")

