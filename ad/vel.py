import re

# Assuming args is an object or variable that contains the threshold value
args = {
    "threshold": 5
}

# Example input string
input_string = "Hello, world! This is a sample sentence."

# Regular expression pattern to find words with more than the threshold number of characters
pattern = r"\b\w{6,}\b"  # Matches words with 6 or more characters

# Perform the pattern matching and length check
matches = re.finditer(pattern, input_string)
for match in matches:
    if len(match.group(0)) > args["threshold"]:
        print(f"Match found: {match.group(0)}")
