from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from blog.config import Config
db = SQLAlchemy()

def create_app(config_class=Config):

    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)
    
    from blog.user.routes import user
    #from blog.admin.routes import admin
    from blog.post.routes import post
    
    
    app.register_blueprint(user)
   # app.register_blueprint(admin)
    app.register_blueprint(post)
    
    return app 
    

