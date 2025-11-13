def display_main_menu():
    print("Enter some numbers seperated by commas(e.g. 5, 67, 32)")

def get_user_input():
    print("get_user_input")
    numlist = []
    inputstr = input()
    numlist = inputstr.split(",")
    for eachnum in numlist:
        numlist.append(float(eachnum))

        return numlist

def calc_average(numlist):
    print("Sub: calc_average")
    total = sum(numlist)
    average = total / len(numlist)
    print("Average = " , f{average . 2f})

    


def find_min_max(numlist):
    print("find_min_max")


def sort_temperature(numlist):
    print("Sub: sort_temperature")
    templist = numlist.copy()
    templist.sort()
    print("Sorted Numbers = ", templist)
    return templist

def calc_median_temperature(numlist):
    print("calc_median_temperature")


def main():
    print("ET0735 (DevOps for AIoT) - Lab 2 - Introduction to Python")
    display_main_menu()
    arraylist = get_user_input()

if __name__ == "_main_":
    main()