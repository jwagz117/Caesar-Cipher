# Jack Wagner
# 3/20/2020
# Program to crack a Caesar Shift Cipher

from nltk.corpus import words

# Store input encoded message from user
code = input("What is your encoded message?     ")


# Function to split a word into a list of characters
def split(word):
    return [char for char in word]


# Split input message and make a list of lists
split_code = code.split(" ")
res = []

for part in split_code:
    # Each small list is the character list of just one word
    res.append(split(part.lower()))

out_file = open("testPoss.txt", "w")

# Iterate over all possible 26 shifts
for i in range(1, 26):
    for word in res:
        for letter in word:
            # Make new ord for the shifted letter
            new_ord = ord(str(letter)) - i
            if new_ord < 97:
                # Wrap around if the ord goes below "a"
                new_ord = 123 - (97 - new_ord)
            # Write the new shifted character
            out_file.write(str(chr(new_ord)))
        # Write a space between each word
        out_file.write(" ")
    # Break to a new line after each of 26 shifts
    out_file.write("\n")

out_file.close()

# Re-open the file to see if the shifted words are real words
file = open("testPoss.txt", "r")

max_score = 0
max_line = None
count = 0
for curr_line in file:
    curr_score = 0
    word_list = curr_line.split(" ")
    for word in word_list:
        # Increase score for each word that is real
        if str(word) in words.words():
            curr_score += 1
    # Continuously update the max line
    count += 1
    print(str(count) + ": " + str(curr_score))
    if curr_score > max_score:
        max_score = curr_score
        max_line = curr_line

print("Decoded Message: " + str(max_line))

file.close()

