from django.core.mail import EmailMessage
from books.models import BookUser
from django.utils import timezone


def send_mail_to(title, user_mail, content):
    message = EmailMessage(
        title,
        content,
        'mailneuna@gmail.com',
        [user_mail],
    )
    message.send()

def deadline_end():
    users = BookUser.objects.filter(deadline__lt=timezone.now())
    print('dzialam')
    for user in users:
        send_mail_to('cron', user.user.username, 'ejże!')