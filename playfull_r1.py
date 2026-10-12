# Shopping Cart Total
# Write a program that calculates the total price of a product based on the product selected and the quantity entered by the user. The program should support the 
# four available products and display the total amount that needs to be paid




headPhone = 999
smartWatch = 1599
PS5 = 1299
iPad = 599

productName = input("Enter Product Name: ")
quantity = int(input("Enter Quantity: "))

if productName == "headPhone":
    totalprice = headPhone * quantity

elif productName == "smartWatch":
    totalprice = smartWatch * quantity

elif productName == "PS5":
    totalprice = PS5 * quantity

elif productName == "iPad":
    totalprice = iPad * quantity

else:
    totalprice = None
    print("Invalid Product Name")

if totalprice is not None:
    print(f"Total Amount To Be Paid: {totalprice}")