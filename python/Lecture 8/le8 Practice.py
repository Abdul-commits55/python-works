# class student:
#     def __int__(self,name,marks):
#         self.name=name
#         self.marks=marks

#     def get_avg(self):
#         sum =0
#         for val in self.marks:
#             sum += val
#         print("hi ",self.name,"your avg score is:",sum/3)

# s1= student("tony")
# s1.get_avg()

# # s1.name="ironman"
# # s1.get_avg()


#que2

class Account:
     def __init__(self,bal,acc):
        self.balance = bal
        self.account_no = acc
                        #debit method
     def debit(self,amount):
        self.balance -= amount
        print("Rs",amount,"was debited")
        print("total balance =",self.get_balance())

                    #
     def credit(self,amount):
        self.balance += amount
        print("Rs",amount,"was credited")
        print("total balance =",self.get_balance())

     def get_balance(self):
        return self.balance


acc1 =Account(20000,4321)
acc1.debit(5000)
acc1.credit(60000)