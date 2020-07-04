from flask import Flask
import os 
dir_path = os.path.dirname(os.path.realpath(__file__))
app = Flask(__name__,template_folder=os.path.join(dir_path,"templates"))
print(os.path.join(dir_path,"templates"))

from app import routes