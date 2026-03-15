from marshmallow import fields, Schema, validates

class ExerciseSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(dump_only=True)
    category = fields.Str(dump_only=True)
    equipment_needed = fields.Bool(dump_only=True)

class WorkoutSchema(Schema):
    id = fields.Int(dump_only=True)
    date = fields.Date(required=True)
    duration_minutes = fields.Int(required=True)
    notes = fields.Str()

    workoutexercises = fields.Nested(lambda: WorkoutExercisesSchema(), exclude=('workout',), many=True)

class WorkoutExercisesSchema(Schema):
    id = fields.Int(dump_only=True)
    workout_id = fields.Int(dump_only=True)
    exercise_id = fields.Int(dump_only=True)
    reps = fields.Int(required=True)
    duration_seconds = fields.Int()

    exercise = fields.Nested(ExerciseSchema())

    @validates('reps')
    def validates_reps(self, key, reps):
        if reps <= 0:
            raise ValueError("The number of reps must be positive")
        if reps is None:
            raise ValueError("Must input number of reps")
        return reps
    
    @validates('duration_seconds')
    def validates_duration(self, key, duration_seconds):
        if duration_seconds is not None and duration_seconds <= 0:
            raise ValueError("Duration of exercise must be positive")
        return duration_seconds