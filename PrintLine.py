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
            if self.resources[RES_STR_IN_MEM] == '':
                print("BLOCKED Waiting for RES_STR_IN_MEM  ")
            else:
                print("Got resource RES_STR_IN_MEM -> stage 2")
                self.switchCase = 2

        elif self.switchCase == 2:
            if not self.resources[RES_CHN_DEVICE]:
                print("BLOCKED Waiting for RES_CHN_DEVICE")
            else:
                print("Got resource RES_CHN_DEVICE -> stage 3")
                self.switchCase = 3

        elif self.switchCase == 3:
            # Eilutes i6vedimas
            print("Print line to GUI")
            print(self.resources[RES_STR_IN_MEM])
            self.switchCase = 4

        elif self.switchCase == 4:
            # Atlaisvinam "res_channel_dev"
            print("Free Chanel device resource")
            self.resources.free(RES_CHN_DEVICE)
            self.switchCase = 1
