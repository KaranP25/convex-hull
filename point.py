class Point(object):
        # Constructor for Wells Object
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # Return method used to access Objects values
    def __repr__(self):
        return "({0},{1})".format(self.x, self.y)
