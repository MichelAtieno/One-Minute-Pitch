from . import db, login_manager
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(UserMixin,db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255))
    email = db.Column(db.String(255))
    bio = db.Column(db.String(255))
    profile_pic_path = db.Column(db.String())
    pass_secure = db.Column(db.String(255))

    pitches = db.relationship('Pitch', backref='user', lazy='dynamic')
    comments = db.relationship('Comment', backref = 'user', lazy = "dynamic")

    @property
    def password(self):
        raise AttributeError('You cannot read the password attribute')

    @password.setter
    def password(self, password):
        self.pass_secure = generate_password_hash(password)


    def verify_password(self,password):
        return check_password_hash(self.pass_secure,password)

    def __repr__(self):
        return f'User {self.username}'

class Category(db.Model):
    __tablename__ = 'categories'

    id = db.Column(db.Integer,primary_key = True)
    category_name = db.Column(db.String(255), index= True)

    pitches = db.relationship('Pitch', backref='category', lazy='dynamic')

    @classmethod
    def get_pitch_categories(cls):
        categories = Category.query.all()
        return categories


class Pitch(db.Model):
    __tablename__ = 'pitches'

    id = db.Column(db.Integer,primary_key = True)
    pitch_description = db.Column(db.String())
    pitch_category = db.Column(db.String(255))

    user_id = db.Column(db.Integer,db.ForeignKey('users.id'))
    category_id = db.Column(db.Integer,db.ForeignKey('categories.id'))
    comments = db.relationship('Comment', backref = 'pitch', lazy = "dynamic")


    @classmethod
    def save_pitch(self):
       db.session.add(self)
       db.session.commit()

    @classmethod
    def get_pitch(cls,id):
        pitches = Pitch.query.filter_by(category_id = id).all()
        return pitches

class Comment(db.Model):
    __tablename__ = 'comments'

    id = db.Column(db.Integer, primary_key = True)
    post_comment = db.Column(db.String(255), index = True)
    #time = db.Column(db.DateTime, default = datetime.utcnow)

    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    pitch_id = db.Column(db.Integer, db.ForeignKey('pitches.id'))

    def save_comment(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_comments(cls, id):
        comments = Comment.query.filter_by(pitch_id=id).all()
        return comments


        
        
        

