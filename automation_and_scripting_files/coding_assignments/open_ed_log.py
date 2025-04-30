# simple open, read, and print example

with open('Journal.2025-02-02T211249.01.log', 'r') as file:
    content = file.read()
    print(content)