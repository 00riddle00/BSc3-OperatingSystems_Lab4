
# processes
PROCS = {
    'root':   'START_STOP',
    'rfi':    'READ_FROM_INTERFACE',
    'chk':    'CHECKER',
    'ldr':    'LOADER',
    'mproc':  'MAIN_PROC',
    'jgov':   'JOB_GOVERONR',
    'vm':     'VIRTUAL_MACHINE',
    'int':    'INTERRUPT',
    'io':     'INPUT_OUTPUT',
    'printl': 'PRINT_LINE',
    'os':     'OS',
    'jmem':   'JOB_TO_MEMORY'
}

# resources
RES = {
    'mend':  'MOS_END',
    'smem':  'SUPERVISOR_MEMORY',
    'umem':  'USER_MEMORY',
    'chdev': 'channel_device',
    'hdds':  'LOAD_PROGRAM_FROM_HDD_TO_SUPERVISOR_MEMORY',
    'hdds+': 'LOADED_PROGRAM_FROM_HDD_TO_SUPERVISOR_MEMORY',
    'su':    'LOAD_PROGRAM_FROM_SUPERVISOR_MEMORY_TO_USER_MEMORY',
    'su+':   'LOADED_PROGRAM_FROM_SUPERVISOR_MEMORY_TO_USER_MEMORY',
    'ts':    'TASK_IS_IN_SUPERVISOR_MEMORY',
    'uif':   'USER_INTERFACE',
    'non':   'NONEXISTENT',
    'sin':   'STRING_IS_IN_SUPERVISOR_MEMORY',
    'fint':  'FROM_INTERRUPT',
    'ui':    'USER_INPUT'
}
