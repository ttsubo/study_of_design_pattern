class Context(object):
    def __init__(self, stateObj):
        self.state = stateObj

    def setState(self, obj):
        self.state = obj
    
    def getState(self):
        return self.state

    def handle(self):
        self.state.handle(self)
