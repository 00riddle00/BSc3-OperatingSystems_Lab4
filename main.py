from StartStop import StartStop
import Utils as ut

if __name__ == '__main__':

    # curr_proc = ProcessTable.current()

    # if curr_proc.blocked_state > 0:
    #     perduoti kitam procesui
    # else:
    #     if curr_proc.priority == 'highest':
    #         curr_proc.run()
    #         sleep(2)
    #     elif:

    start_stop = StartStop(None, None)
    # resources = start_stop.resources
    start_stop.start()

    resources = start_stop.resources
    process_table = start_stop.process_table

    read_from_interface = start_stop.children['rfi']
    read_from_interface.unblock()  # user input will be read here

    if resources.get_res_mos_end():  # if user input is 'shutdown', the OS powers off
        start_stop.unblock()

    # user input is not 'shutdown', so that means that the user
    # has entered the name of the program, possibly with parameters
    loader = start_stop.children['ldr']
    loader.unblock()

    if resources.get_res_load_fin_hdd_to_smem():
        # read_from_interface process is notified about
        # the successful loader operation and writes
        # a success message
        read_from_interface.unblock()

    read_from_interface.unblock()  # read user input once again

    if resources.get_res_mos_end():  # if user input is 'shutdown', the OS powers off
        start_stop.unblock()
