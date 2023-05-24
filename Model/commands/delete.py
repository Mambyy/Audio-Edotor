import os

from Model.commands.icommand import Command


class Delete(Command):
    def __init__(self, parent, fragment_index):
        super().__init__(parent, fragment_index)

    def do(self):
        del self.parent.active_fragments[self.fragment_index]

    def undo(self):
        self.parent.active_fragments.insert(self.fragment_index, self.old_file)
