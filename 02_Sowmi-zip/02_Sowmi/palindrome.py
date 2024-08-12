def is_palindrome(input_string):
    
    cleaned_string = ''.join(input_string.split()).lower()
    
    
    return cleaned_string == cleaned_string[::-1]


input_str = input("Enter a string: ")
if is_palindrome(input_str):
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")
