#Micah DeCaro, 9/12/24, Total Purchase
def calculate_total_purchase():
    # A customer in a store is purchasing five items.  
    # Write a program that asks for each item, 
    # then displays the subtotal of the sale, 
    # the amount of sales tax, and the total.  
    # Assume the sales tax is 7 percent.
    item1=float(input("What is the price of item 1 in dollars? "))
    item2=float(input("What is the price of item 2 in dollars? "))
    item3=float(input("What is the price of item 3 in dollars? "))
    item4=float(input("What is the price of item 4 in dollars?"))
    item5=float(input("What is the price of item 5 in dollars? "))

    subtotal=(item1+item2+item3+item4+item5)
    sales_tax=subtotal*.07
    total=subtotal+sales_tax
    print('Your subtotal is $', subtotal)
    print('The sales tax is $', format(sales_tax, '.2f'))
    print('Therefore, your total cost is $', format(total, '.2f'))
    
calculate_total_purchase()
