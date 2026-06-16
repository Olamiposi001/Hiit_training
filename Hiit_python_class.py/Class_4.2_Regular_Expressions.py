import re # or regex, it is a module that provides support for regular expressions in Python

text = "I work with python"

result = re.search("python", text) # search for the word "python" in the text
print(result.group()) # print the matched word


text = "I have 2 apples and 3 oranges"
result = re.search(r'\d', text) # search for the first digit in the text
print(result.group()) # print the matched digit

text = "I have 22 apples and 3 oranges"
result = re.findall(r'\d', text) # search for all digits in the text
print(result) # print the list of matched digits