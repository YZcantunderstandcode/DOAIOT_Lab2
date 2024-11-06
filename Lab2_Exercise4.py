
def display_main_menu():
    print ("display_main_menu")
    print ("Enter a value separated by a comma (e.g - 5,7,2,2,3,3,3)")

def get_user_input():
    print ("get_user_input")
    inputstr=input()
    print ("Raw input =" + inputstr)

    # Next step is to split  the string into segments of strings using comma as splitter
    splitlist=inputstr.split(",")
    print ("After splitting ", splitlist)

    #Next step is to convert eachs hort string in the list into float
    floatlist = [] #define an empty list of float numbers
    for x in splitlist:
        floatnum=float(x) #Convert string to float 
        floatlist.append(floatnum) #Add float number to the float list
    print ("Floatlist= ", floatlist)
    return floatlist


def calc_average(input_list):
    print ("cal_average")
    total= sum(input_list)
    average=total/len(input_list)
    print ("Average = ", average)
    return average 

def find_min_max(input_list):
    print ("find_min_max")
    input_list.sort()
    resultlist = [input_list[0], input_list[-1]]
    print ("Minimum & Maximum list =" , resultlist)
    return resultlist

def sort_temperate(input_list):
    print ("sort_temperature")

def calc_median_temperature(input_list):
    print ("calculate_median_temperature")

def main ():
    print("ET0735 (DevOps for AIoT) - Lab 2 - Introduction to Python")
    display_main_menu()
    floatlist = get_user_input()
    calc_average(floatlist)
    find_min_max(floatlist)


if __name__=="__main__":
    main()
