from django.core.mail import send_mail
from .models import Order

def order_created(order_id):
    order = Order.objects.get(id=order_id)
    subject = 'Order nr. {}'.format(order.id)
    message = 'Dear {}, \n\nYour have successfully placed an order.Your order id is {}.'.format(order.first_name, order.id)

    mail_sent = send_mail(subject, message, 'admin@myshop.com', [order.email])

    return mail_sent
