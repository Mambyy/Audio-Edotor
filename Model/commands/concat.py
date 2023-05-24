from Model.commands.icommand import Command
from Model import ffmeg_editor
from Model.fragment import Fragment


class Concat(Command):
    def __init__(self, parent, fragment_index, fragment2_index):
        self.fragment2_index = fragment2_index
        self.old2_file = parent.active_fragments[fragment2_index]
        super().__init__(parent, fragment_index)

    def do(self):
        del self.parent.active_fragments[self.fragment_index]
        del self.parent.active_fragments[self.fragment2_index + -1 if self.fragment2_index > self.fragment_index else 1]
        self.parent.active_fragments.insert(min(self.fragment_index, self.fragment2_index), self.new_file)

    def undo(self):
        del self.parent.active_fragments[min(self.fragment_index, self.fragment2_index)]
        self.parent.active_fragments.insert(self.fragment2_index + -1 if self.fragment2_index > self.fragment_index else 1, self.old2_file)
        self.parent.active_fragments.insert(self.fragment_index, self.old_file)

    def operate(self):
        old2_file_name = ''
        for i in range(len(self.old2_file.content) - 1, -1, -1):
            if self.old2_file.content[i] == '/':
                break
            old2_file_name += self.old2_file.content[i]
        new_path = self.old_file.content[:-4] + '-' + old2_file_name[::-1]
        ffmeg_editor.concat([self.old_file.content, self.old2_file.content], new_path)
        fragment = Fragment(new_path)
        self.parent.project_files.append(fragment)
        return fragment