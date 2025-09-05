# Write a program to open the file in read mode and print each line, stripping any leading or trailing whitespace.
with open("example.txt") as fd:
    for line in fd:
        print(line.strip())

# Create a file named output.txt and write the text "Python is fun!" into it. Close the file and reopen it to verify its content.
with open("output.txt", "w") as fd_write:
    fd_write.write("Python is fun!")


with open("output.txt") as fd_read:
    print(fd_read.read())

# Open the file notes.txt in append mode and add the text "Remember to review file handling in Python!" as a new line at the end. If the file does not exist, create it.
with open("notes.txt", "a") as fd:
    fd.write("Remember to review file handling in Python!\n")

# Write a program to open the file story.txt, read its content, and count the total number of words in the file. Display the count to the user.
with open("story.txt") as fd:
    words = fd.read().split()
    print(f"Total words: {len(words)}")

# Write a program to copy the content of source.txt into destination.txt. If the destination file already exists, overwrite its content.
with open("source.txt") as fd:
    with open("destination.txt", "w") as fd1:
        fd1.write(fd.read())

# Write a program to remove all blank lines from data.txt and save the cleaned content to cleaned_data.txt.
with open("data.txt") as fd:
    with open("cleaned_data.txt", "a") as fd1:
        for line in fd:
            if line.strip():
                fd1.write(line)

# Write a program to copy the content of a binary file image.jpg into a new file copy_image.jpg. Ensure that the copied file is identical to the original.
with open("image.jpg", "rb") as fd, open("copy_image.jpg", "wb") as fd1:
    fd1.write(fd.read())

# Write a program to analyze a log file log.txt and generate a report of the total number of occurrences for each log level (INFO, WARNING, ERROR) in a new file summary.txt.
with open("log.txt") as fd, open("summary.txt", "w") as fd1:
    content = fd.read()
    info_count = content.count("INFO")
    warning_count = content.count("WARNING")
    error_count = content.count("ERROR")
    fd1.write(f"INFO: {info_count}\nWARNING: {warning_count}\nERROR: {error_count}")

# Create a new text file named relative_output.txt in a folder called relative_files (located relative to your script's directory). Write "This is a file created using a relative path." into the file.
import os

if not os.path.exists("relative_files"):
    os.makedirs("relative_files")

with open("relative_files/relative_output.txt", "w") as fd:
    fd.write("This is a file created using a relative path.")

# Open the file example_data.txt located in the data_files folder (relative to the script directory). Print its content to the console.
import os

os.makedirs("data_files", exist_ok=True)
file_path = os.path.join("data_files", "example_data.txt")

if not os.path.exists(file_path):
    with open(file_path, "w") as f:
        f.write("This is example data.")

with open("data_files/example_data.txt") as fd:
    print(fd.read())

# Write a program to determine and print the absolute path of the file settings.json, which is located in the config folder relative to the script directory.
import os
relative_path = os.path.join("config", "settings.json")
print(os.path.abspath(relative_path))

# Write a program to create a new file named exclusive_file.txt using the x mode and write the text "This file is created using x mode." into it. Ensure the program handles errors gracefully if the file already exists.
try:
    with open("exclusive_file.txt", "x") as file:
        file.write("This file is created using x mode.")
except FileExistsError:
    print("Error: File exclusive_file.txt already exists.")

# Write a program that prompts the user to input a file name. Create a new file with that name using x mode and write "File <filename> created successfully." into it. If the file already exists, notify the user.
file_name = input("Enter file name: ")

try:
    with open(file_name, "x") as file:
        file.write(f"File {file_name} created successfully.")
except FileExistsError:
    print(f"Error: File {file_name}t already exists.")