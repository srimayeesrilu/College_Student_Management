import csv
from flask import Flask
from models import db, Student

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///students.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

def to_float(value):
    try:
        return float(value)
    except:
        return None

def to_int(value):
    try:
        return int(float(value))
    except:
        return None

with app.app_context():
    db.create_all()
    with open('college_student_management_data.csv', encoding='utf-8-sig') as f:
        reader = csv.DictReader(f)
        for row in reader:
            if not row["student_id"]:
                continue

            if Student.query.get(row["student_id"]):
                continue  # Skip duplicates

            student = Student(
                student_id=row["student_id"],
                age=to_int(row["age"]),
                gender=row["gender"],
                major=row["major"],
                GPA=to_float(row["GPA"]),
                course_load=to_float(row["course_load"]),
                avg_course_grade=to_float(row["avg_course_grade"]),
                attendance_rate=to_float(row["attendance_rate"]),
                enrollment_status=row["enrollment_status"],
                lms_logins_past_month=to_float(row["lms_logins_past_month"]),
                avg_session_duration_minutes=to_float(row["avg_session_duration_minutes"]),
                assignment_submission_rate=to_float(row["assignment_submission_rate"]),
                forum_participation_count=to_float(row["forum_participation_count"]),
                video_completion_rate=to_float(row["video_completion_rate"]),
                risk_level=row["risk_level"]
            )
            db.session.add(student)
        db.session.commit()
        print("✅ Data imported successfully.")
