from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import validates
db = SQLAlchemy()

#Models
class Exercise(db.Model):
    __tablename__ = 'exercises'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    category = db.Column(db.String)
    equipment_needed = db.Column(db.Boolean)

class Workout(db.Model):
    __tablename__ = 'workouts'

    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date)
    duration_minutes = db.Column(db.Integer)
    notes = db.Column(db.Text) #should this be db.String?

workout_exercises = db.Table('WorkoutExercises', 
                           db.Column('id', db.Integer, primary_key=True),
                           db.Column('workout_id', db.Integer, db.ForeignKey('workouts.id')),
                           db.Column('exercise_id', db.Integer, db.ForeignKey('exercises.id')),
                           db.Column('reps', db.Integer),
                           db.Column('duration_seconds', db.Integer)
                           )