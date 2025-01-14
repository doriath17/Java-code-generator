from java_variable_code_generator import JavaVariableCodeGenerator, write_class_to_file, get_v_list

v_names = [
    'pesoLordo', 'pesoTara', 'pesoNetto'
]
factory = JavaVariableCodeGenerator(
    v_type='SimpleObjectProperty<Double>', io_type='Double',                  
    set_method='setValue', get_method='getValue',
    instance_init_value='0.0',
)

v_list1 = get_v_list(v_names, factory)

v_list2 = [JavaVariableCodeGenerator(v_type='CategoriaRifiuto', name='categoria',have_set=False, have_get=False)]
v_list3 = [JavaVariableCodeGenerator(v_type='Analisi', name='currentAnalisi',have_set=False, have_get=False)]


v_lists = [v_list1, v_list2, v_list3]
write_class_to_file('build/Rifiuto.java', 'Rifiuto', v_lists, package_name='myapps.data')