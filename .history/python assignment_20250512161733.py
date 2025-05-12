def calculate_discount(price, discount_percent):
    """
    Calculate the final price after applying a discount.
    
    Args:
        price (float): The original price of the item
        discount_percent (float): The discount percentage
        
    Returns:
        float: The final price after discount (if applicable)
    """
    if discount_percent >= 20:
        # Apply the discount
        discount_amount = price * (discount_percent / 100)
        final_price = price - discount_amount
        return final_price
    else:
        # Return original price if discount is less than 20%
        return price

def main():
    # Get input from user
    try:
        price = float(input("Enter the original price of the item: $"))
        discount_percent = float(input("Enter the discount percentage: "))
        
        # Validate inputs
        if price < 0 or discount_percent < 0:
            print("Please enter positive values for price and discount.")
            return
            
        # Calculate and display the final price
        final_price = calculate_discount(price, discount_percent)
        
        # Check if discount was applied
        if discount_percent >= 20:
            print(f"A {discount_percent}% discount was applied.")
            print(f"Final price after discount: ${final_price:.2f}")
        else:
            print(f"No discount applied (discount was less than 20%).")
            print(f"Original price: ${final_price:.2f}")
            
    except ValueError:
        print("Invalid input. Please enter numeric values.")

if __name__ == "__main__":
    main()