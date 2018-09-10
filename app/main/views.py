from flask import render_template,request, redirect, url_for, flash,abort
from . import main
from ..models import User,Pitch, Comment
from .forms import PitchForm, CommentForm, UpdateProfile
from flask_login import login_required, current_user
from .. import db,photos
import markdown2

#Views
@main.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''


    title = 'Pitch Haven'
    return render_template('index.html', title = title)

    
@main.route('/pitch', methods= ['GET', 'POST'])
@login_required
def get_new_pitch():
    '''
    View Category that returns a form to create pitch
    '''
    pitch_form = PitchForm()
    
    if pitch_form.validate_on_submit():
        pitch_title = pitch_form.pitch_title.data
        new_category = pitch_form.pitch_post.data

        #pitch instance
        new_pitch = Pitch(pitch_description=pitch_title, pitch_category=new_category, user = current_user)
        new_pitch.save_pitch()
        
        return redirect(url_for('main.get_new_pitch'))

    all_pitches = Pitch.get_all_pitches()
    title = 'Pitches | One Minute Pitch'
   
    return render_template('pitch.html', title = title, pitch_form= pitch_form, pitches=all_pitches)

@main.route('/category/<new_category>')
def category(new_category):
    new_category  = Pitch.get_category(new_category)

    title = f'{new_category} category | One Minute Pitch'

    return render_template('category.html', title=title, category=new_category)


main.route('/pitch/comment/new/<int:id>', methods = ['GET','POST'])
@login_required
def new_comment(id):
    '''
    View Category that returns a form to create new comment
    '''
    form = CommentForm()
    pitch = Pitch.query.filter_by(id = id).first()
    if form.validate_on_submit():
        comment = form.comment.data

        # review instance
        new_comment = Comment(pitch_id = pitch.id, post_comment = comment, user = current_user)

        # save review 
        new_comment.save_comment()
        return redirect(url_for('.comments', id = pitch.id ))

    title = f'{pitch.title} comment'
    return render_template('new_comment.html', title = title, comment_form = form, pitch = pitch)

@main.route('/pitch/comments/<int:id>')
def comments(id):
    '''
    view category that returns all comments for a pitch
    '''
    pitch = Pitch.query.get(id)
    comment = Comment.get_comments(pitch.id)
    title = f'{pitch.title} comment'

    return render_template('comments.html', title = title, pitch = pitch, comment= comment)

@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(username = uname).first()

    if user is None:
        abort(404)

    return render_template("profile/profile.html", user = user)

@main.route('/user/<uname>/update',methods = ['GET','POST'])
@login_required
def update_profile(uname):
    user = User.query.filter_by(username = uname).first()
    if user is None:
        abort(404)

    form = UpdateProfile()

    if form.validate_on_submit():
        user.bio = form.bio.data

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('.profile',uname=user.username))

    return render_template('profile/update.html',form =form)

@main.route('/user/<uname>/update/pic',methods= ['POST'])
@login_required
def update_pic(uname):
    user = User.query.filter_by(username = uname).first()
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.profile_pic_path = path
        db.session.commit()
    return redirect(url_for('main.profile',uname=uname))

