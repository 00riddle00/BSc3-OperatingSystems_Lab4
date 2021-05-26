from Process import Process
from Utils import *


class ReadFromInterface(Process):
    id = 2
    name = PROC_READ_FROM_INTERFACE

    # Possible blocked states:
    # unblocked                      = 0
    # waiting for RES_USER_INTERFACE = 1
    # waiting for RES_SUPERVISOR_MEM = 2
    blocked_state = 0

    user_input = ''

    def __init__(self, resources, process_table):
        super(ReadFromInterface, self).__init__(resources, process_table)
        self.start()

    def start(self):
        super(ReadFromInterface, self)
        self.blocked_state = 1

    def unblock(self):
        if self.blocked_state == 1:
            self.user_input = input("Enter command: ")
            if self.user_input == 'poweroff':
                self.resources.free(RES_MOS_END)
            else:
                self.resources.free(RES_HDD_TO_SUPERVISOR_MEM, self.user_input)
                self.blocked_state = 2
        elif self.blocked_state == 2:
            print("[ReadFromInterface]: The program is now in supervisor memory")
            self.blocked_state = 1
