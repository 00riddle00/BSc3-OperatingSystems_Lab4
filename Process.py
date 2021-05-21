from abc import abstractmethod, ABCMeta
from ProcessTable import ProcessTable


# class Process(metaclass=ABCMeta):
class Process(object):

    def __init__(self, resources, process_table):
        self.resources = resources
        self.process_table = process_table

        # Possible stages:
        # blocked = -1
        # stopped =  0
        # ready   =  1
        # running =  2
        self.stage = 0

        self.children = dict()

    def add_child(self, child):
        self.children[child.name] = child

    def get_child(self, child_name):
        return self.children[child_name]

    @property
    @abstractmethod
    def name(self):
        pass

    @property
    @abstractmethod
    # Possible blocked states:
    # unblocked               = 0
    # waiting for resource x  = 1
    # waiting for resource y  = 2
    # ...
    def blocked_state(self):
        pass

    @abstractmethod
    def start(self):
        if self.process_table:
            self.process_table.add(self)

    @abstractmethod
    def unblock(self):
        pass
