ipsum_file = open('files/ipsum.txt')

for line in ipsum_file:
    print(line.rstrip())

# reset the cursor to the beginning
ipsum_file.seek(0)

lines = ipsum_file.readlines()
print(lines)

# read from specific position
ipsum_file.seek(50)
file_text = ipsum_file.read(100)
print(file_text)

# close a file
ipsum_file.close()