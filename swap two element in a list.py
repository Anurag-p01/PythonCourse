def swap_elements(lst, index1, index2):
    # Swap using tuple unpacking
    lst[index1], lst[index2] = lst[index2], lst[index1]
    return lst

def main():
    # Get list input from user
    input_str = input("Enter the list elements separated by spaces: ")
    user_list = input_str.split()

    # Optional: convert to integers if needed
    # user_list = list(map(int, user_list))

    print("Original list:", user_list)

    # Get indices to swap
    try:
        index1 = int(input("Enter the first index to swap: "))
        index2 = int(input("Enter the second index to swap: "))

        if index1 < 0 or index2 < 0 or index1 >= len(user_list) or index2 >= len(user_list):
            print("Error: Index out of range.")
        else:
            swapped = swap_elements(user_list, index1, index2)
            print("List after swapping:", swapped)
    except ValueError:
        print("Invalid input. Please enter integer indices.")

if __name__ == "__main__":
    main()
