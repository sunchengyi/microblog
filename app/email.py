from threading import Thread

from flask import current_app
from flask_mail import Message
from flask_babel import _

from app import mail

def send_async_email(app, msg):
    with app.app_context():
        mail.send(msg)

def send_email(subject, sender, recipients, text_body, html_body):
    msg = Message(subject, sender=sender, recipients=recipients)
    msg.body = text_body
    msg.html = html_body
    # here, "current_app._get_current_object()" is necessary,
    # since "current_app" is a proxy object and only works in a thred handling 
    # the client request.
    Thread(target=send_async_email, 
           args=(current_app._get_current_object(), msg)).start()