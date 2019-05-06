def inverse_dict(original_dict):
    """ return a new dictionary with original values as key and list of original keys as value
        :param original_dict: any desired dictionary
        :type original_dict:  dict
        :rtype: dict
    """
    out_dict = dict()
    for original_key in original_dict:
        original_value =  original_dict[original_key]
        if original_value in out_dict.keys():
            out_dict[original_value] += [original_key]
            out_dict[original_value].sort()
        else:
            out_dict[original_value] = [original_key]

    return out_dict


DICT_TEST_VECTOR = [
                    {1 : "a", 2 : "b", 3 : "a"},
                    {'I': 3, 'love': 3, 'self.py!': 2},
                   ]

for DICT in DICT_TEST_VECTOR:
    print("Original:")
    print(DICT)
    print("Inversed:")
    print(inverse_dict(DICT))