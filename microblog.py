from app import app, db, cli
from app.models import User, Post
from app.translate import translate

@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'Post': Post, 'translate': translate}