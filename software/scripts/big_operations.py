import pandas as pd
import numpy as np

ALPHABETS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

def return_clean_df(input_df = None, allow_list_df = None, exclude_list_df = None):


    input_df.columns = return_columns(len(input_df.columns))
    allow_list_df.columns = return_columns(len(allow_list_df.columns))
    exclude_list_df.columns = return_columns(len(exclude_list_df.columns))

    allowed_df = return_allowed_df(input_df, allow_list_df)

    clean_df = return_not_excluded_df(allowed_df, exclude_list_df)


    return clean_df


def return_allowed_df(input_df, include_list_df):
    allow_index = []
    for index, serie in include_list_df.iterrows():

        query = return_query(serie, '==')
        allow_index.extend( input_df.query(query).index)
    input_df = input_df.loc[list(set(allow_index))]

    return input_df


def return_not_excluded_df(input_df, exclude_list_df):
    drop_index = []

    for index, serie in exclude_list_df.iterrows():
        query = return_query(serie, '==')

        #print(query)
        #print(input_df.query(query).index)

        drop_index.extend(input_df.query(query).index
        #print(drop_index)
    input_df = input_df.drop(list(set(drop_index)))

    return input_df



def return_columns(no_of_columns):
    return(ALPHABETS[0:no_of_columns])

def return_query(serie, comparer):
    
    query = ''
    cnt = 0

    for index, item in serie.items():
        if pd.isna(item): continue
        
        elif cnt == 0:
            cnt = 1
            if type(item) == str:
                query += f"{index} {comparer} '{item}'"
                continue
                
            query += f"{index} {comparer} {item}"

        else: 
            if type(item) == str:
                query += f"{index} {comparer} '{item}'"
                continue
            query += f" and {index} {comparer} {item}"

    return query
        


def main():
    
    '''
    df = pd.DataFrame(np.random.randn(10, 4),
                              columns=['Col1', 'Col2', 'Col3', 'Col4'])
    '''

    rt = return_clean_df(pd.read_excel("../inputs/input.xlsx"),
        pd.read_excel("../inputs/allow_list.xlsx"),
        pd.read_excel("../inputs/exclude_list.xlsx"))

    print(rt)



if __name__ == "__main__":
    main()
