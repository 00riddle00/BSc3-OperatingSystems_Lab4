from StartStop import StartStop
from Utils import *

if __name__ == '__main__':
    start_stop = StartStop(None, None)
    start_stop.start()

    resources = start_stop.resources
    process_table = start_stop.process_table

    read_from_interface = start_stop.get_child(PROC_READ_FROM_INTERFACE)
    read_from_interface.unblock()  # user input will be read here

    if resources.get_res_mos_end():  # if user input is 'shutdown', the OS powers off
        start_stop.unblock()

    # user input is not 'shutdown', so that means that the user
    # has entered the name of the program, possibly with parameters
    loader = start_stop.get_child(PROC_LOADER)
    loader.unblock()

    if resources.get_res_load_fin_hdd_to_smem():
        # read_from_interface process is notified about
        # the successful loader operation and writes
        # a success message
        read_from_interface.unblock()

    read_from_interface.unblock()  # read user input once again

    if resources.get_res_mos_end():  # if user input is 'shutdown', the OS powers off
        start_stop.unblock()
