import numpy as np

def entroy_many_factor_e_void(area_solid, area_total):
    area_void = area_total - area_solid
    return (-1*(area_void/ area_total)) * (np.log2(area_void / area_total))