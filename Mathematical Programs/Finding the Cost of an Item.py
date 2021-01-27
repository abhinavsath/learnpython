#Finding the total cost of the item if quantity and price is given
name=input('Enter the name of the Item.')
quantity=int(input('Enter the quantity of the Item. Enter in KGS. eg :- if item = 2 KG, write 2.'))
sprice=int(input('Enter the price of the Item.'))
totalprice=quantity*sprice
print ('Price for the item',name, 'is' ,totalprice, 'Rupees')
