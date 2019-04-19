import os
import sys
base_directory = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
base_save_dir = f'{base_directory}/data/lstm_files/post_grade/'

sys.path.append(f'{base_directory}/training_utils/')
sys.path.append(f'{base_directory}/models/char-rnn-tensorflow/')
sys.path.append(f'{base_directory}/types/')

from pprint import pprint
import climb_loader
import sample
import grade
from climbset import Climbset


def grade_output(score):
    # Given a sample of the networks output convert it to type Grade
    # if the grade is invalid just fill the value with None
    try:
        return grade.Grade(score[-1])
    except ValueError:
        return None


def grade_everything(climbs):
    # Convert each climb from the data type Climb, to a string without the grade on the end
    seed_strings = [climb.moves_nn_string()+Climbset.get_grade_seperator() for climb in climbs]

    # Generate the grade character for every climb in the list
    model_output = sample.sample_many(base_save_dir, 1, seed_strings)

    # Convert the network output into the Grade type
    model_grades = list(map(grade_output, model_output))

    pprint(list(zip(model_output, model_grades)))

    # Update the climbs with the grade value
    for climb, nn_grade in zip(climbs, model_grades):
        climb.nn_grade = nn_grade

    return climbs

if __name__ == '__main__':
    # Load all the climbs
    all_climbs = climb_loader.load_all_as_climbset()

    # Grade and keep the first 100 climbs
    num = 100
    all_climbs.climbs = grade_everything(all_climbs.climbs[0:num])

    num_graded = sum([i.nn_grade is not None for i in all_climbs.climbs])
    print(f'Managed to grade {num_graded/num:.0%}')
    
    num_correct = sum([i.nn_grade is not None and i.grade.grade_number == i.nn_grade.grade_number for i in all_climbs.climbs])
    print(f'Managed to correctly grade {num_correct/num:.0%}')
