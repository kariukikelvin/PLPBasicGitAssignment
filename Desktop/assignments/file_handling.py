file = open("my_file.txt", "w")

file.write("python is fun. \n")
file.write("This is line Number: 2. \n")
file.write("athe third line . \n")

print("File created and initial content written successfully.")

file = open("my_file.txt", "r")
content = file.read()
print(content)
file.close()

file = open("my_file.txt", "a")
file.write("appending the fourth line. \n")
file.write("the second number: 110. \n")
file.write("the last line to append. \n")
print("Additional content appended successfully.")

try:
    file = open("my_file.txt", "r")
    updated_content = file.read()
    print("\nUpdated file content:")
    print(updated_content)
except FileNotFoundError:
    print("Error: The file was not found.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
finally:
    print("\nFile handling script execution completed.")

