def read_and_modify_file():
    try:
        filename = input("Enter the file name to read: ")

        with open(filename, "r") as file:
            content = file.read()

        modified_content = content.upper()

        new_filename = "modified_" + filename
        with open(new_filename, "w") as file:
            file.write(modified_content)

        print(f" Modified content written to '{new_filename}'")

    except FileNotFoundError:
        print(" Error: File not found. Please check the file name and try again.")
    except PermissionError:
        print(" Error: You don't have permission to read this file.")
    except Exception as e:
        print(f" An unexpected error occurred: {e}")

if __name__ == "__main__":
    read_and_modify_file()

