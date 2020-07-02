from flask import Flask ,render_template
import requests
import json

response = json.loads(requests.get("https://raw.githubusercontent.com/shakirshakeelzargar/practice-python/master/assets/fd-reminder.json").text)

application = Flask(__name__)

all_posts=response
# all_posts=[{'Sal':'Mr','Name':'Ashir','Prof':'Director'},{'Sal':'Miss','Name':'Ruby'}]
@application.route('/')
def index():
    return render_template('index.html') #asdasd

@application.route('/Var/<string:name>')
def Func1(name):
    return "Welcome to " + name

@application.route('/Test',methods=['Get'])
def func2():
    return "Lololo"

@application.route('/Posts',methods=['Get'])
def func_post():
    return render_template('Posts.html',posts=all_posts)

if __name__ == "__main__":
    application.run(debug=True)