# utils.py


# utils.py

from django.core.mail import send_mail

def send_password_reset_email(email, reset_token):
    subject = 'Password Reset'
    message = f'Use this link to reset your password: https://dtest6366@gmail.com/reset-password?token={reset_token}'
    send_mail(subject, message, 'dtest6366@gmail.com', [email])

