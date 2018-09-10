from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SelectField,SubmitField
from wtforms.validators import Required

class PitchForm(FlaskForm):

    #category = StringField('Pitch Category',validators=[Required()])
    pitch_title = TextAreaField('Pitch Title', validators=[Required()])
    pitch_post = SelectField('Category', choices=[('Business-Pitch','Business Pitch'),('Product-Pitch','Product Pitch'),('Academic-Pitch','Academic Pitch'),('Technology','Technology'),('Health','Health')],validators=[Required()])
    submit = SubmitField('Submit')

class CommentForm(FlaskForm):
    comment = TextAreaField('Your Comments', validators = [Required()])
    submit = SubmitField('Submit')

class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about you.',validators = [Required()])
    submit = SubmitField('Submit')