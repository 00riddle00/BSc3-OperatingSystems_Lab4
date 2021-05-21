from StartStop import StartStop
from Utils import *

if __name__ == '__main__':
    start_stop = StartStop(None, None)
    start_stop.start()

    resources = start_stop.resources
    process_table = start_stop.process_table

    read_from_interface = start_stop.get_child(PROC_READ_FROM_INTERFACE)
    # user input will be read here
    read_from_interface.unblock()

    # if user input is 'poweroff', the OS shuts down
    if resources.check(RES_MOS_END):
        start_stop.unblock()

    exit()

    # user input is not 'shutdown', so that means that the user
    # has entered the name of the program, possibly with parameters
    loader = start_stop.get_child(PROC_LOADER)
    loader.unblock()

    if resources.get_res_load_fin_hdd_to_smem():
        # read_from_interface process is notified about
        # the successful loader operation and writes
        # a success message
        read_from_interface.unblock()

    # read user input once again
    read_from_interface.unblock()

    # if user input is 'poweroff', the OS shuts down
    if resources.get_res_mos_end():
        start_stop.unblock()
