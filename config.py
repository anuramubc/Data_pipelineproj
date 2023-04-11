#Config.py to externalize the code to add the database connection infomration
# Info for source database
import os
#Using dictionary to provide details about the source database
DB_DETAILS = {
    'dev' :{
    'SOURCE_DB' :{
            'DB_TYPE' : 'mysql',
            'DB_HOST' : ' Vijays-MacBook-Pro-2.local',
            'DB_NAME' : 'retail_db',
            'DB_USER' : 'root',
            'DB_PASS' : 'Netflix@2019'
        },
    'TARGET_DB' :{
            'DB_TYPE' : 'mysql',
            'DB_HOST' : ' Vijays-MacBook-Pro-2.local',
            'DB_NAME' : 'retail_db2',
            'DB_USER' : 'root',
            'DB_PASS' : 'Netflix@2019'
        }
    }

}