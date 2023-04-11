#importing information of source database from config.py
#sys: exposes all information passed to this script during runtime
#include sys if using environment variables
import sys

#import DB_DETAILS from config.py to get the info of the source database
from config import DB_DETAILS
#import get_tables from util.py to get the tables to be loaded from the table_list.txt
from util import get_tables, load_db_details
from read import read_table
from write import load_table

def main():
   db_details = load_db_details('dev')
   tables = get_tables('tables_list')
   for table_name in tables['table_name']:
    print('read table from {}'.format(table_name))
    data, column_name = read_table(db_details, table_name)
    print('write table to {}'.format(table_name))
    load_table(db_details, data, column_name, table_name)

if __name__ == '__main__':
    main()