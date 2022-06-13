from pprint import pprint
from multiprocessing import Pool, Queue

from faker.config import AVAILABLE_LOCALES
import pandas as pd


def csv_data_generator(names):
    # function will be used in multiprocessing so import sratemen inside function

    from datetime import date

    from faker import Faker
    import pandas as pd

    file_name = file_name_queue.get()
    rows = []
    no_of_rows, duplicate_pid, iteration  = 0, None, 0
    columns = ['Product ID', 'First Name', 'Middle Name', 'Last Name', 'Date of Order']
    
    fake = Faker(csv_data_generator.locales)
    
    start_date = date(1990, 3,14)
    end_date = date(2011, 8, 29)
    dates = [fake.date_between_dates(date_start = start_date, date_end = end_date) for _ in range (fake.randomize_nb_elements(number= 25)) ]
    
    for name in names:
        for date in dates:
            orders = fake.randomize_nb_elements(number = 20)
            same_order = False

            for _ in range(orders):
                iteration += 1
                row = []
                pid = fake.bothify('TID-??##-?#?')
                if iteration % 500 == 0: duplicate_pid, same_order = pid, True
                if duplicate_pid != None and same_order == False:
                    pid = duplicate_pid
                    duplicate_pid = None
                
                row.append(pid)
                row.extend(name)
                row.append(date)

                rows.append(row)
                

                
    df = pd.DataFrame(rows, columns = columns)
    df.to_csv(file_name, index = False, date_format = '%d/%m/%Y')
    
    print ("1 file over")
    return df.shape[0]

def csv_init(queue):
    csv_data_generator.file_name_queue = queue
    AVAILABLE_LOCALES.pop(41)
    csv_data_generator.locales = AVAILABLE_LOCALES


def add_file_name(queue, no_of_files):
    for _  in range(no_of_files):
        queue.put('../outputs/input_chunks/input_data_' + str(_) + '.csv')


if __name__ == "__main__":
    
    rows = 100
    chunk_size = 100
    names_chunks = pd.read_csv('../inputs/name.csv', nrows = rows, chunksize = chunk_size)
    file_name_queue = Queue()
    
    with Pool(None, csv_init, [file_name_queue]) as pool:

        iterator = [chunk.values.tolist() for chunk in names_chunks]
        add_file_name(file_name_queue, len(iterator))
        rows_made_list =(pool.map(csv_data_generator, iterator))
        
        pprint(rows_made_list)
        print(sum(rows_made_list))

    '''file_name_queue.put("../outputs/test.csv")
    iterator = [chunk.values.tolist() for chunk in names_chunks]
    csv_init(file_name_queue)
    csv_data_generator(iterator[0])'''
