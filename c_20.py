# Polimorfism in Python Oriented to Objects
# Polimorfism is a principle that allow that
# derivative classes of the same superclass
# have the same methods (with the same signiture)
# but different behaviors.
# Method Signiture Same name and parameters amount
# (return is not part of the signiture)
# Opinion + principles importants:
# Method Signiture: name, parameters and same return
# SO"L"ID
# Liskov Substitution Principle
# Objects of a superclass must be replaceble
# for objects of a subclass without broke the application.
# Overload is not allowed in python
# Override is allowed in python
from abc import ABC, abstractmethod

class Notification:
    def __init__(self, msg) -> None:
        self.msg = msg
    
    @abstractmethod
    def send(self) -> bool:
        ...
    

class EmailNotification(Notification):
    def send(self) -> bool:
        print('Sending Email: ', self.msg)

        return True


class SMSNotification(Notification):
    def send(self) -> bool:
        print("Sending SMS: ", self.msg)

        return True


def do_notification(notification: Notification):
    notification_sent = notification.send()

    if notification_sent:
        print("Notification sent")
    
    else:
        print("Notification didn't send")


email_notifi = "Test email"
do_notification(EmailNotification(email_notifi))

sms_notif = "Test SMS"
do_notification(SMSNotification(sms_notif))