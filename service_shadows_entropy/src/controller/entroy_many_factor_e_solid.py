import numpy as np

def entroy_many_factor_e_solid (area_solid, area_total):
    return (-1*(area_solid / area_total)) * (np.log2(area_solid / area_total ))
