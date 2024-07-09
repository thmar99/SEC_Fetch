import re

data = ['-123-xyz', '123_xyz', '-567-gaap', '7.38', '94.3*', '-1.3']

# Function to extract numeric characters along with leading characters
def extract_numeric_with_leading(string):
    match = re.search(r'[-+]?\d*\.?\d+', string)
    if match:
        return string[:match.end()]
    return ""

# Apply the function to each element in the list
modified_data = [extract_numeric_with_leading(item) for item in data]
print(modified_data)