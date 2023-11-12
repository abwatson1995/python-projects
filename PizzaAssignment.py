number_of_pizzas = int(input('Enter number of pizzas: '))
number_of_teenagers = int(input('Enter number of teens: '))
number_of_slices_in_each_pizza = int(input('Enter number of slices in each pizza: '))

print(f"\n We have {number_of_pizzas} pizzas and {number_of_teenagers} people "
f"\n that means {(number_of_pizzas*number_of_slices_in_each_pizza)/number_of_teenagers} slices per \n teenager")