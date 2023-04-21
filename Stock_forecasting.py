initial_stock = int(input("Enter initial stock value:  "))

number_of_months = int(input("Enter number of months to plan: "))

monthly_sales = {}

for month in range (1, number_of_months+1): 
    planned_sales = int(input(f"Enter planned sales for the month {month}: "))
    monthly_sales[month] = planned_sales

for month, planned_sales in monthly_sales.items(): 
    if initial_stock > planned_sales: 
        print(f"Your production quantity for month {month} is 0")

        initial_stock -= planned_sales
    else: 
        quantity_produced = planned_sales - initial_stock
        print(f"Your production quantity for month {month} is {quantity_produced}")

        initial_stock += quantity_produced - planned_sales






