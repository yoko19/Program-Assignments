'''
This file makes a terminal checklist.
You can add, remove, update, and read entries from the list.
An empty checkbox is prepended to every new entry.
You can then check or uncheck the entry's checkbox.
'''

# creating empty list
checklist = [] 
# CREATE
def create(item):

    # Create item code here
    checklist.append(item)

    return "Added {} to checklist".format(item)
# READ
def read(index):

    # Read code here
    print(checklist[index])

    return checklist[index]
# UPDATE
def update(index, item):

    old = checklist[index]

    # Update code here
    checklist[index] = item

    return "Changed {} to {}".format(old, item)

# DESTROY
def destroy(index):

    removed = checklist[index]

    # Destroy code here
    checklist.pop(index)

    return "Removed {} from checklist".format(removed)

# SEE ALL ITEMS
def all_items():

    items = []

    for element in checklist:
        print(element)
        items.append(element)
    
    return items
# ADD CHECK MARK TO ITEM
def checked(index):

    unchecked = checklist[index]

    checklist[index] = "check " + unchecked

    return checklist[index]
# USER INPUT FUNCTION
def user_input(prompt):

    entry = input(prompt)

    return entry
# USER CHOICE FUNCTIx
def user_choice():

    editing = True 

    while editing:

        choice = user_input("Which function would you like to use? Enter C for create, R for read, U for update, D for destroy, A to view all items in checklist and S to select an item with a checkmark. ")

        if choice == "C" or choice == "c":

            item = user_input("What item do you want ot crwtae create? Type out the name of your desired item. ")

            create(item)

            continue
        elif choice == "R" or choice == "r":

            index = user_input("What item do you wanto  read? Give a number for the position of the item. ")

            read(int(index))

            continue
        elif choice == "U" or choice == "u":

            update_index = user_input("What item do ypu want to update? Give the number for the position. ")

            new_item = user_input("what is your new item. ")

            update(int(update_index), new_item)

            continue
        elif choice == "D" or choice == "d":

            delete_index = user_input("What item do you want to delete? what is the number of the item. ")

            destroy(int(delete_index))

            continue
        elif choice == "A" or choice == "a":

            all_items()

            continue
        elif choice == "S" or choice == "s":

            checked_index = user_input("What item do you wantto check of? Give the number of the position. ")

            checked(int(checked_index))

            continue

        else:

            end = user_input("Quit? Enter Y or N. ")

            if end == "Y" or end == "y":
                print(checklist)
                editing = False

            else:

                continue

def test():

    # create("purple sox")
    # create("red cloak")
    # print(read(0))
    # print(read(1))
    # update(0, "purple socks")
    # destroy(1)
    # print(read(0))
    # print(all_items())
    # print(checked(0))
    # print(user_input("Is this working? "))
    user_choice()

user_choice()