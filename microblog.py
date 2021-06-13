#!/usr/bin/env python3.6

from app import create_app, db, cli
from app.models import User, Post, Message, Notification, Task
from app.translate import translate
from sqlalchemy.inspection import inspect

app = create_app()
cli.register(app)

@app.shell_context_processor
def make_shell_context():
    def get_columns(table):
        return [column.name for column in inspect(table).c]
    return {'db': db, 'User': User, 'Post': Post, 'translate': translate, 
            'Message': Message, 'get_columns': get_columns, 
            'Notification': Notification, 'Task': Task}