from django.dispatch import receiver,Signal
notification = Signal(providing_args=['request', 'user'])
@receiver(notification)
def show_nartification(sender, **kwargs):
    print("Notification received")
    print("Sender",sender)
    print("kwargs",kwargs)
    print("Notification sent to: ", kwargs['user'])