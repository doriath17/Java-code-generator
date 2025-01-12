from java_variable_code_generator import JavaVariableCodeGenerator, write_class_to_file, get_v_list

v_names = [
    'grossWeight', 'tareWeight', 'netWeight'
]

v_list = get_v_list(v_names, v_type='SimpleObjectProperty<Double>', io_type='Double', get_method='getValue', set_method='setValue', instance_init_value='0.0')

v_lists = [v_list]
write_class_to_file('Waste.txt', 'Waste', v_lists, package_name='myapps.reportanalisi.data')