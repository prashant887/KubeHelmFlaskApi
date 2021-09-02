import snowflake.connector
import os


class DbConnector:
    # This is to help initialize the DbConnector object
    def __init__(self, debug=False, logger=None):

        self.debug = debug
        self.connector = None
        self.logger = logger
        self.connection = None

        if debug:
            if self.logger:
                self.logger.logMsg('DbConnector object is created')
            print('DbConnector object is created')

        conn_args = {'user': os.getenv('USER').strip(),
                     'password': os.getenv('PASSWD').strip(),
                     'account': os.getenv('ACC').strip(),
                     'database': os.getenv('DB').strip(),
                     'warehouse': os.getenv('WH').strip(),
                     'role': os.getenv('ROLE').strip(),
                     'schema': os.getenv('SCHEMA').strip()
                     }
        """
        conn = {'account': 'jd98257.canada-central.azure', 'user': 'prashant887', 'password': 'prashantL@887',
                'warehouse': 'COMPUTE_WH', 'database': 'DEMO_DB', 'schema': 'PUBLIC', 'role': 'ACCOUNTADMIN'}
        """
        try:
            self.connection = snowflake.connector.connect(**conn_args)
            # self.connection = snowflake.connector.connect(**conn)
        except Exception as e:
            if self.logger:
                self.logger.logError('The snowflake db connection could not be established - ' + str(e))
            raise Exception('The snowflake db connection could not be established - ' + str(e))

    def execute_sql(self, sql=None):
        try:
            if self.debug:
                if self.logger:
                    self.logger.logMsg('DbConnector execute_sql method is called')

            if not sql:
                if self.logger:
                    self.logger.logError('The passed in sql string is empty')
                raise Exception('The passed in sql string is empty')

            if not self.connection:
                if self.logger:
                    self.logger.logError('The snowflake db connection does not exist, try connecting to db again')
                raise Exception('The snowflake db connection does not exist, try connecting to db again')

            return self.connection.cursor().execute(sql)
        except Exception as e:
            if self.logger:
                self.logger.logError("The sql statement could not be executed successfully - " + str(e))
            raise Exception("The sql statement could not be executed successfully - " + str(e))

    # This method can be called to close the snowflake connection gracefully
    def close_connection(self):
        if self.debug:
            if self.logger:
                self.logger.logMsg('DbConnector close_connection method is called')

        if self.connection is not None:
            self.connection.close()

        if self.debug:
            if self.logger:
                self.logger.logMsg('DbConnector connection is closed successfully')
