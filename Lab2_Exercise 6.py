def display_main_menu():
    print("display_main_menu")
    print("Enter a value separated by a comma (e.g - 5,7,2,2,3,3,3)")

def get_user_input():
    print("get_user_input")
    inputstr = input()
    print("Raw input =" + inputstr)

    # Split the string into segments using commas as the separator
    splitlist = inputstr.split(",")
    print("After splitting", splitlist)

    # Convert each substring in the list into a float
    floatlist = []
    for x in splitlist:
        try:
            floatnum = float(x)  # Convert string to float
            floatlist.append(floatnum)  # Add float number to the list
        except ValueError:
            print(f"'{x}' is not a valid number and will be ignored.")
    print("Floatlist =", floatlist)
    return floatlist

def calc_average(input_list):
    print("calc_average")
    total = sum(input_list)
    average = total / len(input_list)
    print("Average =", average)
    return average

def find_min_max(input_list):
    print("find_min_max")
    input_list.sort()  # Sort list to make finding min/max easier
    resultlist = [input_list[0], input_list[-1]]
    print("Minimum & Maximum list =", resultlist)
    return resultlist

def sort_temperate(input_list):
    print("sort_temperature")
    input_list.sort()

def calc_median_temperature(input_list):
    print("calculate_median_temperature")
    count = len(input_list)
    input_list.sort()  # Ensure the list is sorted for median calculation

    if count % 2 == 1:
        # If odd, take the middle element
        median = input_list[(count - 1) // 2]
    else:
        # If even, average the two middle elements
        median = (input_list[count // 2] + input_list[(count // 2) - 1]) / 2
    print("Median =", median)
    return median

def main():
    print("ET0735 (DevOps for AIoT) - Lab 2 - Introduction to Python")
    display_main_menu()
    floatlist = get_user_input()
    calc_average(floatlist)
    find_min_max(floatlist)
    sort_temperate(floatlist)
    print("After sorting =", floatlist)
    calc_median_temperature(floatlist)

if __name__ == "__main__":
    main()
