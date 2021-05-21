import Utils as ut


class ResourcesTest:
    resources = {
        ut.RES['mend']:   0,
        ut.RES['smem']:   0,
        ut.RES['umem']:   0,
        ut.RES['chdev']:  0,
        ut.RES['hdds']:  '',
        ut.RES['hdds+']:  0,
        ut.RES['su']:    '',
        ut.RES['su+']:    0,
        ut.RES['ts']:     0,
        ut.RES['uif']:    0,
        ut.RES['non']:    0,
        ut.RES['sin']:    0,
        ut.RES['fint']:   0,
        ut.RES['ui']:     0
    }

    def __getitem__(self, key):
        if key not in self.resources.keys():
            raise KeyError

        return self.resources[key]

    def __setitem__(self, key, value):
        if key not in self.resources.keys():
            raise KeyError

        self.resources[key] = value


class Resources:
    res_mos_end = 0
    res_supervisor_mem = 0
    res_user_mem = 0
    res_channel_dev = 1
    res_load_prog_hdd_to_smem = ''
    res_load_fin_hdd_to_smem = 0
    res_load_prog_smem_to_umem = ''
    res_load_fin_smem_to_umem = 0
    res_task_in_smem = 0
    res_user_interface = 0
    res_nonexistant = 0
    res_string_in_smem = 0
    res_from_interrupt = 0
    res_interrupt = 0
    res_user_input = 0
#
#     def resources_initialization(self):
#         self.res_mos_end = 0
#         self.res_supervisor_mem = 1
#         self.res_user_mem = 1
# #         sukuriam/pakeiciam reikiamus resursus


    #############################
    # set_resources
    #############################
    def set_res_mos_end(self, value):
        self.res_mos_end = value
    def set_supervisor_mem(self, value):
        self.res_supervisor_mem = value
    def set_res_user_mem(self, value):
        self.res_user_mem = value
    def set_res_channel_dev(self, value):
         self.res_channel_dev = value
    def set_res_load_prog_hdd_to_smem(self, value):
        self.res_load_prog_hdd_to_smem = value
    def set_res_load_fin_hdd_to_smem(self, value):
        self.res_load_fin_hdd_to_smem = value
    def set_res_load_prog_smem_to_umem(self, value):
        self.res_load_prog_smem_to_umem = value
    def set_res_load_fin_smem_to_umem(self, value):
        self.res_load_fin_smem_to_umem = value
    def set_res_task_in_smem(self, value):
        self.res_task_in_smem = value
    def set_res_user_interface(self, value):
        self.res_user_interface = value
    def set_res_nonexistant(self, value):
        self.res_nonexistant = value
    def set_res_string_in_smem(self, value):
        self.res_string_in_smem = value
    def set_res_from_interrupt(self, value):
         self.res_from_interrupt = value
    def set_res_interrupt(self, value):
        self.res_interrupt = value
    def set_res_user_input(self, value):
        self.res_user_input = value

    #############################
    # get_resources
    #############################
    def get_res_mos_end(self):
        return  self.res_mos_end
    def get_res_supervisor_mem(self):
        return  self.res_supervisor_mem
    def get_res_user_mem(self):
        return  self.res_user_mem
    def get_res_channel_dev(self):
        return  self.res_channel_dev
    def get_res_load_prog_hdd_to_smem(self):
        return  self.res_load_prog_hdd_to_smem
    def get_res_load_fin_hdd_to_smem(self):
        return  self.res_load_fin_hdd_to_smem
    def get_res_load_prog_smem_to_umem(self):
        return  self.res_load_prog_smem_to_umem
    def get_res_load_fin_smem_to_umem(self):
        return  self.res_load_fin_smem_to_umem
    def get_res_task_in_smem(self):
        return  self.res_task_in_smem
    def get_res_user_interface(self):
        return  self.res_user_interface
    def get_res_nonexistant(self):
        return  self.res_nonexistant
    def get_res_string_in_smem(self):
        return  self.res_string_in_smem
    def get_res_from_interrupt(self):
        return  self.res_from_interrupt
    def get_res_interrupt(self):
        return  self.res_interrupt
    def get_res_user_input(self):
        return  self.res_user_input
