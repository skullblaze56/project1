from application import db

class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    grade = db.Column(db.String(2), nullable=False)
    
    def __repr__(self):
        return f'<Student {self.name}>' 