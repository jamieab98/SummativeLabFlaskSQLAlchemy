#!/usr/bin/env python3
from app import app
from models import *
from datetime import date

with app.app_context():

    WorkoutExercises.query.delete()
    Workout.query.delete()
    Exercise.query.delete()

    pushups = Exercise(name="Push-Ups", category="Strength", equipment_needed=False)
    pullups = Exercise(name="Pull-Ups", category="Strength", equipment_needed=False)
    rowing = Exercise(name="Rowing", category="Cardio", equipment_needed=True)
    jumprope = Exercise(name="Jumping Rope", category="Cardio", equipment_needed=True)
    benchpress = Exercise(name="Benmch Press", category="Strength", equipment_needed=True)

    db.session.add_all([pushups, pullups, rowing, jumprope, benchpress])
    db.session.commit()

    workout1 = Workout(date=date(2026,3,12), duration_minutes=50, notes="Easiest workout of my life")
    workout2 = Workout(date=date(2026,3,11), duration_minutes=10, notes="At least I showed up")

    db.session.add_all([workout1, workout2])
    db.session.commit()

    link1 = WorkoutExercises(workout_id=1, exercise_id=1, reps=10, duration_seconds=35)
    link2 = WorkoutExercises(workout_id=1, exercise_id=2, reps=13, duration_seconds=40)
    link3 = WorkoutExercises(workout_id=1, exercise_id=4, reps=500, duration_seconds=200)
    link4 = WorkoutExercises(workout_id=2, exercise_id=5, reps=3, duration_seconds=12)
    link5 = WorkoutExercises(workout_id=2, exercise_id=4, reps=20, duration_seconds=7)
    link6 = WorkoutExercises(workout_id=2, exercise_id=2, reps=2, duration_seconds=15)

    db.session.add_all([link1, link2, link3, link4, link5, link6])
    db.session.commit()

    print("Database seeded")