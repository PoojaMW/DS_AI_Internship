filename = input("Enter the filename to open (e.g., config.txt): ")

try:
    with open(filename, "r") as file:
        print("\nFile contents:")
        print(file.read())

except FileNotFoundError:
    print("Oops! That file doesn't exist yet.")
