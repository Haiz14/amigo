import pandas as pd

import base_v1
import big_operations as bo

class AmigoController:
    def __init__(self, path_dict = dict(), take_input = False):
        if take_input == True:
            path_dict['input_df_path'] = input('Enter the path to input_df: ')
            path_dict['allow_list_path'] = input('Enter the path to allow_list: ')
            path_dict['exclude_list_path'] = input('Enter the path to exclude list: ')
            

        self.input_df = base_v1.read_pandas(path_dict['input_df_path'])
        self.allow_list_df = base_v1.read_pandas(path_dict['allow_list_path'])
        self.exclude_list_df = base_v1.read_pandas(path_dict['exclude_list_path'])

        self.clean_df = bo.return_clean_df(self.input_df, self.allow_list_df, self.exclude_list_df)



if __name__ == '__main__':
    path_dict = {'input_df_path': "../inputs/input.xlsx",
            'allow_list_path': "../inputs/allow_list.xlsx",
            'exclude_list_path': "../inputs/exclude_list.xlsx"}

    ac = AmigoController(path_dict)
    print(ac.clean_df)
