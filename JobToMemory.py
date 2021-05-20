from time import sleep

from Resources import Resources

class JobToMemory:
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
        while(res_Program_OK == '' & self.blocked_state == 0):
            sleep(1)
            print("Waiting for program_OK")
        self.blocked_state = 1
        print("Got resource program_OK -> stage 1")

        while(res_User_mem == False & self.blocked_state == 1):
            sleep(1)
            print("Waiting for res_User_mem")
        self.blocked_state = 2
        print("Got resource res_User_mem -> stage 2")

        # Atlaisvinam "Load program from supervisor memory to user memory"
        res_load_prog_smem_to_umem = res_Program_OK


        # while(res_load_prog_smem_to_umem == False & self.blocked_state == 2):
        #     sleep(1)
        #     print("Waiting for res_load_prog_smem_to_umem")
        # self.blocked_state = 3
        # print("Got resource res_load_prog_smem_to_umem -> stage 3")

        while(res_channel_dev == False & self.blocked_state == 2):
            sleep(1)
            print("Waiting for res_load_prog_smem_to_umem")
        self.blocked_state = 3
        print("Got resource res_channel_dev -> stage 3")
        res_channel_dev = 5 #5 - random tiesiog reiksme kad is cia i ten sukelt reikia


        # Atlaisvinam "load_fin_smem_to_umem"
        load_fin_smem_to_umem = "Complete"
        # Atlaisvinam "res_channel_dev"
        res_channel_dev = 0
        # Atlaisvinam "res_supervisor_mem"
        res_supervisor_mem = 0

#     def start(self):
#         self.blocked_state = 1
#
#     def unblock(self):
#         if self.blocked_state == 1:
#             self.user_input = input("Enter command: ")
#             self.blocked_state = 3
#         if self.blocked_state == 3:
#             # self.copy_block_to_supervisor_memory()
#             pass
#
#     @staticmethod
#     def get_user_input():
#         user_input = input("Enter command: ")
#         return user_input
#
#     def copy_block_to_supervisor_memory(self):
#         print("copy_block_to_supervisor_memory")
#
# # ReadFromInterface -> block
