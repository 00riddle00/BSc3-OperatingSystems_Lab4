from Utils import *


# also known as Planner
class ProcessManager:

    def __init__(self, init_process):
        self.init_process = init_process

    def plan(self):
        self.init_process.start()

        resources = self.init_process.resources
        process_table = self.init_process.process_table

        read_from_interface = self.init_process.get_child(PROC_READ_FROM_INTERFACE)
        # user input will be read here
        read_from_interface.unblock()

        # if user input is 'poweroff', the OS shuts down
        if resources.check(RES_MOS_END):
            self.init_process.unblock()

        # user input is not 'shutdown', so that means that the user
        # has entered the name of the program, possibly with parameters
        loader = self.init_process.get_child(PROC_LOADER)
        loader.unblock()

        # if resources.check(RES_L  get_res_load_fin_hdd_to_smem():
        if resources.check(RES_HDD_TO_SUPERVISOR_MEM_FIN):
            # read_from_interface process is notified about
            # the successful loader operation and writes
            # a success message
            read_from_interface.unblock()

        # read user input once again
        read_from_interface.unblock()

        # if user input is 'poweroff', the OS shuts down
        if resources.check(RES_MOS_END):
            self.init_process.unblock()
