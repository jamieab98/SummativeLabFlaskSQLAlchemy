Project Title: Flask SQLAlchemy Summative Lab
Project Description: The backend program that allows a user to create a workout, create an exercise, and log an exercise with a workout

Installation Instructions:
    Packages to install:
        flask
        flask-migrate
        flask-sqlalchemy
        wekzeug
        marshmallow
    
    Seeding the database:
        Navigate to the server folder
        In the terminal, run:
            python3 seed.py

Starting the Server:
    Navigate to the server folder
    In the terminal, run:
        python3 app.py

Activate the shell to manually search through the database
    Navigate to the server folder
    In the terminal, run:
        flask shell
    In the terminal, you may now query the database
        
API Endpoints:
    GET /workouts
        Obtain all the objects from the Workout class
    
    GET /workouts/id
        Obtain the object from the Wokout class that matches the id in the URL
    
    POST /workouts
        Create a new object using the Workout class and store it in the database
    
    DELETE /workouts/id
        Remove the object from the Workout class that matches the id in the URL
    
    GET /exercises
        Obtain all the object from the Exercise class
    
    GET /exercises/id
        Obtain the object from the Exercise class that matches the id in the URL
    
    POST /exercises
        Create a new object using the Exercise class and store it in the database
    
    DELETE /exercises/id
        Remove the object from the Exercise class that matches the id in the URL
    
    POST /workouts/workout_id/exercises/exercise_id/workout_exercises
        Create a new object using the WorkoutExercises class and store it in the databse