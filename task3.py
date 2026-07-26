import re

def normalize_phone(phone_number):
    pattern = r"[^0-9+]"
    replacement = ""
    clean_phone = re.sub(pattern, replacement, phone_number)

    if clean_phone.startswith("+"):
        return clean_phone 
    elif clean_phone.startswith("380"):
        return "+" + clean_phone
    else:
        return "+38" + clean_phone

raw_numbers = [
    "067\t123 4567",
    "(095) 234-5678",
    "+380 44 123 4567"
]

sanitized_numbers = [normalize_phone(num) for num in raw_numbers]
print("Нормалізовані номери телефонів для SMS-розсилки:", sanitized_numbers)