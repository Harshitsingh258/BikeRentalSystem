class BikeRentShop:

    def __init__(self,stock):
       self.stock=stock
    def DisplayBike(self):
        print("Total No. of Bikes",self.stock)
    def RentForBike(self,q):

        if q<=0:
            print("Enter the Positive Value or Greater than 0")
        elif q>self.stock:
            print("Enter the Value(Less than Stocks)")

        else:
            self.stock=self.stock-q
            print("Total Prices=",q*500)
            print("Total Bikes=",self.stock)

while True:
    print("-----Bike Rent Shop-----")
    obj=BikeRentShop(150)
    uc=int(input('''
    1. Display Total no.of Bikes
    2. Rent Bike/s
    3. Exit    
    '''))
    if uc==1:
        obj.DisplayBike()
    elif uc==2:
        n=int(input("Enter the Quantity="))
        obj.RentForBike(n)
    else:
        break

