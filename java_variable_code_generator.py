
'''
TODO: una variabile puo essere da inizializzare -> new 
oppure puo essere passata come parametro nel costruttore

TODO: 
se la variabile ha un set_method e un wrapper (il metodo serve per ricavare il valore)
se ha have_set / have_get: si riferiscono alla variabile stessa, cosi com e.

TODO: 
creare una classe python: JavaClassGenerator

TODO:
simple getters or setters could be written in one single line:
    public Rifiuto getImballagi() { return imballagi; }

'''


class JavaVariableCodeGenerator:
    
    def __init__(self,
                v_type,
                visibility='private',
                name='factory', io_type=None, 
                get_method=None, have_get=True, 
                set_method=None, have_set=True,
                instance_init_value=None,
                ):
        self.visibility = visibility
        self.v_type = v_type
        self.name = name
        self.name2 = name[0].upper() + name[1:]
        self.get_method = get_method 
        self.set_method = set_method
        self.io_type = io_type
        self.have_get = have_get
        self.have_set = have_set
        self.instance_init_value = instance_init_value
    
    def get_variable_delcaration(self):
        return "\t" + self.visibility + ' ' + self.v_type + ' ' + self.name + ';\n'
        
    def generate_variable(self, name):
        v = JavaVariableCodeGenerator(
            v_type=self.v_type, name=name, io_type=self.io_type,
            get_method=self.get_method, have_get=self.have_get,
            set_method=self.set_method, have_set=self.have_set,
            instance_init_value=self.instance_init_value
        )
        return v
        

    def getter_code(self):
        if self.have_get is False:
            return ''
        
        return_type = ''
        if self.io_type is not None:
            return_type = self.io_type
        else: 
            return_type = self.v_type

        if self.get_method is None and self.io_type is None:
            return f'\tpublic {return_type} get{self.name2}() {{ return {self.name}; }}\n'
        if self.get_method is None:
            return f'\tpublic {return_type} get{self.name2}() {{ return this.{self.name}; }}\n'
        else:
            return f'\tpublic {return_type} get{self.name2}() {{ return {self.name}.{self.get_method}(); }}\n'

            
    def setter_code(self):
        if self.have_set is False:
            return ''
                    
        if self.set_method is None and self.io_type is None:
            return  ''
        if self.set_method is None:
            return f'\tpublic void set{self.name2}({self.io_type} value) {{ this.{self.name} = value; }}\n'

        else:
            return f'\tpublic void set{self.name2}({self.io_type} value) {{ {self.name}.{self.set_method}(value); }}\n'

            
    def generate_var_allocation_code(self):
        init_value = ''
        if self.instance_init_value is not None:
            init_value = self.instance_init_value
        return f'{self.name} = new {self.v_type}({init_value});\n'
            
    def accessor_code(self):
        return self.getter_code() + self.setter_code() +'\n'


def write_class_to_file(filename, classname, v_lists, package_name=None):
    code = ''
    with open(filename, 'w') as file:
        if package_name is not None:
            code += 'package ' + package_name + ';\n'

        code += '\npublic class '+classname+' {\n'
        constructor_code = f'\tpublic {classname}(){{\n'
        
        for v_list in v_lists:
            for v in v_list:
                code += v.get_variable_delcaration()
                constructor_code += '\t\t' + v.generate_var_allocation_code()
            code += '\n'
            constructor_code += '\n'
        constructor_code += '\t}\n'
        code += '\n\n'
        
        code += constructor_code
        code += '\n\n'
        
        for v_list in v_lists:
            for v in v_list: 
                code += v.accessor_code()            
            
        code += "\n}"
        file.write(code)
        
    file.close()
        
def get_v_list(v_names, factory):
    v_list = []
    for v_name in v_names:
        v_list.append(factory.generate_variable(v_name))
    return v_list

