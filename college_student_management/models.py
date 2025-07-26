from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Student(db.Model):
    student_id = db.Column(db.String(10), primary_key=True)
    age = db.Column(db.Integer)
    gender = db.Column(db.String(10))
    major = db.Column(db.String(100))
    GPA = db.Column(db.Float)
    course_load = db.Column(db.Float)
    avg_course_grade = db.Column(db.Float)
    attendance_rate = db.Column(db.Float)
    enrollment_status = db.Column(db.String(20))
    lms_logins_past_month = db.Column(db.Float)
    avg_session_duration_minutes = db.Column(db.Float)
    assignment_submission_rate = db.Column(db.Float)
    forum_participation_count = db.Column(db.Float)
    video_completion_rate = db.Column(db.Float)
    risk_level = db.Column(db.String(20))
