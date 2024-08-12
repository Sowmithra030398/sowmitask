def remove_vowels(input_string):
    vowels = "aeiouAEIOU"
   
    result = ''.join([char for char in input_string if char not in vowels])
    
    return result

input_str = input("Enter a string: ")
print("String with vowels removed:", remove_vowels(input_str))