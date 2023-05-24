import os

from PyQt5.QtCore import QUrl

from Model.commands.down import Down
from Model.commands.change_speed import ChangeSpeed
from Model.commands.clone import Clone
from Model.commands.concat import Concat
from Model.commands.import_file import ImportFile
from Model.commands.delete import Delete
from Model.commands.trim import Trim
from Model.player import Player
from Model.fragment import Fragment
from PyQt5 import QtCore
from Model import ffmeg_editor


class Project:
    def __init__(self, name):
        self.path = ""
        self.name = name

        self.project_files = []
        self.active_fragments = []

        self.player = Player()

        self.done_stack = []
        self.undone_stack = []


    def delete(self, fragment_index):
        cmd = Delete(self, fragment_index)
        cmd.do()
        self.done_stack.append(cmd)

    def change_speed(self, fragment_index, speed_ratio):
        cmd = ChangeSpeed(self, fragment_index, speed_ratio)
        cmd.do()
        self.done_stack.append(cmd)

    def trim(self, fragment_index, start, end):
        cmd = Trim(self, fragment_index, int(start), int(end))
        cmd.do()
        self.done_stack.append(cmd)

    def concat(self, fragment1, fragment2):
        cmd = Concat(self, fragment1, fragment2)
        cmd.do()
        self.done_stack.append(cmd)

    def import_file(self, path):
        cmd = ImportFile(self, path=path)
        cmd.do()
        self.done_stack.append(cmd)

    def up(self, fragment_index):
        if fragment_index != 0:
            fragment_to_down_index = fragment_index - 1
            cmd = Down(self, fragment_to_down_index)
            cmd.do()
            self.done_stack.append(cmd)

    def down(self, fragment_index):
        if fragment_index != len(self.active_fragments) - 1:
            cmd = Down(self, fragment_index)
            cmd.do()
            self.done_stack.append(cmd)

    def clone(self, fragment_index):
        cmd = Clone(self, fragment_index)
        cmd.do()
        self.done_stack.append(cmd)

    def export_as_file(self, path):
        ffmeg_editor.concat([x.content for x in self.active_fragments], path[1:])

    def undo(self):
        if len(self.done_stack) == 0:
            return
        cmd = self.done_stack.pop()
        cmd.undo()
        self.undone_stack.append(cmd)

    def redo(self):
        if len(self.undone_stack) == 0:
            return
        cmd = self.undone_stack.pop()
        cmd.do()
        self.done_stack.append(cmd)

    @staticmethod
    def unpack(pack_array, name, path):
        proj = Project(name)
        proj.path = path
        for line in pack_array:
            proj.active_fragments.append(Fragment(line[:-1]))
        return proj

    def pack(self):
        answer = []
        for fragment in self.active_fragments:
            answer.append(fragment.content)
        return answer
