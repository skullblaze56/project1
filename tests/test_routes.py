import pytest
import json
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

@pytest.fixture
def client(app):
    return app.test_client()

@pytest.fixture
def sample_student(app):
    with app.app_context():
        student = Student(name='Test Student', grade='A')
        db.session.add(student)
        db.session.commit()
        student_id = student.id  # Store the ID
        return student_id  # Return just the ID

def test_index_route(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b'Student Records' in response.data

def test_add_student(client):
    response = client.post('/student', 
        json={'name': 'John Doe', 'grade': 'B'},
        content_type='application/json')
    assert response.status_code == 200
    data = json.loads(response.data)
    assert data['message'] == 'Student added successfully'

def test_get_student(client, sample_student):
    response = client.get(f'/student/{sample_student}')  # Use the ID directly
    assert response.status_code == 200
    data = json.loads(response.data)
    assert data['name'] == 'Test Student'
    assert data['grade'] == 'A' 