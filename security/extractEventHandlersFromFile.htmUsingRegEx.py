import re

# Function to read the content of the HTML file
def read_html_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

# Path to the HTML file
file_path = 'file.htm'

# Read the HTML content from the file
html_content = read_html_file(file_path)

# Regex pattern to match any word starting with "on" preceded by ">" and followed by "<"
pattern = r'>.*?(on\w*).*?<'

# Find all matches in the HTML content
matches = re.findall(pattern, html_content)

# Print matches
# print(matches)
uniq = []
for match in matches:
    if len(match) > 4:
        if match not in uniq:
            uniq.append(match)
            # print(match)
for m in uniq:
    print(m)