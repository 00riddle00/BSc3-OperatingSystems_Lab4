from Resources import Resources

class ReadFromInterface:

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

    user_input = ''

    def __init__(self):
        self.start()

    def start(self):
        self.blocked_state = 1

    def unblock(self):
        if self.blocked_state == 1:
            self.user_input = input("Enter command: ")
            self.blocked_state = 3
        if self.blocked_state == 3:
            # self.copy_block_to_supervisor_memory()
            pass

    @staticmethod
    def get_user_input():
        user_input = input("Enter command: ")
        return user_input

    def copy_block_to_supervisor_memory(self):
        print("copy_block_to_supervisor_memory")

# ReadFromInterface -> block
