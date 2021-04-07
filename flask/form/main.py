from flask import Flask,render_template,session,redirect,url_for,flash
from flask_script import Manager
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField,SelectField,FileField
from wtforms.validators import DataRequiredz

app = Flask(__name__)
app.config['SECRET_KEY'] = 'hard to guess string'
manager = Manager(app)
bootstrap = Bootstrap(app)

class NameForm(FlaskForm):
    name = StringField('What is your name?', validators=[DataRequired()])
    language = SelectField(u'Programming Language', choices=[('cpp', 'C++'), ('py', 'Python'), ('text', 'Plain Text')])
    image        = FileField(u'Image File')
    submit = SubmitField('Submit')

class TestForm(FlaskForm):
    # name = StringField('What is your name?', validators=[DataRequired()])
    language = SelectField(u'Programming Language', choices=[('cpp', 'C++'), ('py', 'Python'), ('text', 'Plain Text')])
    image        = FileField(u'Image File')
    # submit = SubmitField('Submit')

@app.route('/',methods=['GET','POST'])
def index():
    name = None
    form = NameForm()
    form2 = TestForm()
    if form.validate_on_submit():
        old_name = session.get('name')
        if old_name is not None and old_name != form.name.data:
            flash('looks like you have change the name!')
        session['name'] = form.name.data
        form.name.data = ''
        return redirect(url_for('index'))
    return render_template('index.html',form=form,form2=form2,name=session.get('name'))

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
