def count_words(s):
    # Split the string into words 
    words = s.split()
    
    return len(words)

input_string = "Guvi Geeks Network Private Limited"
number_of_words = count_words(input_string)

print(f"Number of words in the string: {number_of_words}")
