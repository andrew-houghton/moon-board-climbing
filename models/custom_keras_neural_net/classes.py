class Hold:
    ''' Hold class contains all the information about an individual hold. '''

    def __init__(self,XY=None):
        if XY != None:
            self.X = XY[0]
            self.Y = XY[1]
            self.padding = 1
        else:
            self.X = 0.0
            self.Y = 0.0
            self.padding = 0

    def get_data_len():
        return 3

    def get_data(self):
        return (
            self.X,
            self.Y,
            self.padding)

    def __repr__(self):
        return str(self.get_data())


class Climb:
    ''' Climb class contains a sqeunce of holds in an array '''
    def get_max_len():
        return 13

    def __init__(self, hold_array=[]):
        self.holds = [Hold() for i in range(Climb.get_max_len())]

        # Add the holds supplied to the climb
        for i in range(Climb.get_max_len()):
            hold = hold_array[i]
            if type(hold) == Hold:
                self.holds[i] = hold
            else:
                print('Invalid hold input.')

    def __repr__(self):
        return str(self.holds)