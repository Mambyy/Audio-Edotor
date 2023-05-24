from Model.commands.icommand import Command


class Down(Command):
    def __init__(self, parent, fragment_index):
        super().__init__(parent, fragment_index)
    def do(self):
        self.parent.active_fragments[self.fragment_index], self.parent.active_fragments[self.fragment_index + 1] = self.parent.active_fragments[self.fragment_index + 1], self.parent.active_fragments[self.fragment_index]

    def undo(self):
        self.do()