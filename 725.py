def sort_string(input_str):
    sorted_string1 = ''.join(sorted(input_str))
    return sorted_string1


input_str = input("Enter the input string: ")
print("The output string:", sort_string(input_str))

