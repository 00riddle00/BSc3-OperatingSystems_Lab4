from StartStop import StartStop
from ReadFromInterface import ReadFromInterface

if __name__ == '__main__':
    start_stop = StartStop()
    read_from_interface = start_stop.start()

    read_from_interface.unblock()
    read_from_interface.unblock()

    read_from_interface.unblock()
    read_from_interface.unblock()

    start_stop.unblock()
