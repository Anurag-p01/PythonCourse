from pathlib import Path
import os

def readfileandfolder():
    try:
        path = input("Enter the folder path (leave empty for current folder): ").strip()
        if path == "":
            path = "."
        items = os.listdir(path)
        print("\nFiles and Folders:")
        for i, item in enumerate(items):
            print(f"{i+1} : {item}")
    except Exception as e:
        print(f"Error: {e}")


def createfile():
    try:
        name = input("Enter the name of the file to be created: ") 
        p = Path(name)
        if not p.exists():
            with open(p, 'w') as fs:
                data = input("What do you want to write in the file: ")
                fs.write(data)
            print("✅ File created successfully!")
        else:
            print("⚠️ File already exists.")    
    except Exception as e:
        print(f"An error occurred: {e}")


def readfile():
    try:
        name = input("Enter the file name to read: ")
        p = Path(name)
        if p.exists():
            with open(p, 'r') as fs:
                print("\nFile Content:\n")
                print(fs.read())
        else:
            print("⚠️ File does not exist.")
    except Exception as e:
        print(f"Error: {e}")


def updatefile():
    try:
        name = input("Enter the file name to update: ")
        p = Path(name)
        if p.exists():
            with open(p, 'a') as fs:
                data = input("Enter text to append: ")
                fs.write("\n" + data)
            print("✅ File updated successfully!")
        else:
            print("⚠️ File does not exist.")
    except Exception as e:
        print(f"Error: {e}")


def deletefile():
    try:
        name = input("Enter the file name to delete: ")
        p = Path(name)
        if p.exists():
            os.remove(p)
            print("🗑 File deleted successfully!")
        else:
            print("⚠️ File does not exist.")
    except Exception as e:
        print(f"Error: {e}")


# Menu loop
while True:
    print("\n========= FILE HANDLING MENU =========")
    print("1. Create a new file")
    print("2. Read a file")
    print("3. Update a file")
    print("4. Delete a file") 
    print("5. List files/folders")
    print("6. Exit")

    try:
        check = int(input("Please enter your choice: "))
        if check == 1:
            createfile()
        elif check == 2:
            readfile()
        elif check == 3:
            updatefile()
        elif check == 4:
            deletefile()
        elif check == 5:
            readfileandfolder()
        elif check == 6:
            print("👋 Exiting program.")
            break
        else:
            print("❌ Invalid choice! Please try again.")
    except ValueError:
        print("❌ Please enter a valid number.")
