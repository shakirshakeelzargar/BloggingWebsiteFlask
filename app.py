from flask import Flask ,render_template

application = Flask(__name__)

@application.route('/')
def index():
    return render_template('index.html') #asdasd

@application.route('/<string:name>')
def Func1(name):
    return "Welcome to " + name


@application.route('/Test',methods=['Get'])
def func2():
    return "Lololo"
    
if __name__ == "__main__":
    application.run(debug=True)