class ReportProp:

    def __init__(self, filename: str):
        self.filename = filename
        self.obj_id: str = None
        self.found = {}
        self.router = {}
        self.router['OBJECT'] = self.__proc_object
        self.router['    ProcessingOnly=Yes'] = self.__proc_specified_property
        self.router['    Modified=Yes'] = self.__proc_specified_property


    def do_nothing(self, source_line: str = None):
        pass


    def __proc_object(self, source_line: str = None):
        if source_line is None:
            raise ValueError('Where is my source code?!')
        self.obj_id = None
        words = source_line.split(' ', 3)
        if words[1] == 'Report':
            self.obj_id = words[2]        


    def __proc_specified_property(self, source_line: str = None):
        if self.obj_id is not None:
            self.found[self.obj_id] = self.found.get(self.obj_id, 0) + 1        


    def run(self):
        with open(self.filename, 'r', encoding='cp866') as fi:
            for line in fi:
                # prop = list(filter(lambda r: line.startswith(r), self.router.keys())) 
                # self.router.get(prop[0] if prop else 'XXX', self.do_nothing)(line)
                if prop := list(filter(lambda r: line.startswith(r), self.router.keys())):
                    self.router[prop[0]](line)


    def get_result(self, print_to_file: str = None):
        if print_to_file is None:
            print ('\n'.join([key for key, val in self.found.items() if val == 2])) 
        else:           
            with open(print_to_file, "w") as fo:
                fo.write('\n'.join([key for key, val in self.found.items() if val == 2]))


rep = ReportProp('c:/temp/naCLDev_20200924.txt')
rep.run()
#rep.get_result("C:/temp/result2.txt")
rep.get_result()
