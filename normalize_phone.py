import re

def normalize_phone(phone_number):
    pattern = r"[^\d,+]"
    only_number_plus = re.sub(pattern,'', phone_number)

    if only_number_plus[0]=='+':
         true_format_number=only_number_plus
    elif len(only_number_plus)==12:
         true_format_number="+"+only_number_plus
    elif len(only_number_plus)==10:
         true_format_number="+38"+only_number_plus
    else:
         true_format_number="unrecognized number: "+only_number_plus
    
    print(true_format_number)
    return true_format_number

#test
raw_numbers = [
    "067\\t123 4567",
    "(095) 234-5678\\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ",
]

sanitized_numbers = [normalize_phone(num) for num in raw_numbers]
print("Нормалізовані номери телефонів для SMS-розсилки:", sanitized_numbers)