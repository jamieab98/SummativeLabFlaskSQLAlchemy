from flask import Flask, jsonify
from flask_migrate import Migrate

from models import *

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

migrate = Migrate(app, db)

db.init_app(app)

#Routes
@app.route("/workouts")
def get_workouts():
    workouts = Workout.query.all()
    workout_list = []
    for workout in workouts:
        workout_dict = {'id': workout.id, 'date': workout.date.isoformat(), 'duration in minutes': workout.duration_minutes, 'notes': workout.notes}
        workout_list.append(workout_dict)
    return jsonify(workout_list), 200

@app.route('/workouts/<int:id>')
def get_workout(id):
    workout = Workout.query.filter_by(id=id).first()
    if workout is None:
        return jsonify({'message': 'workout does not exist'}), 404
    exercises = workout.workoutexercises
    exercises_list = []
    for exercise in exercises:
        exercise_dict = {'id': exercise.id, 'reps': exercise.reps, 'duration': exercise.duration_seconds, 'name': exercise.exercise.name}
        exercises_list.append(exercise_dict)
    return jsonify(exercises_list), 200

if __name__ == '__main__':
    app.run(port=5555, debug=True)