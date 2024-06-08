def string_length(s):
    return len(s)
def string_copy(s):
    return s
def string_concatenate(s1, s2):
    return s1 + s2
def string_to_uppercase(s):
    return s.upper()


first_string = input("Enter the first string: ")
second_string = input("Enter the second string: ")
print("Length of first string:", string_length(first_string))
print("Length of second string:", string_length(second_string))
print("Copy of first string:", string_copy(first_string))
print("Concatenation of both strings:", string_concatenate(first_string, second_string))
print("Uppercase of first string:", string_to_uppercase(first_string))

