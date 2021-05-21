
class ProcessTable:
    table = dict()

    def add(self, process):
        self.table[process.name] = process
