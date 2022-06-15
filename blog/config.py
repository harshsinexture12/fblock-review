import os 

class Config:
      SECRET_KEY = 'fsdgh45rfghersd'
    
      SQLALCHEMY_DATABASE_URI = "postgresql://postgres:password@localhost:5432/kblog"

      SQLALCHEMY_TRACK_MODIFICATIONS = False

      UPLOAD_FOLDER = 'blog/static/images/'
      
    

