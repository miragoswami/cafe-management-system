@ -0,0 +1,32 @@
menu = {
    'pizza': 80,
    'pasta': 60,
    'roll' : 40,
    'momos': 50,
}

 
print("welcome sir to our Restaurant")
print(" pizza : Rs.80 \n pasta : Rs.60 \n roll  : Rs.40 \n momos : Rs.50")

order_total = 0

item_1 = input("enter name of item which you want to order :")
if item_1 in menu :
    order_total += menu[item_1]
    print("your ", item_1 , "has been added to your order")
else:
    print("Ordered item is not available yet! ")
    
another_item=  input("do you want to order somehting else? (yes/no) :" )
if another_item == "yes" :
       item_2 = input("enter the name of the item : " )
       if item_2 in menu :
            order_total += menu[item_2]
            print("another item " , item_2 , "has been added to your order ! ")
       else:
           print("Ordered item is not available ! ")

print("total amount of item is " ,order_total)

    
