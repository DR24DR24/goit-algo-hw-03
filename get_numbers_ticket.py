import random

def get_numbers_ticket(min, max, quantity):
    if min<1 or not isinstance(min, int):
         return []
    if max>1000 or not isinstance(max, int):
         return []
    if quantity>max-min+1 or not isinstance(quantity, int):
         return []
    
    numbers_ticket=random.sample(range(min,max+1), k=quantity)
    sort_numbers_ticket=sorted(numbers_ticket)
    return sort_numbers_ticket
    

#test
lottery_numbers = get_numbers_ticket(1, 5, 5)
print("Ваші лотерейні числа:", lottery_numbers)