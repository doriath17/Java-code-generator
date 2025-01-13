from java_variable_code_generator import JavaVariableCodeGenerator, write_class_to_file, get_v_list

v_names1 = [
    'altreFE'
]

v_names2 = [
    'monomateriale', 'traccianti', 'frazioniEstranee', 'altreFE',
]

v_names3 = [
    'imballagi', 'industriali', 'umido', 'vetro',
    'medicinali', 'alluminioAcciaio', 'frazioniFine2x2',
    'raee', 'legno', 'inerti', 'tessuti',
]

cat1 = ['umido', 'vetro',
    'medicinali', 'alluminioAcciaio', 'frazioniFine2x2',
    'raee', 'legno', 'inerti', 'tessuti',]

# v_lists1 = get_v_list(v_names1, 'SimpleObjectProperty<Double>', io_type='Double', get_method='getValue', set_method='setValue', instance_init_value='0.0')
# v_lists2 = get_v_list(v_names2, 'Category', have_set=False)
# v_lists3 = get_v_list(v_names3, 'Waste', have_set=False, instance_init_value='this')

v_list = get_v_list(cat1, 'Waste', have_set=False, instance_init_value='this, frazioniEstraneeInstance()')

v_lists = [v_list]
write_class_to_file('build/Analysis.txt', 'Analysis', v_lists, package_name='myapps.reportanalisi.data')