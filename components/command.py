#enter some notes later on what this class does...

class Command():
    def run(self):
            raise NotImplementedError()
    

class UserInterface():
    def __init__(self):
         #we probably want any pre-initialization stuff here
         self.commands = []
         #any player stuff could go here as well

    def update(self):
        #we should prob update any state changes in UI here