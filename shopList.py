# import the array library
import array as array

# make an array contrained to be signed integer
lists = array.array('i', [1, 2, 3, 4, 5, 6, 7, 8, 9, 20])
print(lists)

# prompt user to add new item to the list
removeItem  = int(input("Enter item you will like to remove from the list.\n"))

# check if item is present in the list
if removeItem in lists:
        # get the index of the item to be removed from the list
        index = lists.index(removeItem)

        # remove the give item using the index
        lists.pop(index)

        print("The update is list is shown below")
        print(lists)

        # prompt user to add a new item to the list
        addItem = int(input("Enter the new item you will like to add.\n"))

        # check if item is already present in the list
        if addItem in lists:
            print("Sorry, a similar item is already in the list")
        else:
            lists.append(addItem)
            print("You just added", addItem, "to the item list.")
            print(lists)
else:
    print ("Item can not be found in the list.")
