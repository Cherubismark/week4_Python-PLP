# Ask the user for the filename
input_filename = input("Enter the filename to read: ")
output_filename = "modified_" + input_filename  # Output file with a prefix 'modified_'

try:
    # Try to open the input file for reading
    with open(input_filename, "r") as file:
        # Read the content of the file
        content = file.read()
        
    # Modify the content (for example, converting the content to uppercase)
    modified_content = content.upper()
    
    # Write the modified content to a new file
    with open(output_filename, "w") as output_file:
        output_file.write(modified_content)
    
    print(f"File has been modified and saved as {output_filename}")
    
except FileNotFoundError:
    print(f"Error: The file '{input_filename}' was not found.")
except IOError:
    print(f"Error: Could not read the file '{input_filename}'.")
