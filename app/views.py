from flask import render_template
from . import main
from .models import User, Pitch
from .forms import PitchForm

#Views
@main.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''

    title = 'Pitch Haven'
    return render_template('index.html', title = title)

#@main.route('/user/<uname>&user_id')
#def User_Profile(uname, user_id):
   # user=User

    #new_pitch = Pitch

    #return render_template()

