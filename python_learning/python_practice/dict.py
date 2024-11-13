# NESTED DICTIONARY WITH INDEXING:
# dict ={'Dict1' : {'A' : 'ali' , 'B' : 'khadim' , 'C' : 'usama'},
#        'Dict2' : {1 : 'hayat' , 2 : 'zoya' , 3 : 'maha'},
#        'Dict3' : {1 : 'apple' , 2 : 'cherry' , 3 : 'pear'}}
# print("original Dictionary :", dict)
# print(dict['Dict3'])
# print(dict['Dict3'][1])
# print(dict['Dict3'][2])
# print(dict['Dict3'][3])
# # USER INPUT:
# user_dict = {}
# for i in range(5):
#     key = input(f'enter key {i + 1}:')
#     value = input(f'enter value{i + 1}:')
#     user_dict[key] = value
# print('\nUser_Dictionary:')
# print(user_dict)
# IMPORT DICT:
# from typing import Dict, Union, Optional
# import pprint

# Key = Union[int,str]
# Value = Union[int, str, list, dict, tuple, set]

# # List                    0                1            2
# data : Dict[Key,Value] = {
#                         "fname":"Muhammad Aslam",
#                         "name":"Muhammad Qasim",
#                         "education": "MSDS",
#                         "abc" : [1,2,3],
#                         'xyz': {1,2,3},
#                         'efg' : (1,2,3),
#                         'cde' : {"a":1, "b":2}
#                         # [1,2,3] : "Pakistan", # error
#                         # (1,2,3) : "Pakistan", #error
#                         # {1,2,3} : "pakistan", #error
#                         }

# pprint.pprint(data)
# print(data["name"])
# print(data['fname'])

# print(data['xyz'])
# print(data['education'])



# from nptyping import NDArray , shape 
# import numpy as np
# from typing import

# arr1:NDArray[shape['10'],`Any] = np.array([1,2,3,4,5,6,7,8,9,10])
# print(arr1)



# from nptyping import NDArray , shape 
# import numpy as np
# from typing import

# arr1:NDArray[shape['10'],`Any] = np.array([1,2,3,4,5,6,7,8,9,10])
# print(arr1)

# from nptyping import NDArray , shape 
# import numpy as np
# from typing import

# arr1:NDArray[shape['10'],`Any] = np.array([1,2,3,4,5,6,7,8,9,10])
# print(arr1)

# import pandas as pd
# fruits_series = pd.Series(fruits)
# print(fruits_series)