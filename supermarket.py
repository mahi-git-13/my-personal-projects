from datetime import datetime

name="mahesh"

items_list = '''    
Rice  rs 20/kg 
sugar rs 30/kg
oil   rs 80/liter
boost rs 90/kg'''
#declaration
price=0
pricelist=[]
totalprice=0
Finalprice=0
finalamount=0
gst=0
ilist=[]
qlist=[]
plist=[]

#rates for items
items={'rice' or 'Rice': 20 ,'sugar':30,'oil' : 80 ,'boost':90}
option=int(input("For list of items press 1: "))
if option==1:
    print(items_list)
for i in range(len(items)):
    inp1=int(input("Enter 1 to buy or 2 to exit : "))
    if inp1==2:
        break
    if inp1==1:
        item=input("Enter items: ")
        quantity=int(input("Enter your Quantity : "))
        if item in items.keys():
            price=quantity*(items[item])
            pricelist.append((item,quantity,items,price))
            totalprice+=price
            ilist.append(item)
            qlist.append(quantity)
            plist.append(price)
            gst=(totalprice*5)/100
            finalamount=gst+totalprice
        else:
            print("Sorry you entered item is NOT AVAILABLE ")
    else:
        print(" You entered wrong number ")
    inp=input(" can i bill the amount yes or no : ")
    if inp=='yes':
        pass
        if finalamount!= 0:
            print(25*"=","--  MAHESH SUPER MARKET  -- ",25*"=")
            print(28*" "," Suryapet")
            print("Name : " ,name,30*"" ,"Date :", datetime.now)
            print(75*"-")
            print('Sno.',5*' ',"items" ,15*'',"quantity(kg)",20*'',"price")

            for i in range(len(pricelist)):
                print(i,8*' ',ilist[i],8*' ',qlist[i],5*' ',plist[i])
            print(50*' ',"totalprice",'Rs' ,totalprice)
            print("gst amount(5%)",45*" ",'rs',gst)
            print(75*'-')
            print(50*" ","finalamount ","Rs" ,finalamount)
            print(75*'-')
            print(25*'=',"Thanks for visiting",25*'=')




    
    




















