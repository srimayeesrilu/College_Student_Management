from flask import Flask, render_template, request, redirect, url_for
from models import db, Student

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///students.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

with app.app_context():
    db.create_all()

@app.route('/')
def index():
    students = Student.query.all()
    return render_template('index.html', students=students)

@app.route('/add', methods=['GET', 'POST'])
def add_student():
    if request.method == 'POST':
        if Student.query.get(request.form['student_id']):
            return "Student ID already exists!", 400

        student = Student(
            student_id=request.form['student_id'],
            age=int(request.form['age']),
            gender=request.form['gender'],
            major=request.form['major'],
            GPA=float(request.form['GPA']),
            course_load=float(request.form['course_load']),
            avg_course_grade=float(request.form['avg_course_grade']),
            attendance_rate=float(request.form['attendance_rate']),
            enrollment_status=request.form['enrollment_status'],
            lms_logins_past_month=float(request.form['lms_logins_past_month']),
            avg_session_duration_minutes=float(request.form['avg_session_duration_minutes']),
            assignment_submission_rate=float(request.form['assignment_submission_rate']),
            forum_participation_count=float(request.form['forum_participation_count']),
            video_completion_rate=float(request.form['video_completion_rate']),
            risk_level=request.form['risk_level']
        )
        db.session.add(student)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('add_student.html')

if __name__ == '__main__':
    app.run(debug=True)
