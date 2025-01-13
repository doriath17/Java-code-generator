class JavaVariableCodeGenerator:
    
    def __init__(self, var_type: str, name: str, io_type=None, 
                get_method=None, have_get=True, set_method=None, have_set=True, 
                instance_init_value=None):
        self.var_type = var_type
        self.name = name
        self.name2 = name[0].upper() + name[1:]
        self.get_method = get_method 
        self.set_method = set_method        
        self.io_type = io_type
        self.have_get = have_get
        self.have_set = have_set
        self.instance_init_value = instance_init_value
    
    def get_variable_delcaration(self):
        return "\t" + self.var_type + " " + self.name + ";\n"

    def getter_code(self):
        if self.have_get is False:
            return ''
        
        return_type = ''
        if self.io_type is not None:
            return_type = self.io_type
        else: 
            return_type = self.var_type
                    
        if self.get_method is None and self.io_type is None:
            return  (
                f'\tpublic {return_type} get{self.name2}(){{\n'
                f'\t\treturn {self.name}Instance();\n'
                f'\t}}\n\n'
            )
        if self.get_method is None:
            return  (
                f'\tpublic {return_type} get{self.name2}(){{\n'
                f'\t\treturn this.{self.name};\n'
                f'\t}}\n\n'
            )
        else:
            return (
                f'\tpublic {return_type} get{self.name2}(){{\n'
                f'\t\treturn {self.name}Instance().{self.get_method}();\n'
                '\t}\n\n'
            )
            
    def setter_code(self):
        if self.have_set is False:
            return ''
                    
        if self.set_method is None and self.io_type is None:
            return  ''
        if self.set_method is None:
            return  (
                f'\tpublic void set{self.name2}({self.io_type} value){{\n'
                f'\t\tthis.{self.name} = value;\n'
                f'\t}}\n\n'
            )
        else:
            return (
                f'\tpublic void set{self.name2}({self.io_type} value){{\n'
                f'\t\t{self.name}Instance().{self.set_method}(value);\n'
                '\t}\n\n'
            )
            
    def generate_var_allocation_code(self):
        init_value = ''
        if self.instance_init_value is not None:
            init_value = self.instance_init_value
        return f'{self.name} = new {self.var_type}({init_value});'
            
    def accessor_code(self):
        return self.getter_code() + self.setter_code() +'\n\n'
        



def write_class_to_file(filename, classname, v_lists, package_name=None):
    code = ''
    with open(filename, 'w') as file:
        if package_name is not None:
            code += 'package ' + package_name + ';\n'

        code += '\npublic class '+classname+' {\n'
        
        for v_list in v_lists:
            for v in v_list: 
                code += v.get_variable_delcaration()
            code += '\n'
        
        code += '\n\n'
        
        for v_list in v_lists:
            for v in v_list: 
                code += v.accessor_code()            
            
        code += "\n}"
        file.write(code)
        
    file.close()
        
def get_v_list(v_names, v_type: str, io_type=None, get_method=None, have_get=True, set_method=None, have_set=True, instance_init_value=None):
    v_list = []
    for v_name in v_names:
        v_list.append(JavaVariableCodeGenerator(v_type, v_name, io_type=io_type, get_method=get_method, set_method=set_method, instance_init_value= instance_init_value))
    return v_list

