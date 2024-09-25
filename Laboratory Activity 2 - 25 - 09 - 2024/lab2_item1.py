def is_palindrome(digit):
    str_digit = str(digit)
    
    if str_digit == str_digit[::-1]: 
        return "Palindrome"
    else:
        return "Not a Palindrome"

digit = int(input("Enter an interger: "))
result = is_palindrome(digit)
print(result)

