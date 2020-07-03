from flask import Flask,render_template,redirect,request
from flask_sqlalchemy import SQLAlchemy
import requests
import json
from datetime import datetime

# response = json.loads(requests.get("https://raw.githubusercontent.com/shakirshakeelzargar/practice-python/master/assets/fd-reminder.json").text)

application = Flask(__name__)

application.config['SQLALCHEMY_DATABASE_URI']='sqlite:///posts.db'
db=SQLAlchemy(application)

class BlogPost(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    title= db.Column(db.Text(),nullable=False)
    content=db.Column(db.Text(),nullable=False)
    author=db.Column(db.String(100),default='N/A')
    date_post=db.Column(db.DateTime,default=datetime.utcnow())
    
    def __repr__(self):
        return str(id)


# all_posts=[{'Sal':'Mr','Name':'Ashir','Prof':'Director'},{'Sal':'Miss','Name':'Ruby'}]
@application.route('/')
def index():
    return "Test" #asdasd

@application.route('/Var/<string:name>')
def Func1(name):
    return "Welcome to " + name

@application.route('/Test',methods=['Get'])
def func2():
    return "Lololo"

@application.route('/Posts',methods=['GET','POST'])
def func_post():
    if request.method=='POST':
        new_post = BlogPost(title=request.form['title'],content=request.form['content'],author=request.form['author'])
        db.session.add(new_post)
        db.session.commit()
        return redirect('/Posts')
    else:
        all_posts = BlogPost.query.all()
        return render_template('Posts.html',posts=all_posts)

if __name__ == "__main__":
    application.run(debug=True)