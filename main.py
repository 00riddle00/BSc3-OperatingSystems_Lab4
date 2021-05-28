from StartStop import StartStop
from ProcessManager import ProcessManager

if __name__ == '__main__':
    start_stop = StartStop(None, None)
    process_manager = ProcessManager(start_stop)
    process_manager.plan()