# ranges.py
# ---------
# By MWC Contributors

def print_all_numbers(maximum):
    "Prints all integers from 0 to maximum."
    for number in range(maximum):
        print(number)

def print_even_numbers(maximum):
    "Prints all even integers from 0 to maximum."
    pass

def print_odd_numbers(maximum):
    "Prints all odd integers from 0 to maximum."
    pass

def print_multiples_of_five(maximum):
    "Prints all integers which are multiples of five from 0 to maximum."
    pass

chosen_maximum = int(input("Choose a number: "))
print(f"All numbers from 0 to {chosen_maximum}")
print_all_numbers(chosen_maximum)
print(f"All even numbers from 0 to {chosen_maximum}")
print_even_numbers(chosen_maximum)
print(f"All odd numbers from 0 to {chosen_maximum}")
print_odd_numbers(chosen_maximum)
print(f"All multiples of 5 from  0 to {chosen_maximum}")
print_multiples_of_five(chosen_maximum)

