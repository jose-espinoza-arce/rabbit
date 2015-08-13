from django.core.mail import get_connection
from django.core.mail.message import EmailMultiAlternatives


def send_mail(subject, message, from_email, to_email, recipient_list,
              fail_silently=False, auth_user=None, auth_password=None,
              connection=None, html_message=None):

    connection = connection or get_connection(username=auth_user,
                                              password=auth_password,
                                              fail_silently=fail_silently)
    mail = EmailMultiAlternatives(subject, message, from_email, to_email, recipient_list,
                                  connection=connection)
    if html_message:
        mail.attach_alternative(html_message, 'text/html')

    return mail.send()
