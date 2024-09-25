def calculate_discount(purchase_amount):
    discount_rate = 0.10 if purchase_amount > 5000 else 0.05
    
    discount = purchase_amount * discount_rate
    final_amount = purchase_amount - discount
    
    return final_amount, discount

def main():
    while True:
            purchase_amount = float(input("Enter the total purchase amount: "))
            
            final_amount, discount = calculate_discount(purchase_amount)
            
            print(f"Initial Purchase Amount: {purchase_amount:.2f}")
            print(f"Discount: {discount:.2f}")
            print(f"Final price: {final_amount:.2f}")
            
            try_again = input("Do oyu want to try again? (yes/no): ").strip().lower()
            if try_again != 'yes':
                print("Thank you!")
                break
main()
