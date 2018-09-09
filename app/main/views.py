from flask import render_template
from . import main
from ..models import Category,Pitch
from .forms import PitchForm

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
    

#@main.route('/user/<uname>&user_id')
#def User_Profile(uname, user_id):
   # user=User

    #new_pitch = Pitch

    #return render_template()

