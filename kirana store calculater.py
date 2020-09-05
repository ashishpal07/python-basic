# kirana calculator

'''
sum = 0
while(True):
    price = input("enate items price : ")

    if(price != "q"):
        sum += int(price)
        print(f"your total is so far {sum}.")

    else:
        print(f"your total amount is {sum}.\nThank your visit again")
        break
'''

d = {}
l = []
sum = 0
items_no = int(input("Enter no of items purchased : \n"))

for i in range(items_no):
    item_name = input("Enter item name : ")
    item_price = int(input("Enter item price : "))
    d[item_name] = item_price
    l.append(item_price)

    sum += item_price

print("you prchased = ",d,"\nWelcome to kirana store.\n\nYour Bill Reciept : -->")

for index,value in enumerate(l,1):
    print(f'{index}\t\t{value}')
    
print(f"\nyour total amount is {sum}.\nThank you visit again")
    
