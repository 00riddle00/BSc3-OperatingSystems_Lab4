from Utils import *


class Resources:

    resources = {
        RES_USER_INTERFACE:                  0,
        RES_STR_IN_MEM:                      0,
        RES_SUPERVISOR_MEM:                  0,
        RES_CHN_DEVICE:                      1,
        RES_HDD_TO_SUPERVISOR_MEM:          '',
        RES_HDD_TO_SUPERVISOR_MEM_FIN:       0,
        RES_TASK_IN_SUPERVISOR_MEM:          0,
        RES_USER_MEM:                        0,
        RES_SUPERVISOR_MEM_TO_USER_MEM:     '',
        RES_SUPERVISOR_MEM_TO_USER_MEM_FIN:  0,
        RES_USER_INPUT:                      0,
        RES_FROM_INTERRUPT:                  0,
        RES_NONEXISTENT:                     0,
        RES_MOS_END:                         0,
    }

    def __getitem__(self, key):
        if key not in self.resources.keys():
            raise KeyError

        return self.resources[key]

    def __setitem__(self, key, value):
        if key not in self.resources.keys():
            raise KeyError

        self.resources[key] = value

    def free(self, key, value=None):
        if key not in self.resources.keys():
            raise KeyError

        if not value:
            value = 1

        self.resources[key] = value

    def check(self, key, value=None):
        if key not in self.resources.keys():
            raise KeyError

        if not value:
            value = 1

        return self.resources[key] == value
