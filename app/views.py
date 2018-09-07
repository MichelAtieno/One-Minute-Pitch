from flask import render_template
from . import main
from .forms import PitchForm
from .models import Pitch

#Views
@main.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''

    title = 'Pitch Haven'
    return render_template('index.html', title = title)

