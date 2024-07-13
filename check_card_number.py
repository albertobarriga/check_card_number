def luhn_check(card_number):
    card_number = card_number.replace(" ", "")
    
    # Verify that the card number has between 13 and 19 digits
    if not (13 <= len(card_number) <= 19):
        return False

    reversed_digits = card_number[::-1]
    total_sum = 0
    
    for i, digit in enumerate(reversed_digits):
        n = int(digit)
        if i % 2 == 1:
            n *= 2
            if n > 9:
                n -= 9
        total_sum += n
    
    return total_sum % 10 == 0

def main():
    card_number = input("Please enter the credit card number: ")
    is_valid = luhn_check(card_number)
    if is_valid:
        print(f"The card number {card_number} is valid.")
    else:
        print(f"The card number {card_number} is invalid.")

if __name__ == "__main__":
    main()
