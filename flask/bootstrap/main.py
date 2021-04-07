from flask import Flask,render_template
from flask_script import Manager
from flask_bootstrap import Bootstrap


app = Flask(__name__)
manager = Manager(app)
bootstrap = Bootstrap(app)

@app.route('/user/<name>')
def user(name):
    return render_template('user.html',name=name)

@app.route('/user2/<name>')
def user2(name):
    return render_template('user2.html',name=name)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

if __name__ == '__main__':
    manager.run()