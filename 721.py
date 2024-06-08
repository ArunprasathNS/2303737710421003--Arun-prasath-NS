def compare_strings(str1, str2):
    if str1 == str2:
        print(f"{str1} is equal to {str2}")
    else:
        print(f"{str1} is not equal to {str2}")
        if str1 < str2:
            print(f"{str1} is less than {str2}")
        else:
            print(f"{str1} is greater than {str2}")


str1 = input("Enter first string: ")
str2 = input("Enter second string: ")
compare_strings(str1, str2)

