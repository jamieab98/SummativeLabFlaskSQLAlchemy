from flask import Flask, jsonify, request
from flask_migrate import Migrate
from marshmallow import ValidationError
from models import *
from schemas import *


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

migrate = Migrate(app, db)

db.init_app(app)

#Routes
@app.get("/workouts")
def get_workouts():
    workouts = Workout.query.all()
    results = WorkoutSchema(many=True).dump(workouts)
    return jsonify(results), 200

@app.get('/workouts/<int:id>')
def get_workout(id):
    workout = Workout.query.filter_by(id=id).first()
    if workout is None:
        return jsonify({'message': 'workout does not exist'}), 404
    result = WorkoutSchema().dump(workout)
    return jsonify(result), 200

@app.post('/workouts')
def create_workout():
    user_data = request.get_json()
    try:
        deserialized_data = WorkoutSchema().load(user_data)
    except ValidationError as err:
        return jsonify(err.messages), 400
    workout = Workout(**deserialized_data)
    db.session.add(workout)
    db.session.commit()
    result = WorkoutSchema().dump(workout)
    return jsonify(result), 201

@app.delete('/workouts/<int:id>')
def delete_workout(id):
    workout = Workout.query.filter_by(id=id).first()
    if workout is None:
        return jsonify({'message': 'searched workout does not exist'}), 404
    db.session.delete(workout)
    db.session.commit()
    return jsonify({'message': 'workout successfully deleted'}), 200

@app.get('/exercises')
def get_exercises():
    exercises = Exercise.query.all()
    results = ExerciseSchema(many=True).dump(exercises)
    return jsonify(results), 200

@app.get('/exercises/<int:id>')
def get_exercise(id):
    return jsonify({'message': f'placehold for showing exercise with id: {id}'})

@app.post('/exercises')
def create_exercise():
    return jsonify({'message': 'placeholder for post exercise'})

@app.delete('/exercises/<int:id>')
def delete_exercise(id):
    return jsonify({'message': f'placeholder for deleteing exercise with id: {id}'})

@app.post('/workouts/<int:workout_id>/exercises/<int:exercise_id>/workout_exercises')
def add_exercise_to_workout(workout_id, exercise_id):
    return jsonify({'message': f'placeholder for adding exercise {exercise_id} to workout {workout_id}'})

if __name__ == '__main__':
    app.run(port=5555, debug=True)