import numpy as np

def calculate_shapes_entropy(dict_in):
    # print(dict_in)
    entropy_shape3 = []
    entropy_shape4 = []
    entropy_shape5 = []
    entropy_shape6 = []
    entropy_shape7 = []
    entropy_shape8 = []

    sum_of_each_shape = []
    for i in dict_in['counting_each_array_3']:
        entropy_val = (-1*(dict_in['counting_each_array_3'][i] / dict_in['total_leanght_3'])) * (np.log2(dict_in['counting_each_array_3'][i] / dict_in['total_leanght_3']))
        # print("3 => ",entropy_val)
        entropy_shape3.append(entropy_val)
        
    for i in dict_in['counting_each_array_4']:
        entropy_val = (-1*(dict_in['counting_each_array_4'][i] / dict_in['total_leanght_4'])) * (np.log2(dict_in['counting_each_array_4'][i] / dict_in['total_leanght_4']))
        # print("4 => ",entropy_val)
        entropy_shape4.append(entropy_val)

    for i in dict_in['counting_each_array_5']:
        entropy_val = (-1*(dict_in['counting_each_array_5'][i] / dict_in['total_leanght_5'])) * (np.log2(dict_in['counting_each_array_5'][i] / dict_in['total_leanght_5']))
        # print("5 => ",entropy_val)
        entropy_shape5.append(entropy_val)

    for i in dict_in['counting_each_array_6']:
        entropy_val = (-1*(dict_in['counting_each_array_6'][i] / dict_in['total_leanght_6'])) * (np.log2(dict_in['counting_each_array_6'][i] / dict_in['total_leanght_6']))
        # print("6 => ",entropy_val)
        entropy_shape6.append(entropy_val)

    for i in dict_in['counting_each_array_7']:
        entropy_val = (-1*(dict_in['counting_each_array_7'][i] / dict_in['total_leanght_7'])) * (np.log2(dict_in['counting_each_array_7'][i] / dict_in['total_leanght_7']))
        # print("7 => ",entropy_val)
        entropy_shape7.append(entropy_val)

    for i in dict_in['counting_each_array_8']:
        entropy_val = (-1*(dict_in['counting_each_array_8'][i] / dict_in['total_leanght_8'])) * (np.log2(dict_in['counting_each_array_8'][i] / dict_in['total_leanght_8']))
        # print("8 => ",entropy_val)
        entropy_shape8.append(entropy_val)

    sum_of_each_shape.append(sum(entropy_shape3))
    sum_of_each_shape.append(sum(entropy_shape4))
    sum_of_each_shape.append(sum(entropy_shape5))
    sum_of_each_shape.append(sum(entropy_shape6))
    sum_of_each_shape.append(sum(entropy_shape7))
    sum_of_each_shape.append(sum(entropy_shape8))
    
    # print("sum_of_each_shape => ",sum_of_each_shape)

    avg_of_entropy_shape = np.mean(sum_of_each_shape)

    return avg_of_entropy_shape