# (open/create file and return lines of text as a list of strings)
def getList(example):
    try:
        with open("example.txt", "r") as file:
            data = file.readlines()
        return [item.strip() for item in data]  # Remove newline characters and return list
    except FileNotFoundError:  # Handle the case where the file does not exist
        return []

# (receive list of strings and display them, or "nothing in list" message)
def showList(data):
    if len(data) == 0:
        print("Nothing in the list.")
    else:
        for index, item in enumerate(data, start=1):
            print(f"{index}. {item}")


# --- addToList(example, data), returns a list of strings ---
def addToList(example, data):
    new_item = input("Enter the item to add: ")
    data.append(new_item)
    with open("example.txt", "a") as file:  # Append mode to add new item to file
        file.write(new_item + "\n")  # Add item to file
    return data


# (prompt for item number to delete from the list of strings and write list to the file)
def deleteFromList(example, data):
    showList(data)  # Show current list items
    try:
        item_index = int(input("Enter the number of the item to delete: ")) - 1
        if 0 <= item_index < len(data):
            deleted_item = data.pop(item_index)  # Remove item from list
            with open("example.txt", "w") as file:  # Write mode to update entire file
                file.write("\n".join(data))  # Update file without deleted item
            print(f"Deleted: {deleted_item}")
        else:
            print("Invalid item number.")
    except ValueError:  # Handle non-integer input for item number
        print("Invalid input for item number.")
    return data


# --- main part of program ---
example = 'list.txt'  # define the example used to store the list
lineList = getList(example)  # call the getList function to read the file into a list

while True:  # this endless loop displays the list and prompts the user for a command

    showList(lineList)  # call showList to show the current content of the list

    # show the instructions for the possible commands - [a]dd, [d]elete, e[x]it
    print('\nType "a" to add an item.')

    if len(lineList) > 0:  # only show the delete instruction if the list has items
        print('Type "d" to delete an item.')

    print('Type "x" to exit.')

    command = input('> ')  # prompt for a command

    # if "a", call addToList to prompt for item and add to list
    if command == 'a':
        lineList = addToList(example, lineList)

    # if "d", call deleteFromList to prompt for item number and delete from list
    elif command == 'd' and len(lineList) > 0:
        lineList = deleteFromList(example, lineList)

    elif command == 'x':  # if "x", break out of the loop to end the program
        print('Goodbye!')
        break

    else:  # if anything else, show an error message
        print('Invalid command.\n')
