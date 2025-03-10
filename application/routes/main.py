from flask import Blueprint, render_template, request, jsonify
from application.models.student import Student
from application import db

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def index():
    students = Student.query.all()
    return render_template('students.html', students=students)

@main_bp.route('/student', methods=['POST'])
def add_student():
    data = request.json
    new_student = Student(name=data['name'], grade=data['grade'])
    db.session.add(new_student)
    db.session.commit()
    return jsonify({'message': 'Student added successfully'})

@main_bp.route('/student/<int:id>', methods=['GET'])
def get_student(id):
    student = Student.query.get_or_404(id)
    return jsonify({
        'id': student.id,
        'name': student.name,
        'grade': student.grade
    }) 