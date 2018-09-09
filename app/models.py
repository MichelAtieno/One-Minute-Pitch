from . import db
from werkzeug.security import generate_password_hash,check_password_hash

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255))
    email = db.Column(db.String(255))
    pass_secure = db.Column(db.String(255))

    pitches = db.relationship('Pitch', backref='user', lazy='dynamic')

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


    @classmethod
    def save_pitch(self):
       db.session.add(self)
       db.session.commit()

    @classmethod
    def get_pitch(cls,id):
        pitches = Pitch.query.filter_by(category_id = id).all()
        return pitches
        
        
        

