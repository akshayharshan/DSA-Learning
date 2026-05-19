from abc import ABC, abstractmethod

class Payment(ABC):
    @abstractmethod
    def pay(amount):
        pass



class UPIPayment(Payment):
    def pay(self,amount):
        return f"Paid {amount} using UPI"
class CardPayment(Payment):
    def pay(self,amount):
        return f"Paid {amount} using Card"
class PayPalPayment(Payment):
    def pay(self,amount):
        return f"Paid {amount} using Paypal"
    


class PaymentFactory:

    @staticmethod
    def create_payment(payment_method):
        
        if payment_method == "upi":
            return UPIPayment()
        if payment_method == "card":
            return CardPayment()
        if payment_method == "paypal":
            return PayPalPayment()
        



payment = PaymentFactory.create_payment("card")
print(payment.pay(500))



class UserService:
    def __init__(self,db):
        self.db = db

    

class MysqlDatabase:
    def __init__(self):



mysql = MysqlDatabase()
UserService(mysql)
        