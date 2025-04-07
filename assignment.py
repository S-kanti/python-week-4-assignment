def read_and_write_file():
    try:
        input_file = input("Enter file/'s name:")
        with open(input_file,'r') as file:
            content = file.read()

            #modifiction options for yuser to chose
            print("Choose an option:")
            print("1. Add line numbers")
            print("2. Convert all text to uppercase")
            print("3. Reverse the content of each line")
            choice = input("Enter your choice:")

            # elif statements to check the user's choice
            if choice == '1':
                modified_content = [f"{i + 1}: {line}" for i, line in enumerate(content)]
            elif choice == "2":
                modified_content = [line.upper() for line in content]
            elif choice == "3":
                modified_content = [line[::-1] for line in content]
            else:
                print("Invalid choice. No modifications will be made.")
                modified_content = content
            # Write the modified content to a new file
        output_file = "modified_" + input_file
        with open(output_file, 'w') as file:
            file.writelines(modified_content)
        
        print(f"Modified content has been written to {output_file}")
    
    except FileNotFoundError:
        print("Error: The file does not exist.")
    except IOError:
        print("Error: The file could not be read or written.")

# Run the function
if __name__ == "__main__":
    read_and_write_file()