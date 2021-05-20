from StartStop import StartStop
from ReadFromInterface import ReadFromInterface
from Resources import Resources

if __name__ == '__main__':

    # curr_proc = ProcessTable.current()

    # if curr_proc.blocked_state > 0:
    #     perduoti kitam procesui
    # else:
    #     if curr_proc.priority == 'highest':
    #         curr_proc.run()
    #         sleep(2)
    #     elif:

    start_stop = StartStop()
    # resources = start_stop.resources
    start_stop.start()

    read_from_interface = start_stop.child_processes[0]
    read_from_interface.unblock()  # user input will be read here

    if Resources.res_mos_end:  # if user input is 'shutdown', the OS powers off
        start_stop.unblock()

    # user input is not 'shutdown', so that means that the user
    # has entered the name of the program, possibly with parameters
    loader = start_stop.child_processes[1]
    loader.unblock()

    if Resources.res_load_fin_hdd_to_smem:
        # read_from_interface process is notified about
        # the successful loader operation and writes
        # a success message
        read_from_interface.unblock()

    # read_from_interface.unblock()  # read user input once again
    # if Resources.res_mos_end:  # if user input is 'shutdown', the OS powers off
    #     start_stop.unblock()
