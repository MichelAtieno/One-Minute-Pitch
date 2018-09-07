class User:
    '''
    User class that defines users
    '''
    def __init__(self,id,username,email):
        self.id = id
        self.username = username
        self.email = email


class Pitch:
    '''
    Pitch class that defines pitch categories
    '''
    all_pitches = []

    def __init__ (self,id,category,pitch):
        self.id = id
        self.category = category
        self.pitch = pitch

    @classmethod
    def save_pitch(self):
        Pitch.all_pitches.append(self)

    @classmethod
    def clear_pitch(cls):
        Pitch.all_pitches.clear()

    @classmethod
    def get_pitch(cls,id):

        response = []

        for pitch in cls.all_pitches:
            if pitch.user_id == id:
                response.append(pitch)

        return response
        

