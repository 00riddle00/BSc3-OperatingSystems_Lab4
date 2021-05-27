from time import sleep
from Process import Process
from Resources import Resources
from Utils import *


class JobToMemory(Process):
    name = PROC_LOADER

    # Possible states:
    #   blocked = -1
    #   stopped =  0
    #   ready   =  1
    #   running =  2

    # Possible blocked states:
    # unblocked = 0
    # user_input = 1
    # supervisor_memory = 2

    switchCase = 1

    def __init__(self, resources, process_table):
        super(JobToMemory, self).__init__(resources, process_table)
        self.switchCase = 1

    def Execute(self):

        if self.switchCase == 1:
            if self.resources[RES_PROGRAM_CKECKED] == '':
                print("BLOCKED Waiting for RES_PROGRAM_CKECKED  ")
            else:
                print("Got resource program_OK -> stage 2")
                self.switchCase = 2

        elif self.switchCase == 2:
            if not self.resources[RES_USER_MEM]:
                print("BLOCKED Waiting for res_User_mem")
            else:
                print("Got resource res_User_mem -> stage 3")
                self.switchCase = 3

        elif self.switchCase == 3:
            # Atlaisvinam "Load program from supervisor memory to user memory"
            self.resources[RES_SUPERVISOR_MEM_TO_USER_MEM] = self.resources[RES_PROGRAM_CKECKED]
            self.switchCase = 4

        elif self.switchCase == 4:
            if not self.resources[RES_CHN_DEVICE]:
                print("BLOCKED Waiting for RES_CHN_DEVICE")
            else:
                print("Got resource RES_CHN_DEVICE -> stage 5")
                self.switchCase = 5

        elif self.switchCase == 5:
            # Atlaisvinam "load_fin_smem_to_umem"
            self.resources[RES_SUPERVISOR_MEM_TO_USER_MEM_FIN] = "Complete"
            # Atlaisvinam "res_channel_dev"
            self.resources.free(RES_CHN_DEVICE)
            # Atlaisvinam "res_supervisor_mem"
            self.resources.free(RES_SUPERVISOR_MEM)
            self.switchCase = 1
