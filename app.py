from typing import final
from flask import Flask, escape, request, jsonify
from flask_cors import CORS
from werkzeug import exceptions
import numpy as np
import random
import conversion
import exercises
app = Flask(__name__)
CORS(app)

bench_1rm = 85
squat_1rm = 180
diddy_1rm = 220
ohp_1rm = 85

@app.route('/')
def home():
    return 'hello from flask'


@app.route('/api/plan/chest')
def plan_chest():
    chest_exercises = exercises.chest_list
    variations = exercises.chest_variations
    chosen_exercises = [*random.sample(chest_exercises.items(), k =4)]
    final_exercises = {}
    print(chosen_exercises)
    for exercise in chosen_exercises:
        num_reps = random.randint(1,12)
        percentage = conversion.conversion[f'{num_reps}']
        variations_to_add = [
            *random.sample(variations.items(), k=random.randint(1, 3))]
        difficulty = exercise[1]
        string_to_add = str()
        for variation in variations_to_add: 
            print('scaling difficulty by',variation[1])
            string_to_add += f'{variation[0]}-'
            difficulty *= variation[1]
        final_exercises[
            f'{string_to_add}{exercise[0]}']=f'3 sets at {np.round(difficulty*bench_1rm*percentage)}kg for {num_reps} reps'
        # final_exercises.append(f'{new_string} {exercise}')
    return jsonify(final_exercises)
@app.route('/api/plan/squat')
def plan_squat():
    squat_exercises = exercises.squat_list
    variations = exercises.squat_variations
    chosen_exercises = [*random.sample(squat_exercises.items(), k =4)]
    final_exercises = {}
    print(chosen_exercises)
    for exercise in chosen_exercises:
        variations_to_add = [
            *random.sample(variations.items(), k=random.randint(1, 3))]
        difficulty = exercise[1]
        string_to_add = str()
        for variation in variations_to_add: 
            print('scaling difficulty by',variation[1])
            string_to_add += f'{variation[0]}-'
            difficulty *= variation[1]
        final_exercises[
            f'{string_to_add}{exercise[0]}']=f'{difficulty*squat_1rm}kg'
        # final_exercises.append(f'{new_string} {exercise}')
    return jsonify(final_exercises)


@app.errorhandler(exceptions.NotFound)
def handle_404(err):
    return jsonify({"message": f'Oops...{err}'}), 404


@app.errorhandler(exceptions.InternalServerError)
def handle_500(err):
    return jsonify({"message": f'Oops...{err}'}), 500


if __name__ == '__main__':
    app.run(debug=True)
