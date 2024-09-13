#Micah DeCaro, 9/12/24, Total Purchase
def calculate_total_purchase():
    # A customer in a store is purchasing five items.  
    # Write a program that asks for each item, 
    # then displays the subtotal of the sale, 
    # the amount of sales tax, and the total.  
    # Assume the sales tax is 7 percent.
    print ("What is the price of item 1 in dollars? ")
    item1=float(input())
    print("What is the price of item 2 in dollars? ")
    item2=float(input())
    print("What is the price of item 3 in dollars? ")
    item3=float(input())
    print("What is the price of item 4 in dollars? ")
    item4=float(input())
    print("What is the price of item 5 in dollars? ")
    item5=float(input())

    subtotal=float(item1+item2+item3+item4+item5)
    sales_tax=subtotal*.07
    total=subtotal+sales_tax
    print("""'$' subtotal
    '$' sales_tax
    '$' total
    """)



calculate_total_purchase()
