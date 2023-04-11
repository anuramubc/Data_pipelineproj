#importing information of source database from config.py
#sys: exposes all information passed to this script during runtime
#include sys if using environment variables
import sys

from config import DB_DETAILS


def main():
   db_details = DB_DETAILS['dev']
   print(db_details)

if __name__ == '__main__':
    main()