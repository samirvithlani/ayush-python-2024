class InvalidString(Exception):

    def __init__(self, value):
        super().__init__(value)

    