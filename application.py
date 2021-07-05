from flask import Flask
application = Flask(__name__)
app = application


@application.route('/')
def hello_world():
    return 'This is my project for testing. This is really test project, please do not copy'
