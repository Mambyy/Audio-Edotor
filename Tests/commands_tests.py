import math
import os
import unittest
from test_preparator import TestPreparator
from Model.commands.change_speed import ChangeSpeed
import Model.fragment
from Model.fragment import Fragment


class ChangeSpeedTests(unittest.TestCase):
    def test_change_speed(self):
        parent, fragment_index, content = TestPreparator.prepare()
        parent_fragment_seconds = parent.active_fragments[fragment_index].seconds
        parent.change_speed(fragment_index, 2)
        fragment = Fragment(os.path.join(os.path.dirname(__file__), "test-s2.wav"))
        os.remove(os.path.join(os.path.dirname(__file__), "test-s2.wav"))

        self.assertEqual(abs(fragment.seconds - parent_fragment_seconds / 2) < 0.1, True)

    def test_change_speed_undo(self):
        parent, fragment_index, content = TestPreparator.prepare()
        parent_fragment_seconds = parent.active_fragments[fragment_index].seconds
        parent.change_speed(fragment_index, 2)
        os.remove(os.path.join(os.path.dirname(__file__), "test-s2.wav"))
        parent.undo()

        self.assertEqual(abs(parent.active_fragments[fragment_index].seconds - parent_fragment_seconds) < 0.1, True)

    def test_change_speed_redo(self):
        parent, fragment_index, content = TestPreparator.prepare()
        parent_fragment_seconds = parent.active_fragments[fragment_index].seconds
        parent.change_speed(fragment_index, 2)
        fragment = Fragment(os.path.join(os.path.dirname(__file__), "test-s2.wav"))
        os.remove(os.path.join(os.path.dirname(__file__), "test-s2.wav"))
        parent.undo()
        parent.redo()

        self.assertEqual(abs(fragment.seconds - parent_fragment_seconds / 2) < 0.1, True)

    def test_clone(self):
        parent, fragment_index, content = TestPreparator.prepare()
        parent.clone(fragment_index)
        parent.undo()
        parent.redo()

        self.assertEqual(parent.active_fragments[fragment_index].content,
                         parent.active_fragments[fragment_index + 1].content)

    def test_delete(self):
        parent, fragment_index, content = TestPreparator.prepare()
        parent.delete(fragment_index)
        parent.undo()
        parent.redo()

        self.assertEqual(len(parent.active_fragments), 0)

    def test_down(self):
        parent, fragment_index, content = TestPreparator.prepare()
        fragment1 = parent.active_fragments[fragment_index]
        fragment2 = Fragment(fragment1.content)
        parent.active_fragments.append(fragment2)
        parent.down(fragment_index)
        parent.undo()
        parent.redo()

        self.assertEqual(parent.active_fragments[fragment_index].id - parent.active_fragments[fragment_index + 1].id, 1)

    def test_up(self):
        parent, fragment_index, content = TestPreparator.prepare()
        fragment1 = parent.active_fragments[fragment_index]
        fragment2 = Fragment(fragment1.content)
        parent.active_fragments.append(fragment2)
        parent.up(fragment_index + 1)
        parent.undo()
        parent.redo()

        self.assertEqual(parent.active_fragments[fragment_index].id - parent.active_fragments[fragment_index + 1].id, 1)

    def test_import_file(self):
        parent, fragment_index, content = TestPreparator.prepare()
        fragment = parent.active_fragments[fragment_index]
        parent.import_file(fragment.content)
        parent.undo()
        parent.redo()

        self.assertEqual(len(parent.active_fragments), 2)

    def test_export_file(self):
        parent, fragment_index, content = TestPreparator.prepare()
        fragment = parent.active_fragments[fragment_index]
        parent.import_file(fragment.content)
        parent.undo()
        parent.redo()

        self.assertEqual(len(parent.active_fragments), 2)

    def test_trim(self):
        parent, fragment_index, content = TestPreparator.prepare()
        parent.trim(fragment_index, 20, 90)
        fragment = Fragment(os.path.join(os.path.dirname(__file__), "test-tf20t90.wav"))
        os.remove(os.path.join(os.path.dirname(__file__), "test-tf20t90.wav"))
        parent.undo()
        parent.redo()

        self.assertEqual(abs(fragment.seconds - 70) < 0.1, True)
