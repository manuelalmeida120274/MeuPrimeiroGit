file_name = input("Enter the name of the file to convert: ")

with open(file_name, 'rb') as file:
    content = file.read()

# Decode the content using ISO-8859-1 and re-encode it to UTF-8
content = content.decode('ISO-8859-1').encode('utf-8')

with open(file_name, 'wb') as file:
    file.write(content)

print(f"{file_name} has been converted to UTF-8 encoding.")