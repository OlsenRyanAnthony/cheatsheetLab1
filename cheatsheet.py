employee_info:


# Define a list of 6 dictionaries to store 6 employees' information
employee_data = [
    {"name": "John", "age": 30, "department": "Sales", "salary": 50000},
    {"name": "Jane", "age": 25, "department": "Marketing", "salary": 60000},
    {"name": "Mary", "age": 23, "department": "Marketing", "salary": 56000},
    {"name": "Chloe",  "age": 35, "department": "Engineering", "salary": 70000},
    {"name": "Mike", "age": 32, "department": "Engineering", "salary": 65000},
    {"name": "Peter", "age": 40, "department": "Sales", "salary": 60000}
]


# This is extra function to demo how to sort the list of dictionaries with chosen key
def sort_employee_data(sortkey):
    templist = employee_data.copy()
    templist.sort(key=lambda x: x[sortkey])
    return templist


def get_employees_by_age_range(age_lower_limit, age_upper_limit):
    result = []

    # check for age limits and append the item to result
    for item in employee_data:
        if int(item["age"]) > int(age_lower_limit) and int(item["age"]) < int(age_upper_limit):
            result.append(item)

    return result


def calculate_average_salary():
    total = 0
    average = 0

    #add your implementation to calculate here
    for everyDictionary in employee_data:
        employeeSalary = everyDictionary["salary"]
        total += employeeSalary

    average = total / len(employee_data)
    average = round(average, 2)  # Rounded to 2 decimal points
    return average


def get_employees_by_dept(targetDept):
    result = []   # A empty list, to be filled in with selected dictionaries

    # Add your implementation from here
    for everyDictionary in employee_data:
        if everyDictionary["department"] == targetDept:
            result.append(everyDictionary)

    return result

def display_all_records():
    print(("Name" + "\t" +"Age" +"\t" +"Department" +"\t" +"Salary" ).expandtabs(15))
    for item in employee_data:
        print((item["name"] + "\t" + str(item["age"]) + "\t" + item["department"] + "\t" + str(item["salary"])).expandtabs(15))


def display_records(employee_info):
    print(("Name" + "\t" +"Age" +"\t" +"Department" +"\t" +"Salary" ).expandtabs(15))
    for item in employee_info:
        print((item["name"] + "\t" + str(item["age"]) + "\t" + item["department"] + "\t" + str(item["salary"])).expandtabs(15))

def display_main_menu():

    print("\n----- Employee information Tracker -----")

    print("Select option\n")

    print("1 - Display all records")
    print("2 - Display average salary")
    print("3 - Display employee within age range")
    print("4 - Display employee in a department")
    print("5 - Display all records according to sort key")     # This is extra function added.
    print("Q - Quit")

    option = input("Enter selection =>")

    if option == '1':
        display_all_records()

    elif option == '2':
        average_salary = calculate_average_salary()
        print("Average salary = " + str(average_salary))

    elif option == '3':
        age_lower_limit = input("age (Lower Limit) = ")
        age_upper_limit = input("age (Uper Limit) = ")
        employee_info = get_employees_by_age_range(age_lower_limit, age_upper_limit)
        display_records(employee_info)


    elif option == '4':
        department = input("Name of Department = ")
        employee_info = get_employees_by_dept(department)
        display_records(employee_info)


    elif option == '5':             # Extra function added to the menu.
        # Ask for the key to be used for sorting
        sortkey = input("Enter key for sorting = ")
        newlist = sort_employee_data(sortkey)
        display_records(newlist)


    elif option == 'Q':
        quit()

def main():

    while (True):
        display_main_menu()


if __name__ == "__main__":
    main()




Lab3


print("Lab 3 - Software Unit Testing with PyTest")

SORT_ASCENDING = 0
SORT_DESCENDING = 1


def bubble_sort(arr, sorting_order):

    # Copy input list to results list
    arr_result = arr.copy()

    # Get number of elements in the list
    n = len(arr_result)

    if n==0:
        return 0
    
    if n>= 10:
        return 1
    

    for item in arr_result:
        if isinstance(item, int)==False:
            return 2
 
    if n < 10:
        # Traverse through all array elements
        for i in range(n - 1):
            # range(n) also work but outer loop will
            # repeat one time more than needed.

            # Last i elements are already in place
            for j in range(0, n - i - 1):

                if sorting_order == SORT_ASCENDING:
                    if arr_result[j] > arr_result[j + 1]:
                        arr_result[j], arr_result[j + 1] = arr_result[j + 1], arr_result[j]


                elif sorting_order == SORT_DESCENDING:
                    if arr_result[j] < arr_result[j + 1]:
                        arr_result[j], arr_result[j + 1] = arr_result[j + 1], arr_result[j]

                else:
                    # Return an empty array
                    arr_result = []
    else:
        arr_result = -1

    return arr_result

def main():
    # Driver code to test above
    arr = [64, 34, 25, 12, 22, 11, 90]

    # Sort in ascending order
    result = bubble_sort(arr, SORT_ASCENDING)
    print("\nSorted array in ascending order: ")
    print(result)

    # Sort in descending order
    print("Sorted array in descending order: ")
    result = bubble_sort(arr, SORT_DESCENDING)
    print(result)

    # Testing of zero array
    print("Sort an empty list: ")
    empty_arr = []
    result = bubble_sort(empty_arr, SORT_DESCENDING)
    print(result)

    # Testing of long array
    print("Sort an too-long list: ")
    long_arr = [64, 34, 25, 12, 22, 11, 90, 5, 7, 23]
    result = bubble_sort(long_arr, SORT_DESCENDING)
    print(result)


    # Testing of non-integer array
    print("Sort an non-integer list: ")
    non_int_arr = [64, 34, 25, 12.5, 22, 11, 90]
    result = bubble_sort(non_int_arr, SORT_DESCENDING)
    print(result)



if __name__ == "__main__":
    main()




PRICE_INFO.PY




price_list={'apple' : 1.20, 'orange':1.40, 'watermelon': 6.50, 'pineapple': 2.70, 'pear' : 0.90, 'papaya': 2.95, 'pomegranate': 4.95 }

quantity_list= {'apple': 5, 'orange':5, 'watermelon': 1, 'pineapple': 2, 'pear' : 10, 'papaya': 1, 'pomegranate': 2}

# This is exatr function to demo how to get the value in dictionary.
def print_fruit_price_and_quantity(whatfruit):
    fruitprice = price_list[whatfruit]
    fruitquantity = quantity_list[whatfruit]
    print("Price of " + whatfruit + " is ", fruitprice)
    print("Quantity to buy is ", fruitquantity)



def total_cost_shopping():
    total_cost = 0
    for key in price_list.keys():
        if key in quantity_list:
            # complete the implementation below:
            total_cost += ( price_list[key]  * quantity_list[key] )
    print("total cost = ", total_cost)
    return total_cost


def cost_of_fruits(fruit, quantity):
    for key in price_list.keys():
        if key == fruit:
            cost = quantity*price_list[key]
            break

    print("cost of ", quantity, fruit, "=", cost)
    return cost


def main():

    cost_of_fruits('apple', 10)
    total_cost_shopping()
    print_fruit_price_and_quantity("pear")


if __name__ == "__main__":
    main()





TEST_EMPLOYEE.PY



import employee_info as EMP
from employee_info import employee_data as EMPDATA


def test_get_employees_by_age_range():
    upper = 33
    lower = 29
    expected = [EMPDATA[0], EMPDATA[4]]
    result = EMP.get_employees_by_age_range(lower, upper)
    assert(result == expected)


def test_calculate_average_salary():
    expected = 60166.67 # Rounded to 2 decimal points
    result = EMP.calculate_average_salary()
    assert(result == expected)


def test_get_employees_by_dept_engg():
    targetDept = "Engineering"
    expected = [EMPDATA[3], EMPDATA[4]]
    result = EMP.get_employees_by_dept(targetDept)
    assert(result == expected)


def test_get_employees_by_dept_marketing():
    targetDept = "Marketing"
    expected = [EMPDATA[1], EMPDATA[2]]
    result = EMP.get_employees_by_dept(targetDept)
    assert(result == expected)



TEST_LAB3.PY




import Lab3

print("Test_Lab3")


def test_bubble_sort_ascending():
    result = []
    input_arr = [64, 34, 25, 12, 22, 11, 90]
    test_arr = [11, 12, 22, 25, 34, 64, 90]

    result = Lab3.bubble_sort(input_arr, Lab3.SORT_ASCENDING)

    assert (result == test_arr)

def test_bubble_sort_descending():
    result = []
    input_arr = [64, 34, 25, 12, 22, 11, 90]
    test_arr = [90, 64, 34, 25, 22, 12, 11]

    result = Lab3.bubble_sort(input_arr, Lab3.SORT_DESCENDING)

    assert (result == test_arr)

def test_bubble_sort_invalid():
    result = []
    input_arr = [64, 34, 25, 12, 22, 11, 90]

    result = Lab3.bubble_sort(input_arr, 3)

    assert (result == [])



def test_bubble_too_long():
    expected = 1
    input_arr = [64, 34, 25, 12, 22, 11, 90, 77, 88, 99]
    result = Lab3.bubble_sort(input_arr, Lab3.SORT_DESCENDING)
    assert (result == expected)



def test_bubble_empty():
    expected = 0
    input_arr = []
    result = Lab3.bubble_sort(input_arr, Lab3.SORT_DESCENDING)
    assert (result == expected)


def test_bubble_non_integer():
    expected = 2
    input_arr = [64, 34.4, 25, 12, 22, 11, 90, 77]
    result = Lab3.bubble_sort(input_arr, Lab3.SORT_DESCENDING)
    assert (result == expected)






TEST_PRICE_INFO.PY




import price_info as PI


def test_cost_of_fruit():
    fruitname = "pear"   # price is $0.90
    quantity = 5
    expected = 4.50
    result = PI.cost_of_fruits(fruitname, quantity)
    assert(result == expected)


def test_total_cost():
    PI.quantity_list = {'apple': 5, 'orange':5, 'watermelon': 2, 'pineapple': 2, 'pear' : 10, 'papaya': 1, 'pomegranate': 2}
    expected = 46.75 + 6.50   # +6.50 because of extra one watermelon to purchase, priced at $6.50
    result = PI.total_cost_shopping()
    assert(result == expected)




README NOTES