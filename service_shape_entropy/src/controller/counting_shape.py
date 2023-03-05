def counting_shape(array_of_type):

    array_3_square = []
    array_4_square = []
    array_5_square = []
    array_6_square = []
    array_7_square = []
    array_8_square = []

    counting_each_array_3 = {}
    counting_each_array_4 = {}
    counting_each_array_5 = {}
    counting_each_array_6 = {}
    counting_each_array_7 = {}
    counting_each_array_8 = {}

    total_leanght_3 = 0
    total_leanght_4 = 0
    total_leanght_5 = 0
    total_leanght_6 = 0
    total_leanght_7 = 0
    total_leanght_8 = 0

    for data in array_of_type:
        convert_width_height = [data['width'], data['height']]
        convert_to_label = str(convert_width_height)
        if data['shape_type'] == "3-square":
            total_leanght_3 += 1
            if convert_width_height in array_3_square:
                value_in_dict = counting_each_array_3[convert_to_label]
                counting_each_array_3[convert_to_label] = value_in_dict + 1
            else:
                array_3_square.append(convert_width_height)
                counting_each_array_3[convert_to_label] = 1

        elif data['shape_type'] == "4-square":
            total_leanght_4 += 1
            if convert_width_height in array_4_square:
                value_in_dict = counting_each_array_4[convert_to_label]
                counting_each_array_4[convert_to_label] = value_in_dict + 1
            else:
                array_4_square.append(convert_width_height)
                counting_each_array_4[convert_to_label] = 1

        elif data['shape_type'] == "5-square":
            total_leanght_5 += 1
            if convert_width_height in array_5_square:
                value_in_dict = counting_each_array_5[convert_to_label]
                counting_each_array_5[convert_to_label] = value_in_dict + 1
            else:
                array_5_square.append(convert_width_height)
                counting_each_array_5[convert_to_label] = 1
            
        elif data['shape_type'] == "6-square":
            total_leanght_6 += 1
            if convert_width_height in array_6_square:
                value_in_dict = counting_each_array_6[convert_to_label]
                counting_each_array_6[convert_to_label] = value_in_dict + 1
            else:
                array_6_square.append(convert_width_height)
                counting_each_array_6[convert_to_label] = 1

        elif data['shape_type'] == "7-square":
            total_leanght_7 += 1
            if convert_width_height in array_7_square:
                value_in_dict = counting_each_array_7[convert_to_label]
                counting_each_array_7[convert_to_label] = value_in_dict + 1
            else:
                array_7_square.append(convert_width_height)
                counting_each_array_7[convert_to_label] = 1

        elif data['shape_type'] == "8-square":
            total_leanght_8 += 1
            if convert_width_height in array_8_square:
                value_in_dict = counting_each_array_8[convert_to_label]
                counting_each_array_8[convert_to_label] = value_in_dict + 1
            else:
                array_8_square.append(convert_width_height)
                counting_each_array_8[convert_to_label] = 1

    return {
        "total_leanght_3":total_leanght_3,
        "total_leanght_4":total_leanght_4,
        "total_leanght_5":total_leanght_5,
        "total_leanght_6":total_leanght_6,
        "total_leanght_7":total_leanght_7,
        "total_leanght_8":total_leanght_8,
        "counting_each_array_3":counting_each_array_3, 
        "counting_each_array_4":counting_each_array_4, 
        "counting_each_array_5":counting_each_array_5, 
        "counting_each_array_6":counting_each_array_6, 
        "counting_each_array_7":counting_each_array_7, 
        "counting_each_array_8":counting_each_array_8
        }