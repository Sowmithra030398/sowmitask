def count_unique_characters(input_string):
   
    unique_characters = set(input_string)
    
   
    return len(unique_characters)


input_str = input("Enter a string: ")
print("Number of unique characters:", count_unique_characters(input_str))