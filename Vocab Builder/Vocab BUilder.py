import re

# Open the input file and read its content
# Open the input file with utf-8 encoding
with open('input.txt', 'r', encoding='utf-8') as input_file:
    text = input_file.read()

# Use a regular expression to find all quoted words/phrases
quoted_words = re.findall(r'[“"](.*?)[”"]', text)

# Write the extracted words/phrases to a new file
vocab_list=[]
with open('output.txt', 'w') as output_file:
    for word in quoted_words:
        if word not in vocab_list:
            output_file.write(word + '\n')
            vocab_list.append(word)
        else:
            print(f"Skipping duplicate word: {word}")