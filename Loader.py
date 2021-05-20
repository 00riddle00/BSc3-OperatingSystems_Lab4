from time import sleep
from Resources import Resources

class Loader:
    resources = Resources
    # Possible states:
    #   blocked = -1
    #   stopped =  0
    #   ready   =  1
    #   running =  2
    stage = 0

    # Possible blocked states:
    # unblocked = 0
    # user_input = 1
    # supervisor_memory = 2
    blocked_state = 0

    # one of {0, 1}
    has_processor = 0
    started = 0

    def __init__(self, resources):
        self.resources = resources
        self.start()

    def start(self):
        self.blocked_state = 1

    def unblock(self):
        if(self.resources.get_res_load_prog_hdd_to_smem == True & self.blocked_state == 0):
            sleep(1)
            self.blocked_state = 1
            self.resources.set_res_load_prog_hdd_to_smem(0)
            print("Got resource res_load_prog_hdd_to_smem -> stage 1")
        elif(self.resources.get_res_channel_dev == True & self.blocked_state == 1):
            sleep(1)
            self.blocked_state = 2
            self.resources.set_res_channel_dev(4)
            print("Got resource res_channel_dev -> stage 2")

        # Atlaisvinam ""
        self.resources.set_res_channel_dev(1)
        # Atlaisvinam ""
        self.resources.set_res_load_prog_hdd_to_smem(1)

