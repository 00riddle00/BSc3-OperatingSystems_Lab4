from config import cls, _sleep, clear_line
from Utils import *

from ReadFromInterface import ReadFromInterface
from Resources import Resources
from Loader import Loader
from ProcessTable import ProcessTable
from Process import Process


class StartStop(Process):
    name = PROC_START_STOP

    # Possible blocked states:
    # unblocked               = 0
    # waiting for res_mos_end = 1

    def start(self):
        super(StartStop, self).start()
        # RunningProcessTable.add(self)
        cls()
        _sleep(0.2)
        print("Booting up.", end='\r')
        _sleep(0.5)
        print("Booting up..", end='\r')
        _sleep(0.5)
        print("Booting up...", end='\r')
        _sleep(0.5)
        clear_line()
        print("Booting up.", end='\r')
        _sleep(0.5)
        print("Booting up..", end='\r')
        _sleep(0.5)
        print("Booting up...", end='\r')
        _sleep(0.7)
        cls()
        _sleep(0.5)

        print("StartStop process has started")
        _sleep(0.5)

        self.Sys_Resources_Initialization()
        self.Sys_Process_Initialization()

        cls()
        print("===============================")
        print("       Welcome to the OS!      ")
        print("===============================")
        _sleep(0.2)

        self.blocked_state = 1

    def unblock(self):
        if self.blocked_state == 1:
            self.Sys_Process_Destruction()
            self.Sys_Resources_Destruction()
            print("Shutting down.", end='\r')
            _sleep(0.5)
            print("Shutting down..", end='\r')
            _sleep(0.5)
            print("Shutting down...", end='\r')
            _sleep(0.5)
            clear_line()
            print("Shutting down")
            _sleep(0.2)
            print("Goodbye!")
            _sleep(0.7)
            cls()

    def Sys_Resources_Initialization(self):
        print("Creating System Resources.", end='\r')
        _sleep(0.4)
        print("Creating System Resources..", end='\r')
        _sleep(0.4)
        print("Creating System Resources...", end='\r')
        _sleep(0.4)
        clear_line()
        print("Creating System Resources.", end='\r')
        _sleep(0.8)
        clear_line()
        print("Creating System Resources")
        self.resources = Resources()
        print("System Resources have been created")
        _sleep(0.5)

    def Sys_Process_Initialization(self):
        print("System Process Initialization", end='\r')
        _sleep(0.5)
        print("System Process Initialization.", end='\r')
        _sleep(0.5)
        print("System Process Initialization..", end='\r')
        _sleep(0.5)
        print("System Process Initialization...", end='\r')
        _sleep(0.5)
        print("System Process Initialization....", end='\r')
        _sleep(0.5)
        print("System Process Initialization.....", end='\r')
        _sleep(0.5)
        clear_line()
        print("System Process Initialization.", end='\r')
        _sleep(0.5)
        print("System Process Initialization..", end='\r')
        _sleep(0.3)
        clear_line()
        print("System Process Initialization")
        _sleep(0.2)

        read_from_interface = ReadFromInterface(self.resources)
        loader = Loader(self.resources)

        self.add_child(read_from_interface)
        self.add_child(loader)

        print("Process ReadFromInterface initialized")
        _sleep(0.3)
        print("Process PrintLine initialized")
        _sleep(0.1)
        print("Process Interrupt initialized")
        _sleep(0.15)
        print("Process MainProc initialized")
        _sleep(0.05)
        print("Process Loader initialized")
        _sleep(0.1)
        print("Process Checker initialized")
        _sleep(0.2)
        print("Process JobToMemory initialized")
        _sleep(0.1)
        print("Process InputOutput initialized")
        _sleep(0.15)
        print("System Processes have been initialized")
        _sleep(0.5)
        self.process_table = ProcessTable()
        cls()

    def Sys_Process_Destruction(self):
        print(".", end='\r')
        _sleep(0.5)
        clear_line()
        print("", end='\r')
        _sleep(0.5)

        print(".", end='\r')
        _sleep(0.5)
        clear_line()
        print("")
        _sleep(0.5)

        print("Sys_Process_Destruction")
        _sleep(0.5)
        # for process in self.created_processes:
        #     OS.kill_process(process)

    def Sys_Resources_Destruction(self):
        print("Sys_Resources_Destruction")
        _sleep(0.5)
        # for resource in self.created_resources:
        #     OS.kill_resource(resource)
