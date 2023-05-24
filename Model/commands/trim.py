from Model.commands.icommand import Command
from Model import ffmeg_editor
from Model.fragment import Fragment


class Trim(Command):
    def __init__(self, parent, fragment_index, start, end):
        self.start = start
        self.end = end
        super().__init__(parent, fragment_index)

    def operate(self):
        suffix = '-tf' + str(self.start) + 't' + str(self.end)
        old_path = self.old_file.content
        new_path = old_path[:-4] + suffix + old_path[-4:]
        ffmeg_editor.trim(old_path, new_path, self.start, self.end)
        return Fragment(new_path)