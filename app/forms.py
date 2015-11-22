from flask.ext.wtf import Form
from wtforms import StringField, SubmitField
from wtforms.validators import Required, URL

class URLForm(Form):
    url = StringField('URL', validators=[Required(), URL()])
    submit = SubmitField('Shorten link')
