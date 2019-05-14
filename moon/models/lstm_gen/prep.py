from moon.utils.load_data import load_climbset
import os


def prep_no_grade():
    output_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'input.txt')
    with open(output_path, 'w') as handle:
        handle.write(load_climbset().no_grade_string())
    return output_path

if __name__=="__main__":
    prep_no_grade()
