##temp class to load pre-gen levels
##Imports

import command

class LoadLevel(Command)
    def __init__(self, ui, file):
        self.ui = ui
        self.fileName = fileName