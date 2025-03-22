import os

# Specify the path (use '.' for current directory)
path = '/'

# Get the list of files and directories
contents = os.listdir(path)

# Print the contents
print(f"Contents of directory '{path}':")
for item in contents:
    print(item)
