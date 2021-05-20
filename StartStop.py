from time import sleep

from ReadFromInterface import ReadFromInterface
from Resources import Resources

class StartStop:

    # Possible states:
    #   blocked = -1
    #   stopped =  0
    #   ready   =  1
    #   running =  2
    state = 0

    # one of {0, 1}
    has_processor = 0
    started = 0

    def start(self):
        print("StartStop process has started")
        state = 2
        sleep(0.35)

        self.Sys_Resources_Initialization()
        self.Sys_Process_Initialization()

        # Blokavimas laukiant res_mos_end resurso
        # while not resources.check_res_mos_end():
        while True:
            user_input = ReadFromInterface.get_user_input()
            print("User input is: ", user_input)

        self.Sys_Resources_Destruction()
        self.Sys_Process_Destruction()

    # def run(self):

    def Sys_Resources_Initialization(self):
        print("Creating System Resources")
        sleep(0.5)
        resources = Resources()
        print("System Resources have been created")
    # Supervizorinė atimintis
    # Vartotojo atmintis
    # Kanalų įrenginys



    def Sys_Process_Initialization(self):
        print("System Process Initialization", end='\r')
        sleep(0.5)
        print("System Process Initialization.", end='\r')
        sleep(0.5)
        print("System Process Initialization..", end='\r')
        sleep(0.5)
        print("System Process Initialization...", end='\r')
        sleep(0.5)
        print("System Process Initialization....", end='\r')
        sleep(0.5)
        print("System Process Initialization.....")
        sleep(0.5)

        read_from_interface = ReadFromInterface()
        print("Process ReadFromInterface initialized")
        sleep(0.3)
        print("Process PrintLine initialized")
        sleep(0.2)
        print("Process Interrupt initialized")
        sleep(0.1)
        print("Process MainProc initialized")
        sleep(0.05)
        print("Process Loader initialized")
        sleep(0.05)
        print("Process Checker initialized")
        sleep(0.2)
        print("Process JobToMemory initialized")
        sleep(0.1)
        print("Process InputOutput initialized")
        sleep(0.05)
        print("System Processes have been initialized")
        sleep(0.05)

        return []

        # VirtualMemory
        # Pager
        # res_supervisor_memory
        # res_channel_dev
# Supervizorinė atimintis
# Vartotojo atmintis
# Kanalų įrenginys


    def Sys_Process_Destruction(self):
        print("Sys_Process_Destruction")
        sleep(0.5)
        # for process in self.created_processes:
        #     OS.kill_process(process)

    def Sys_Resources_Destruction(self):
        print("Sys_Resources_Destruction")
        sleep(0.5)
        # for resource in self.created_resources:
        #     OS.kill_resource(resource)
