from flask import Blueprint, jsonify, request
import numpy as np
import random
from . import conversion
from . import exercises
from werkzeug import exceptions
main = Blueprint('main',__name__)
bench_1rm = 85
squat_1rm = 180
diddy_1rm = 220
ohp_1rm = 85
one_rep_maxes = {
    'bench':85,
    'squat':180,
    'diddy':220,
    'ohp':85
}
@main.route('/')
def home():
    return 'hello from flask'


@main.post('/api/plan/bench')
def plan_chest():
    data = request.get_json()
    one_rep_max = int(data['oneRepMax'])
    chest_exercises = exercises.chest_list
    variations = exercises.chest_variations
    chosen_exercises = [*random.sample(chest_exercises.items(), k =4)]
    final_exercises = []
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
        final_exercises.append(
            {"name":f'{string_to_add}{exercise[0]}',
            "sets": 3,
            "reps": num_reps,
            "weight": f'{np.round(difficulty*one_rep_max*percentage)}kg' })
            
    
    return jsonify(final_exercises)
@main.post('/api/plan/squat')
def plan_squat():
    data = request.get_json()
    one_rep_max = int(data['oneRepMax'])
    squat_exercises = exercises.squat_list
    variations = exercises.squat_variations
    chosen_exercises = [*random.sample(squat_exercises.items(), k =4)]
    final_exercises = []
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
        final_exercises.append(
            {"name":f'{string_to_add}{exercise[0]}',
            "sets": 3,
            "reps": num_reps,
            "weight": f'{np.round(difficulty*one_rep_max*percentage)}kg' })
            
    
    return jsonify(final_exercises)
@main.post('/api/plan/diddy')
def plan_diddy():
    data = request.get_json()
    one_rep_max = int(data['oneRepMax'])
    diddy_exercises = exercises.diddy_list
    variations = exercises.diddy_variations
    chosen_exercises = [*random.sample(diddy_exercises.items(), k =4)]
    final_exercises = []
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
        final_exercises.append(
            {"name":f'{string_to_add}{exercise[0]}',
            "sets": 3,
            "reps": num_reps,
            "weight": f'{np.round(difficulty*one_rep_max*percentage)}kg' })
            
    
    return jsonify(final_exercises)
@main.post('/api/plan/ohp')
def plan_ohp():
    data = request.get_json()
    one_rep_max = int(data['oneRepMax'])
    ohp_exercises = exercises.ohp_list
    variations = exercises.ohp_variations
    chosen_exercises = [*random.sample(ohp_exercises.items(), k =4)]
    final_exercises = []
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
        final_exercises.append(
            {"name":f'{string_to_add}{exercise[0]}',
            "sets": 3,
            "reps": num_reps,
            "weight": f'{np.round(difficulty*one_rep_max*percentage)}kg' })
            
    
    return jsonify(final_exercises)


@main.errorhandler(exceptions.NotFound)
def handle_404(err):
    return jsonify({"message": f'Oops...{err}'}), 404


@main.errorhandler(exceptions.InternalServerError)
def handle_500(err):
    return jsonify({"message": f'Oops...{err}'}), 500