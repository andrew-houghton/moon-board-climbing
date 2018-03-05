from climb import Climb

terminator_character = '_'


class Climbset():
    # Holds many climbs
    # Used to manage entire strings of climbs such as LSTM input and output

    def __init__(self, climbs=[]):
        # Create a climbset starting from a list.
        # If no climbs are supplied then an empty list is used.

        if not type(climbs) == list:
            raise ValueError('Input must be a list of climb objects. Please input a list.')

        for climb in climbs:
            if type(climb) != Climb:
                raise ValueError('Objects in climbset must be of type climb.')

        self.climbs = climbs

    def add(self, climb):
        # Add a new climb into the climbset (at the end)
        if type(climb) != Climb:
            raise ValueError('Objects in climbset must be of type climb.')
        self.climbs.append(climb)

    def pre_grade_string(self):
        # Create a string containing all the climbs in the climbset
        # Put the grade before the moves of the each climb

        output_str = ''
        format_str = '{grade}{moves}{terminator}'
        for climb in self.climbs:
            output_str += format_str.format(
                grade=climb.grade.as_nn_grade(),
                moves=climb.moves_nn_string(),
                terminator=terminator_character)
        return output_str

    def post_grade_string(self):
        # Create a string containing all the climbs in the climbset
        # Put the grade after the moves of the each climb

        output_str = ''
        format_str = '{moves}{grade}{terminator}'
        for climb in self.climbs:
            output_str += format_str.format(
                grade=climb.grade.as_nn_grade(),
                moves=climb.moves_nn_string(),
                terminator=terminator_character)
        return output_str

    def no_grade_string(self):
        # Create a string containing all the climbs in the climbset
        # Do not include the grade of the climb in the string

        output_str = ''
        for climb in self.climbs:
            output_str += climb.moves_nn_string()
            output_str += terminator_character
        return output_str

    def __repr__(self):
        # Create a human readable string representation of the whole climbset.

        return 'Climbset of length {} with climbs;\n{}'.format(
            len(self.climbs),
            '\n'.join([str(i) for i in self.climbs]))
