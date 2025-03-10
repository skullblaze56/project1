import pytest
from application import create_app, db
from application.models.student import Student

@pytest.fixture
def app():
    app = create_app()
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    app.config['TESTING'] = True
    
    with app.app_context():
        db.create_all()
        yield app
        db.drop_all()

def test_new_student(app):
    """Test creating a new student"""
    with app.app_context():
        student = Student(name='John Doe', grade='A')
        db.session.add(student)
        db.session.commit()
        
        assert student.id is not None
        assert student.name == 'John Doe'
        assert student.grade == 'A'

def test_student_representation(app):
    """Test the string representation of a student"""
    with app.app_context():
        student = Student(name='Jane Smith', grade='B')
        assert str(student) == '<Student Jane Smith>' 