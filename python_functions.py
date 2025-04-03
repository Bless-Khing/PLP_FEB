def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        discount_amount = (discount_percent/100) * price
        new_price = price - discount_amount
        print(f"The final price after applying the discount is {new_price}.")


    else:
        print(f"No discout applied. The price still remains {price}")
    

original_price = float(input("Please enter the original price: "))
discount_percentage =  int(input("Enter the discount in percent: "))

calculate_discount(original_price, discount_percentage)
