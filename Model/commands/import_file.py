from Model.commands.icommand import Command
from Model.fragment import Fragment


class ImportFile(Command):
    def __init__(self, parent, fragment_index = -1, path = ''):
        self.path = path
        super().__init__(parent, fragment_index)

    def do(self):
        self.parent.active_fragments.append(self.new_file)

    def undo(self):
        del self.parent.active_fragments[len(self.parent.active_fragments) - 1]

    def operate(self):
        return Fragment(self.path)