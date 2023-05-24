from Model.commands.icommand import Command
from Model.fragment import Fragment


class Clone(Command):
    def __init__(self, parent, fragment_index):
        super().__init__(parent, fragment_index)


    def do(self):
        self.parent.active_fragments.insert(self.fragment_index, self.new_file)

    def undo(self):
        del self.parent.active_fragments[self.fragment_index + 1]
    def operate(self):
        return Fragment(self.old_file.content)