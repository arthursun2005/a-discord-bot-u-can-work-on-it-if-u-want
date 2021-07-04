class Lobby:
    def __init__(self):
        self.owner = None
        self.players = []
        self.state = 0

        '''
        0 = waiting to be started
        1 = started
        ```
