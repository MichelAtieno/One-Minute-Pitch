from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField
from wtforms.validators import Required

class PitchForm(FlaskForm):

    #category = StringField('Pitch Category',validators=[Required()])
    pitch_title = StringField('Pitch Title', validators=[Required()])
    pitch_post = TextAreaField('One Minute Pitch', validators=[Required()])
    submit = SubmitField('Submit')

class CommentForm(FlaskForm):
    comment = TextAreaField('Your Review or Comments', validators = [Required()])
    submit = SubmitField('Submit')