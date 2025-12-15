""" 02 Проверка платежей

Доработайте систему:
Создайте пользовательское исключение InvalidPaymentError.
В каждом платёжном классе метод pay(amount) должен проверять сумму:
Если сумма меньше или равна нулю, выбрасывать InvalidPaymentError.
Иначе проводить платёж.
"""

class PaymentProcessor():
    pass


class PaypalPayment():
    pass


class CreditCardPayment():
    pass


if __name__ == "__main__":
    try:
        paypal = PaypalPayment()
        paypal.pay(100)

        card = CreditCardPayment()
        card.pay(-50)  # вызовет ошибку
    except InvalidPaymentError as e:
        print("Payment error:", e)


# Paid 100 via PayPal
# Payment error: Amount must be greater than zero
