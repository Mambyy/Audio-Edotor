class Command:
    def __init__(self, parent, fragment_index, *args):
        self.fragment_index = fragment_index
        self.parent = parent
        if fragment_index != -1:
            self.old_file = self.parent.active_fragments[fragment_index]
        self.new_file = self.operate()
        parent.project_files.append(self.new_file)

    def do(self):
        self.parent.active_fragments[self.fragment_index] = self.new_file

    def undo(self):
        self.parent.active_fragments[self.fragment_index] = self.old_file

    def operate(self):
        pass