from application import create_app, db
from application.models.student import Student

app = create_app()

with app.app_context():
    db.create_all()
    
    # Add some sample data
    if not Student.query.first():
        students = [
            Student(name='John Doe', grade='A'),
            Student(name='Jane Smith', grade='B'),
            Student(name='Bob Johnson', grade='A-')
        ]
        db.session.add_all(students)
        db.session.commit()

print("Database initialized successfully!") 