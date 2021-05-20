from Resources import Resources

class ReadFromInterface:
    name = 'ReadFromInterface'
    user_input = ''

    def __init__(self, resources):
        self.resources = resources

        # Possible stages:
        # blocked = -1
        # stopped =  0
        # ready   =  1
        # running =  2
        self.stage = 0

        # Possible blocked states:
        # unblocked                         = 0
        # waiting for res_user_input        = 1
        # waiting for res_supervisor_memory = 2
        self.blocked_state = 0

        self.start()

    def start(self):
        self.blocked_state = 1

    def unblock(self):
        if self.blocked_state == 1:
            self.user_input = input("Enter command: ")
            if self.user_input == 'poweroff':
                self.resources.set_res_mos_end(1)
            else:
                self.resources.set_res_load_prog_hdd_to_smem(self.user_input)
                self.blocked_state = 2
        elif self.blocked_state == 2:
            print("[ReadFromInterface]: The program is now in supervisor memory")
            self.blocked_state = 1
