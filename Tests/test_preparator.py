import os

from Model.project import Project
from Model.fragment import Fragment
import Model.fragment


class TestPreparator:
    @staticmethod
    def prepare():
        Model.fragment.last_id = 0
        parent = Project("Test project")
        fragment_index = 0
        content = os.path.join(os.path.dirname(__file__), "test.wav")
        fragment = Fragment(content)
        parent.active_fragments.append(fragment)

        return parent, fragment_index, content
