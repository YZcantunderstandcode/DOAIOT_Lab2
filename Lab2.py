def display_main_menu():
    print("display_main_menu")
    print("Enter some numbers separated by commas (e.g. 5, 67, 32)")

def get_user_input():
    print("===============================")
    print("getting user input")
    inputstr = input("numbers here: ")
    print("You entered: ", inputstr)

    # Split the input string into segnments of strings using comma as splitter
    splitlist = inputstr.split(",")

    # Next step is to convert each short string in hte list into float 
    floatlist = [] # Create an empty list
    for i in splitlist:
        floatlist.append(float(i))

    print(f"List of floats: {floatlist} \n")
    return floatlist
    

def calc_average_temperature(list):
    print("===============================")
    print("calc_average_temperature")
    sum = 0
    for i in list:
        sum += i
    average = sum / len(list)
    print(f"Average temperature: {average} \n")

def calc_min_max_temperature(list):
    print("===============================")
    print("calculate min and max temperature")
    # min = list[0]
    # max = list[0]
    # for i in list:
    #     if i < min:
    #         min = i
    #     if i > max:
    #         max = i

    list.sort()
    min = list[0]
    max = list[-1]
    print(f"Min temperature: {min}")
    print(f"Max temperature: {max}\n")

def calc_median_temperature(list):
    print("===============================")
    print("calculate median temperature")
    list.sort()
    if len(list) % 2 == 0:
        median = (list[len(list) // 2] + list[len(list) // 2 - 1]) / 2
    else:
        median = list[len(list) // 2]
    print(f"Median temperature: {median}\n")

def main():
    print("ET0735 (DevOps for AIoT) - Lab 2 - Introduction to Python")
    display_main_menu()
    result_list = get_user_input()
    calc_average_temperature(result_list)
    calc_min_max_temperature(result_list)
    calc_median_temperature(result_list)

if __name__ == "__main__":
    main()