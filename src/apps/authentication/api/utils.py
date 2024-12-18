import threading

from django.core.mail import EmailMessage


class EmailThread(threading.Thread):
    """
    Thread for sending an email
    """

    def __init__(self, email):
        self.email = email
        threading.Thread.__init__(self)

    def run(self):
        self.email.send()


class EmailSender:
    """
    Class with method that send an email
    """

    @staticmethod
    def send_email(data):
        email = EmailMessage(subject=data["email_subject"], body=data["email_body"], to=[data["to_email"]])
        EmailThread(email).start()
