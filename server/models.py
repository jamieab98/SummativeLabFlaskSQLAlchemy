from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import validates
from datetime import date
db = SQLAlchemy()

#Models
class WorkoutExercises(db.Model):
    __tablename__ = 'workout_exercises'

    id = db.Column(db.Integer, primary_key=True)
    workout_id = db.Column(db.Integer, db.ForeignKey('workouts.id'))
    exercise_id = db.Column(db.Integer, db.ForeignKey('exercises.id'))
    reps = db.Column(db.Integer)
    duration_seconds = db.Column(db.Integer)

    @validates('reps')
    def validates_reps(self, key, reps):
        if reps is None:
            raise ValueError("Please enter rep count")
        if reps <= 0:
            raise ValueError("Rep value must be greater than 0")
        return reps
    
    @validates('duration_seconds')
    def validates_duration_seconds(self, key, duration_seconds):
        if duration_seconds is None:
            raise ValueError("Please enter duration in seconds")
        if duration_seconds <= 0:
            raise ValueError("Duration values must be more than 0 seconds")
        return duration_seconds

    workout = db.relationship('Workout', back_populates='workoutexercises')
    exercise = db.relationship('Exercise', back_populates='workoutexercises')

class Exercise(db.Model):
    __tablename__ = 'exercises'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    category = db.Column(db.String)
    equipment_needed = db.Column(db.Boolean)

    @validates('name')
    def validates_name(self, key, name):
        if name is None or name == "":
            raise ValueError("Exercise name is required")
        return name

    workoutexercises = db.relationship('WorkoutExercises', back_populates='exercise')

class Workout(db.Model):
    __tablename__ = 'workouts'

    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date)
    duration_minutes = db.Column(db.Integer)
    notes = db.Column(db.Text)

    @validates('date')
    def validates_date(self, key, value):
        if value is None:
            raise ValueError("Please provide a date")
        if value > date.today():
            raise ValueError("Date cannot be beyond today's date")
        return value
    
    @validates('notes')
    def validates_notes(self, key, notes):
        if notes and len(notes) > 1024:
            raise ValueError("Please provide a shorter note")
        return notes

    workoutexercises = db.relationship('WorkoutExercises', back_populates='workout')