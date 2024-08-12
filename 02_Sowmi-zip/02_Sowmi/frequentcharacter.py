counter = 0
def most_frequent_character(s):
    # Remove spaces 
    s = s.replace(" ", "").lower()
    
    # Create a Counter object                                       
    char_count = counter(s)
    
    # Find the most common character and its frequency
    most_common_char, most_common_count = char_count.most_common(1)[0]
    
    return most_common_char, most_common_count

input_string = "Guvi Geeks"
char, count = most_frequent_character(input_string)

print(f"Most frequent character: '{char}' with frequency: {count}")