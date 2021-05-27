from time import sleep
from Process import Process
from Resources import Resources
from Utils import *


class PrintLine(Process):
    name = PROC_LOADER

    switchCase = 1

    def __init__(self, resources, process_table):
        super(PrintLine, self).__init__(resources, process_table)
        self.switchCase = 1

    def Execute(self):

        if self.switchCase == 1:
            if self.resources[RES_SUPERVISOR_MEM_TO_USER_MEM_FIN] == '':
                print("BLOCKED Waiting for RES_SUPERVISOR_MEM_TO_USER_MEM_FIN  ")
            else:
                print("Got resource RES_SUPERVISOR_MEM_TO_USER_MEM_FIN -> stage 2")
                self.switchCase = 2

        elif self.switchCase == 2:
            # if not vykdymo_laikas :
            if True:
                print("Create process JobGovernor giving him the RES_SUPERVISOR_MEM_TO_USER_MEM_FIN resource")
                self.switchCase = 3
            else:
                print("Delete JobGovernor, which created following resource")
                self.switchCase = 4

        elif self.switchCase == 3:
            print("Create process JobGovernor giving him the RES_SUPERVISOR_MEM_TO_USER_MEM_FIN resource")
            self.switchCase = 1

        elif self.switchCase == 4:
            print("Delete JobGovernor, which created following resource")
            self.switchCase = 1
