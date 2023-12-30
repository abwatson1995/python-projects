grade_dict= {'english':[90,95,81],
                'math':[100,95,93,98],
                'history':[76,98]}

class_name = ''

''' ******** START MAIN MENU FUNCTIONS ********'''
def print_menu():
    print('1 = reporting')
    print('2 = maintenance')
    print('0 = exit')

def display_grade_manager_list():
    global class_name
    
    while True:
        print("Your grade manager contains grades for:")
        print()
        for key in grade_dict.keys():
            print(f'> {str(key)}')
        print()
        print("To add another class and grades, select 'add'   ")
        print("To work with a class, type the name of the class   ")
        print("To end the program, type 'end'   ")
        print()
        
        try:
            user_option = input("Enter your choice  ").lower().strip()
            print()
            if user_option == 'add':
                add_class_and_grades_to_dict()
            elif user_option in grade_dict:
                class_name = user_option
                perform_reporting_or_maintenance()
            elif user_option == 'end':
                print("Finished processing grades")
                break
            else:
                print("Invalid option, please choose a valid option")
                print()
        except Exception as e:
            print(f"An error occurred: {str(e)}")

def add_class_and_grades_to_dict():
    global grade_dict
    
    try:
        user_key = input("Enter a class name  ").lower()
        user_value = input("Enter grades separated by spaces  ")
        value_list = user_value.split()
        value_list = [int(num) for num in value_list]
        grade_dict[user_key] = value_list
        print(f'The new list contains {grade_dict}')
    except ValueError:
        print("Please enter valid grades as space-separated integers.")
        print()
    except Exception as e:
        print(f"An error occurred: {str(e)}")
    
'''******** END MAIN MENU FUNCTIONS ********'''

def perform_reporting_or_maintenance():
    global class_name
    
    print('**'*15)
    print_menu()
    print('**'*15)
    
    try:
        user_input = int(input('Reporting or Maintenance   '))
        if user_input == 1:
            perform_reporting()
        elif user_input == 2:
            perform_maintenance()
        elif user_input == 0:
            print('Finished processing grades')
            return
        else:
            print('Please enter a valid option (0, 1, or 2).')
            print()
    except ValueError:
        print('Please enter a valid integer (0, 1, or 2) as the option.')
        print()
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        
'''******** START REPORTING FUNCTIONS********'''
def perform_reporting():
    global grade_dict
    global class_name
    
    print('**'*15)
    print('*** Grade Reporting ***')
    print('**'*15)
    
    try:
        print("Options: best worst average end summary    ")
        user_input = input("Select a command   ")
    
        if user_input == 'best':
            get_best_grade(grade_dict, class_name)
            print()
            perform_reporting()
        elif user_input == 'worst':
            get_worst_grade(grade_dict, class_name)
            print()
            perform_reporting()
        elif user_input == 'average':
            get_average_grade(grade_dict, class_name)
            print()
            perform_reporting()
        elif user_input == 'summary':
            get_summary(grade_dict, class_name)
            print()
            perform_reporting()
        elif user_input == 'end':
            return
            print()
        else:
            print("Invalid reporting option. Please select a valid option")
            print()
            perform_reporting_or_maintenance()
    except Exception as e:
        print(f"An error occurred: {str(e)}")
    
def get_best_grade(grade_dict, class_name):
    if class_name in grade_dict:
        grades = grade_dict[class_name]
        best_grade = max(grades)
        if best_grade is not None:
            print(f"The best grade in {class_name} class is: {best_grade}")
            print()
        else:
            print(f"No grades found for the class '{class_name}'")
            print()
    else:
        print(f"The class '{class_name}' was not found in the dictionary.")
        
def get_worst_grade(grade_dict, class_name):
    if class_name in grade_dict:
        grades = grade_dict[class_name]
        worst_grade = min(grades)
        if worst_grade is not None:
            print(f"The worst grade in {class_name} class is: {worst_grade}")
        else:
            print(f"No grades found for the class '{class_name}'")
    else:
        print(f"The class '{class_name}' was not found in the dictionary.")

def get_average_grade(grade_dict, class_name):
    if class_name in grade_dict:
        grades = grade_dict[class_name]
        if grades:
            average_grade = sum(grades) / len(grades)
            print(f"The average grade in {class_name} class is: {average_grade}")
            print()
        else:
            print(f"No grades found for the class '{class_name}'")
            print()
    else:
        print(f"The class '{class_name}' was not found in the dictionary.")

def get_summary(grade_dict, class_name):
    if class_name in grade_dict:
        grades = grade_dict[class_name]
        print(f"Grades in {class_name}: {' '.join(str(grade) for grade in grades)}")
    else:
        print(f"The class '{class_name}' was not found in the dictionary.")
        
''' ******** END REPORTING FUNCTIONS ********'''

''' ******** START MAINTENANCE FUNCTIONS ********'''

def perform_maintenance():
    global class_name
    global grade_dict
    grades = grade_dict[class_name]
    
    print('**'*15)
    print(f'*** Maintaining Grades for {class_name} ***')
    print('**'*15)
    print()
    print(f"Currently, the grades are: {' '.join(str(grade) for grade in grades)}")
    print()
    display_maintenance_menu()

def display_maintenance_menu():
    while True:
        print("1) Change a grade")
        print("2) Add a grade")
        print("3) Delete a grade")
        print("4) End")
        print()
        
        try:
            user_option = int(input("Select an option: "))
            print()
            
            if user_option == 1:
                change_class_grade(grade_dict)
            elif user_option == 2:
                add_new_grade(grade_dict)
            elif user_option == 3:
                delete_class_grade(grade_dict)
            elif user_option == 4:
                perform_reporting_or_maintenance()
                break
            else:
                print("Invalid selection. Please select a valid menu option")
                print()
        except ValueError:
            print("Please enter a valid integer (1, 2, 3, or 4) as the option.")
            print()
        except Exception as e:
            print(f"An error occurred: {str(e)}")

            
def change_class_grade(grade_dict):
    global class_name
        
    if class_name in grade_dict:
        grades = grade_dict[class_name]
        print(f"Current grades for {class_name}: {grades}")
        try:
            old_grade = int(input("Enter the grade you want to change: "))
            if old_grade in grades:
                new_grade = int(input("Enter the new grade: "))
                print()
                index = grades.index(old_grade)
                grades[index] = new_grade
                grade_dict[class_name] = grades
                print(f"Updated grades for {class_name}: {grades}")
                print()
            else:
                print(f"The grade {old_grade} does not exist in {class_name}.")
                print()
        except ValueError:
            print("Please enter valid integer values.")
            print()
    else:
        print(f"The class '{class_name}' was not found in the dictionary.")
        print()

def add_new_grade(grade_dict):
    global class_name
    
    if class_name in grade_dict:
        grades = grade_dict[class_name]
        print(f"Current grades for {class_name}: {grades}")
        print()
        
        try:
            new_grade = int(input("Enter the new grade to add: "))
            print()
            grades.append(new_grade)
            grade_dict[class_name] = grades
            print(f"Updated grades for {class_name}: {grades}")
            print()
        except ValueError:
            print("Please enter a valid integer value.")
            print()
    else:
        print(f"The class '{class_name}' was not found in the dictionary.")
        print()

def delete_class_grade(grade_dict):
    global class_name
    
    if class_name in grade_dict:
        grades = grade_dict[class_name]
        print(f"Current grades for {class_name}: {grades}")
        print()
        
        try:
            grade_to_delete = int(input("Enter the grade to remove: "))
            print()
            if grade_to_delete in grades:
                grades.remove(grade_to_delete)
                grade_dict[class_name] = grades
                print(f"Updated grades for {class_name}: {grades}")
                print()
            else:
                print(f"The grade {grade_to_delete} does not exist in {class_name}.")
                print()
        except ValueError:
            print("Please enter a valid integer value.")
            print()
    else:
        print(f"The class '{class_name}' was not found in the dictionary.")
        
display_grade_manager_list()