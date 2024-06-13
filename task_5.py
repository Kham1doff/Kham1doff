def dict_to_list_dict(input_dict, n):
    output_dict = {}
    for key, value in input_dict.items():
        output_dict[key] = [value] * n
    return output_dict

input_dict = {'a': 1, 'b': 2}
p = 3
output_dict = dict_to_list_dict(input_dict, p)
print(output_dict)
