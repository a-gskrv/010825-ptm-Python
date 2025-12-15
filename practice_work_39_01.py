""" 01 Онлайн-платёжные системы

Создайте абстрактный класс PaymentProcessor.
В классе должен быть метод pay(amount).
Реализуйте два класса:
- PaypalPayment, который печатает "Paid <amount> via PayPal".
- CreditCardPayment, который печатает "Paid <amount> via Credit Card".
"""

class PaymentProcessor():
    pass


class PaypalPayment():
    pass



class CreditCardPayment():
    pass



if __name__ == "__main__":
    paypal = PaypalPayment()
    paypal.pay(100)

    card = CreditCardPayment()
    card.pay(250)


# Paid 100 via PayPal
# Paid 250 via Credit Card
