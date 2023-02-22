from flask import Flask
def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'asdasdasa1231212asdasd'
    
    from .views import views
    app.register_blueprint(views)
    return app

