def check_if_entered_number_is_valid(entered_number):
   is_valid = entered_number < 1 or entered_number > 100
   return not(is_valid)

def even_calculations(entered_number):
    factors = []
    for i in range(1, entered_number + 1):
        if entered_number % i == 0:
            factors.append(i)
    return factors

def odd_calculations(entered_number):
    p = 1
    for i in range(1, entered_number + 1):
        p = p * i
    return p
            

def f_calculation(numberinput):

    if not(check_if_entered_number_is_valid(numberinput)):
        return 'Entered number is not valid'

    if numberinput % 2 == 0:
        responce = even_calculations(numberinput)
    else:
        responce = odd_calculations(numberinput)

    return responce
