from flask import render_template, redirect, url_for
from . import main
from ..models import User,Category,Pitch
from .forms import PitchForm
from flask_login import login_required

#Views
@main.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''

    title = 'Pitch Haven'
    return render_template('index.html', title = title)

@main.route('/category/<int:id>')
def get_category(id):
    '''
    View category function that returns pitches of category
    '''
    category = Category.query.get(id)
    pitch_title = f'{category.category_name}'
    pitch = Pitch.get_pitch(category.id)

    return render_template('.category.html', pitch_title =pitch_title, category= category, pitch= pitch)
    
@main.route('/category/pitch/new/<int:id>', methods= ['GET', 'POST'])
def get_new_pitch():
    '''
    View Category that returns a form to create pitch
    '''
    pitch_form = PitchForm()
    category = Category.query.filter_by(id = id).first()
    if pitch_form.validate_on_submit():
        pitch_title = pitch_form.pitch_title.data
        pitch_post = pitch_form.pitch_post.data

    #pitch instance
    new_pitch = Pitch(category_id = category.id, pitch_title = pitch_title, pitch_post = pitch_post)
    new_pitch.save_pitch()
    return redirect(url_for('.category', id = category.id))
   
    pitch_title = f'{category.category_name}'
    return render_template('new_pitch.html', pitch_title = pitch_title , pitch_form= pitch_form, category= category)

