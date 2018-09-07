from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField
from wtforms.validators import Required

class PitchForm(FlaskForm):

    #category = StringField('Pitch Category',validators=[Required()])
    pitch = TextAreaField('One minute pitch', validators=[Required()])
    submit = SubmitField('Submit')