from collections import namedtuple

DatasetDef = namedtuple('Dataset', ['compound', 'concentration', 'proteome', 'activation_state', 'links'])

datasets = [
    DatasetDef('KB02', 500, 'sol', False, ['G1_500/Tcells1_1_080418_Tcells_exp_sol_KB02_500_V_12A', 'G1_500/Tcells1_1_082817_Tcells_sol_KB02_IV_39D', 'G1_500/Tcells1_1_082917_Tcells_exp_sol_KB02_IV_39E']),
    DatasetDef('KB02', 500, 'sol', True,  ['G1_500/Tcells1_2_071318_Tcells_act_sol_KB02_500_V_7I', 'G1_500/Tcells1_2_092417_Tcells_act_sol_KB02_500_IV_61B', 'G1_500/Tcells1_2_101417_Tcells_act_sol_KB02_500_IV_64C']),
    DatasetDef('KB02', 500, 'mem', False, ['G1_500/Tcells1_3_080418_Tcells_exp_mem_KB02_500_V_12B', 'G1_500/Tcells1_3_083017_Tcells_exp_mem_KB02_IV_40C', 'G1_500/Tcells1_3_083017_Tcells_mem_KB02_IV_40B']),
    DatasetDef('KB02', 500, 'mem', True,  ['G1_500/Tcells1_4_071318_Tcells_act_mem_KB02_500_V_7J', 'G1_500/Tcells1_4_092517_Tcells_act_mem_KB02_500_IV_61D']),
    DatasetDef('KB05', 500, 'sol', False, ['G1_500/Tcells1_5_011718_Tcells_exp_53F_sol_KB05_500_IV_80A', 'G1_500/Tcells1_5_122617_Tcells_exp_sol_KB05_500_IV_77A', 'G1_500/Tcells1_5_122617_Tcells_naive_sol_KB05_500_IV_77B']),
    DatasetDef('KB05', 500, 'sol', True,  ['G1_500/Tcells1_6_081718_Tcells_act_sol_KB05_500_V_15A', 'G1_500/Tcells1_6_092017_Tcells_act_sol_KB05_500_IV_61A', 'G1_500/Tcells1_6_101217_Tcells_act_sol_KB05_500_IV_64A']),
    DatasetDef('KB05', 500, 'mem', False, ['G1_500/Tcells1_7_081318_Tcells_exp_mem_KB05_500_V_12D', 'G1_500/Tcells1_7_022218_Tcells_exp_53F_mem_KB05_500_IV_80B']),
    DatasetDef('KB05', 500, 'mem', True,  ['G1_500/Tcells1_8_081818_Tcells_act_mem_KB05_500_V_15C', 'G1_500/Tcells1_8_092117_Tcells_act_mem_KB05_500_IV_61C', 'G1_500/Tcells1_8_11012017_Tcells_act_KB05_500_mem_IV_64G']),

    DatasetDef('KB02', 100, 'sol', False, ['G2_100/Tcells2_1_030618_Tcells_exp_sol_KB02_100_IV_87J', 'G2_100/Tcells2_1_070518_Tcells_naive_KB02_100_sol_V_7E', 'G2_100/Tcells2_1_112517_Tcells_35F_sol_KB02_100_ekk_195C']),
    DatasetDef('KB02', 100, 'sol', True,  ['G2_100/Tcells2_2_080318_Tcells_act_sol_KB02_100_V_9A', 'G2_100/Tcells2_2_101617_Tcells_act_sol_KB02_100_IV_64B', 'G2_100/Tcells2_2_112317_Tcells_act_sol_KB02_100_ekk_195A']),
    DatasetDef('KB02', 100, 'mem', False, ['G2_100/Tcells2_3_030618_Tcells_exp_mem_KB02_100_IV_87I', 'G2_100/Tcells2_3_071218_Tcells_naive_mem_KB02_100_V_7G', 'G2_100/Tcells2_3_112517_Tcells_35F_mem_KB02_100_ekk_195D']),
    DatasetDef('KB02', 100, 'mem', True,  ['G2_100/Tcells2_4_081318_Tcells_act_mem_KB02_100_V_9B', 'G2_100/Tcells2_4_112317_Tcells_act_mem_KB02_100_ekk_195B', 'G2_100/Tcells2_4_10312017_Tcells_act_KB02_100_mem_IV_64F']),
    DatasetDef('KB05', 100, 'sol', False, ['G2_100/Tcells2_5_030518_Tcells_exp_sol_KB05_100_ekk_198E', 'G2_100/Tcells2_5_071118_Tcells_naive_sol_KB05_100_V_7F', 'G2_100/Tcells2_5_071718_Tcells_exp_sol_KB05_100_V_7K']),
    DatasetDef('KB05', 100, 'sol', True,  ['G2_100/Tcells2_6_081818_Tcells_act_sol_KB05_100_V_15B', 'G2_100/Tcells2_6_101517_Tcells_act_sol_KB05_100_IV_64D', 'G2_100/Tcells2_6_112617_Tcells_act_sol_KB05_100_ekk_195J']),
    DatasetDef('KB05', 100, 'mem', False, ['G2_100/Tcells2_7_022218_Tcells_exp_53F_mem_KB05_100_IV_80C', 'G2_100/Tcells2_7_030518_Tcells_exp_mem_KB05_100_ekk_198F_rep', 'G2_100/Tcells2_7_071218_Tcells_naive_mem_KB05_100_V_7H', 'G2_100/Tcells2_7_071718_Tcells_exp_mem_KB05_100_V_7L']),
    DatasetDef('KB05', 100, 'mem', True,  ['G2_100/Tcells2_8_081918_Tcells_act_mem_KB05_100_V_15D', 'G2_100/Tcells2_8_112717_Tcells_act_mem_KB05_100_ekk_195K', 'G2_100/Tcells2_8_11012017_Tcells_act_KB05_100_mem_IV_64H']),

    DatasetDef('KB02', 50, 'sol', False, ['G3_50_in_situ/Tcells3_1_081418_Tcells_exp_sol_KB02_50_insitu_V_12E', 'G3_50_in_situ/Tcells3_1_032518_Tcells_exp_39M_sol_insitu_KB02_50_IV_89A', 'G3_50_in_situ/Tcells3_1_04142018_Tcells_exp_sol_KB02_50_insitu_IV_95A', 'G3_50_in_situ/Tcells3_1_04172018_Tcells_exp_37M_sol_KB02_50_insitu_IV_95D', 'G3_50_in_situ/Tcells3_1_111517_Tcells_21M_exp_sol_KB02_50_insitu_IV_74B']),
    DatasetDef('KB02', 50, 'sol', True,  ['G3_50_in_situ/Tcells3_2_030918_Tcells_act_sol_insitu_KB02_50_IV_75L', 'G3_50_in_situ/Tcells3_2_033018_Tcells_act_27F_sol_KB02_ekk_223A', 'G3_50_in_situ/Tcells3_2_113017_Tcells_27F_act_sol_KB02_insitu_50_IV_75K']),
    DatasetDef('KB02', 50, 'mem', False, ['G3_50_in_situ/Tcells3_3_081418_Tcells_exp_mem_KB02_50_insitu_V_12F', 'G3_50_in_situ/Tcells3_3_04232018_Tcells_exp_37M_mem_KB02_50_insitu_IV_95I', 'G3_50_in_situ/Tcells3_3_112017_Tcells_21M_exp_mem_KB02_50_insitu_IV_74P']),
    DatasetDef('KB02', 50, 'mem', True,  ['G3_50_in_situ/Tcells3_4_033018_Tcells_act_27F_mem_KB02_ekk_223B', 'G3_50_in_situ/Tcells3_4_04042018_Tcells_act_27F_mem_insitu_KB02_50_IV_75S', 'G3_50_in_situ/Tcells3_4_111817_Tcells_act_mem_KB02_50_insitu_IV_74Q', 'G3_50_in_situ/Tcells3_4_120117_Tcells_27F_act_mem_KB02_insitu_50_IV_75R']),
    DatasetDef('KB05', 50, 'sol', False, ['G3_50_in_situ/Tcells3_5_04212018_Tcells_exp_sol_KB05_50_insitu_IV_95B', 'G3_50_in_situ/Tcells3_5_111617_Tcells_47F_exp_sol_KB05_50_insitu_IV_74F', 'G3_50_in_situ/Tcells3_5_111717_Tcells_naive_sol_KB05_50_insitu_IV_74I']),
    DatasetDef('KB05', 50, 'sol', True,  ['G3_50_in_situ/Tcells3_6_010218_Tcells_act_sol_KB05_50_insitu_IV_78G', 'G3_50_in_situ/Tcells3_6_111717_Tcells_act_sol_KB05_50_insitu_IV_74D']),
    DatasetDef('KB05', 50, 'mem', False, ['G3_50_in_situ/Tcells3_7_04232018_Tcells_exp_mem_KB05_50_insitu_IV_95G', 'G3_50_in_situ/Tcells3_7_111917_Tcells_21M_naive_mem_KB05_50_insitu_IV_74M', 'G3_50_in_situ/Tcells3_7_111917_Tcells_47F_expmem_KB05_50_insitu_IV_74T']),
    DatasetDef('KB05', 50, 'mem', True,  ['G3_50_in_situ/Tcells3_8_010318_Tcells_act_mem_KB05_50_insitu_IV_78J', 'G3_50_in_situ/Tcells3_8_111817_Tcells_27M_act_mem_KB05_50_insitu_IV_74R']),
    # DatasetDef('IA', '10_100', 'sol', False, ['G4: HR/Tcells1_04222018_Tcells_exp_sol_HR_IV_95E', 'G4: HR/Tcells1_04242018_Tcells_naive_sol_HR_IV_92H', 'G4: HR/Tcells1_230218_Tcells_exp_39M_sol_HR_IV_87A']),
    # DatasetDef('IA', '10_100', 'sol', True,  ['G4: HR/Tcells2_040218_Tcells_act_27F_sol_HR_IV_83K', 'G4: HR/Tcells2_040218_Tcells_act_D2_sol_HR_IV_83M', 'G4: HR/Tcells2_220318_Tcells_act_28F_sol_HR_IV_89L']),
    # DatasetDef('IA', '10_100', 'mem', False, ['G4: HR/Tcells3_04222018_Tcells_exp_mem_HR_IV_95J', 'G4: HR/Tcells3_04262018_Tcells_naive_mem_HR_IV_92I', 'G4: HR/Tcells3_04302018_Tcells_naive_mem_HR_IV_89O']),
    # DatasetDef('IA', '10_100', 'mem', True,  ['G4: HR/Tcells4_04302018_Tcells_act_mem_HR_IV_89P', 'G4: HR/Tcells4_070218_Tcells_act_27F_mem_HR_IV_83N', 'G4: HR/Tcells4_080218_Tcells_act_D2_HR_mem_IV_83P']),
]
