import random 

def get_numbers_ticket(min, max, quantity):
    if min < 1 or max > 1000 or quantity > (max - min + 1):
        return []
    
    numbers = random.sample(range(min, max +1), quantity)
    numbers.sort()
    return numbers

lotery_numbers = get_numbers_ticket(1, 49,6)
print(f"Ваші лотерейні числа: {lotery_numbers}")
