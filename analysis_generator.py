from java_variable_code_generator import JavaVariableCodeGenerator, write_class_to_file, get_v_list



v_names1 = [
    'sampleWeight'
]
f1 = JavaVariableCodeGenerator(
    v_type='SimpleObjectProperty<Double>', io_type='Double',
    get_method='getValue',
    set_method='setValue',
    instance_init_value='0.0'
)



v_names2 = [
    'monomateriale', 'traccianti', 'frazioniEstranee', 'altreFE',
]
f2 = JavaVariableCodeGenerator(
    'Category', have_set=False, instance_init_value='this'
)



v_names3 = [
    'imballagi', 'industriali', 'umido', 'vetro',
    'medicinali', 'alluminioAcciaio', 'frazioniFine2x2',
    'raee', 'legno', 'inerti', 'tessuti',
]
f3 = JavaVariableCodeGenerator(
    'Waste', have_set=False, instance_init_value='this'
)



v_lists = [
    get_v_list(v_names1, f1),
    get_v_list(v_names2, f2),
    get_v_list(v_names3, f3),
]
write_class_to_file('build/Analysis.txt', 'Analysis', v_lists, package_name='myapps.data')