from time import sleep
from Process import Process
from Resources import Resources
from Utils import *


class Loader(Process):
    name = PROC_LOADER

    # Possible blocked states:
    # unblocked                         = 0
    # waiting for RES_USER_INTERFACE    = 1
    # waiting for RES_SUPERVISOR_MEMORY = 2
    # supervisor_memory = 2
    blocked_state = 0

    fileName = ''

    def __init__(self, resources, process_table):
        super(Loader, self).__init__(resources, process_table)
        self.start()

    def start(self):
        super(Loader, self)
        self.blocked_state = 1

    def unblock(self):
        # if (self.resources.get_res_load_prog_hdd_to_smem() == '' and self.blocked_state == 1):
        if self.resources[RES_HDD_TO_SUPERVISOR_MEM] == '' and self.blocked_state == 1:
            sleep(1)
            print("Waiting res_load_prog_hdd_to_smem")
        else:
            # self.fileName = self.resources.get_res_load_prog_hdd_to_smem()
            self.fileName = self.resources[RES_HDD_TO_SUPERVISOR_MEM]
            # self.resources.set_res_load_prog_hdd_to_smem(0)
            self.resources.free(RES_HDD_TO_SUPERVISOR_MEM)
            self.blocked_state = 2
            print("Got resource res_load_prog_hdd_to_smem  @", self.fileName, "@  -> stage 1")
        # if(self.resources.get_res_channel_dev == False & self.blocked_state == 2):
        if not self.resources[RES_CHN_DEVICE] and self.blocked_state == 2:
            sleep(1)
            print("Waiting res_channel_dev")
        else:
            self.blocked_state = 1
            # self.resources.set_res_channel_dev(4)
            self.resources[RES_CHN_DEVICE] = 4
            print("Got resource res_channel_dev -> stage 2")

            # Atlaisvinam ""
            self.resources.free(RES_CHN_DEVICE)
            # Atlaisvinam ""
            self.resources.free(RES_HDD_TO_SUPERVISOR_MEM_FIN)
