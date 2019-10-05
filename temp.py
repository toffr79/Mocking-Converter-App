# temporary file with original funcitionality

# Prompt the user for a string to be converted
original_string = input("Please input a string you would like converted for mocking purposes: ")

# Create a list to hold the characters
char_list = []

# Split the string into a list of separate characters
for char in original_string:
    char_list.append(char)

print(char_list)

print(len(char_list))

# Create variable to iterate over while loop and a list for the converted chars
i = 0
converted_char_list = []

# Convert character case based on even/odd
while i <= (len(char_list) - 1):
    if (i == 0) or (i % 2 == 0):
        converted_char_list.append(char_list[i].lower())
    else:
        converted_char_list.append(char_list[i].upper())
    i+=1

# Create variable to hold the converted string
converted_string = ""
for char in converted_char_list:
    converted_string += char

print(converted_char_list)
print(converted_string)
