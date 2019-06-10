from moon.types.climb import Climb


class Climbset:
    # Holds many climbs
    # Used to manage entire strings of climbs such as LSTM input and output

    def __init__(self, climbs=None, input_type="list"):
        # Create a climbset starting from a list.
        # If no climbs are supplied then an empty list is used.
        if not climbs:
            climbs = []

        if input_type == "list":
            if not type(climbs) == list:
                raise ValueError("Input must be a list of climb objects. Please input a list.")

            for climb in climbs:
                if type(climb) != Climb:
                    raise ValueError("Objects in climbset must be of type climb.")
            self.climbs = climbs

        elif input_type == "sample":
            # Check input type
            if not type(climbs) == list:
                raise ValueError("Input must be a list of strings. Please input a list.")

            # Check input type
            for climb in climbs:
                if type(climb) != str:
                    raise ValueError("Input object from sample must be of type str.")

            # Process each climb one by one and add them to the climbset
            self.climbs = []
            for climb in climbs:
                try:
                    cur_climb = Climb("sample", climb)
                    self.climbs.append(cur_climb)
                except ValueError:
                    pass
        else:
            raise ValueError("Invalid input_type argument.")

    @classmethod
    def get_terminator(cls):
        return "_"

    @classmethod
    def get_grade_seperator(cls):
        return "="

    def add(self, climb):
        # Add a new climb into the climbset (at the end)
        if climb.__class__ != Climb:
            raise ValueError("Objects in climbset must be of type climb.")
        self.climbs.append(climb)

    def pre_grade_string(self):
        # Create a string containing all the climbs in the climbset
        # Put the grade before the moves of the each climb

        output_str = ""
        format_str = "{grade}{grade_seperator}{moves}{terminator}"
        for climb in self.climbs:
            output_str += format_str.format(
                grade=climb.grade.as_nn_grade(),
                grade_seperator=self.get_grade_seperator(),
                moves=climb.moves_nn_string(),
                terminator=self.get_terminator(),
            )
        return output_str

    def post_grade_string(self):
        # Create a string containing all the climbs in the climbset
        # Put the grade after the moves of the each climb
        output_str = ""
        format_str = "{moves}{grade_seperator}{grade}{terminator}"
        for climb in self.climbs:

            output_str += format_str.format(
                grade=climb.grade.as_nn_grade(),
                grade_seperator=self.get_grade_seperator(),
                moves=climb.moves_nn_string(),
                terminator=self.get_terminator(),
            )
        return output_str

    def no_grade_string(self):
        # Create a string containing all the climbs in the climbset
        # Do not include the grade of the climb in the string

        output_str = ""
        for climb in self.climbs:
            output_str += climb.moves_nn_string()
            output_str += self.get_terminator()
        return output_str

    def __repr__(self):
        # Create a human readable string representation of the whole climbset.

        return f"Climbset of length {len(self.climbs)}"
