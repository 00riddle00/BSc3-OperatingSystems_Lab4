import os
from subprocess import call
from time import sleep

from ReadFromInterface import ReadFromInterface
from Resources import Resources
from Loader import Loader

class StartStop:
    child_processes = []
    name = 'StartStop'

    def __init__(self):
        # Possible stages:
        # blocked = -1
        # stopped =  0
        # ready   =  1
        # running =  2
        self.stage = 0

        # Possible blocked states:
        # unblocked               = 0
        # waiting for res_mos_end = 1
        self.blocked_state = 0

    def start(self):
        # RunningProcessTable.add(self)
        # self.clear()
        # sleep(0.2)
        print("Booting up.", end='\r')
        # sleep(0.5)
        print("Booting up..", end='\r')
        # sleep(0.5)
        print("Booting up...", end='\r')
        # sleep(0.5)
        print("Booting up.", end='\r')
        # sleep(0.5)
        print("Booting up..", end='\r')
        # sleep(0.5)
        print("Booting up...", end='\r')
        # sleep(1)
        # self.clear()
        # sleep(0.5)

        print("StartStop process has started")
        # sleep(0.5)

        self.resources = self.Sys_Resources_Initialization()
        self.Sys_Process_Initialization()

        # self.clear()
        print("===============================")
        print("       Welcome to the OS!      ")
        print("===============================")

        self.blocked_state = 1

    def unblock(self):
        if self.blocked_state == 1:
            self.Sys_Resources_Destruction()
            self.Sys_Process_Destruction()
            print("Shutting down.", end='\r')
            # sleep(0.5)
            print("Shutting down..", end='\r')
            # sleep(0.5)
            print("Shutting down...")
            # sleep(0.5)
            # self.clear()

    def Sys_Resources_Initialization(self):
        print("Creating System Resources")
        # sleep(0.5)
        resources = Resources()
        print("System Resources have been created")
        return resources

    def Sys_Process_Initialization(self):
        print("System Process Initialization", end='\r')
        # sleep(0.5)
        print("System Process Initialization.", end='\r')
        # sleep(0.5)
        print("System Process Initialization..", end='\r')
        # sleep(0.5)
        print("System Process Initialization...", end='\r')
        # sleep(0.5)
        print("System Process Initialization....", end='\r')
        # sleep(0.5)
        print("System Process Initialization.....")
        # sleep(0.5)

        read_from_interface = ReadFromInterface(self.resources)
        loader = Loader(self.resources)
        self.child_processes.append(read_from_interface)
        self.child_processes.append(loader)
        print("Process ReadFromInterface initialized")
        # sleep(0.3)
        print("Process PrintLine initialized")
        # sleep(0.2)
        print("Process Interrupt initialized")
        # sleep(0.1)
        print("Process MainProc initialized")
        # sleep(0.05)
        print("Process Loader initialized")
        # sleep(0.05)
        print("Process Checker initialized")
        # sleep(0.2)
        print("Process JobToMemory initialized")
        # sleep(0.1)
        print("Process InputOutput initialized")
        # sleep(0.05)
        print("System Processes have been initialized")
        # sleep(0.05)

    def Sys_Process_Destruction(self):
        print("Sys_Process_Destruction")
        # sleep(0.5)
        # for process in self.created_processes:
        #     OS.kill_process(process)

    def Sys_Resources_Destruction(self):
        print("Sys_Resources_Destruction")
        # sleep(0.5)
        # for resource in self.created_resources:
        #     OS.kill_resource(resource)

    def clear(self):
        # check and make call for specific operating system
        _ = call('clear' if os.name =='posix' else 'cls')

