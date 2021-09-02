from SnowflakeConnector import DbConnector
from flask import Flask, request, jsonify
from LoggingModule import GenericLogging
import json
import pandas as pd

app = Flask(import_name=__name__)

logger = GenericLogging()


@app.route("/")
def home():
    logger.logMsg("Calling Home Route")
    return jsonify('Home'), 200


@app.route("/getCustomers", methods=['GET'])
def getUsers():
    logger.logMsg("Calling Get getCustomers")
    sql = """select object_construct('CUSTOMER_ID',CUSTOMER_ID,'CUSTOMER_FNAME',CUSTOMER_FNAME,'CUSTOMER_LNAME',CUSTOMER_LNAME,
                       'CUSTOMER_EMAIL',CUSTOMER_EMAIL,'CUSTOMER_STREET',CUSTOMER_STREET,'CUSTOMER_CITY',CUSTOMER_CITY,'CUSTOMER_STATE',CUSTOMER_STATE,
                        'CUSTOMER_ZIPCODE',CUSTOMER_ZIPCODE
                       ) from customers limit 5;"""
    dbConn = DbConnector(True, logger)
    try:
        result = dbConn.execute_sql(sql)
        data = [json.loads(d[0]) for d in result.fetchall()]

    except Exception as e:
        logger.logError(str(e))
        data = str(e)
    finally:
        dbConn.close_connection()

    return jsonify(data), 200


@app.route("/getCustTab", methods=['GET'])
def getUserTable():
    logger.logMsg("Calling Get getCustTab")
    sql = """select * from customers;"""
    dbConn = DbConnector(True, logger)
    try:
        result = dbConn.execute_sql(sql)
        rows = pd.DataFrame(result.fetchall(), columns=['CUSTOMER_ID',
                                                        'CUSTOMER_FNAME',
                                                        'CUSTOMER_LNAME',
                                                        'CUSTOMER_EMAIL',
                                                        'CUSTOMER_PASSWORD',
                                                        'CUSTOMER_STREET',
                                                        'CUSTOMER_CITY',
                                                        'CUSTOMER_STATE',
                                                        'CUSTOMER_ZIPCODE'])
        dfhtml = rows.to_html()
    except Exception as e:
        logger.logError(str(e))
        dfhtml = str(e)
    finally:
        dbConn.close_connection()

    return dfhtml


@app.route("/getProdTab", methods=['GET'])
def getProdTable():
    logger.logMsg("Calling Get getProdTab")
    sql = """select b.CATEGORY_NAME,c.DEPARTMENT_NAME,a.PRODUCT_NAME,
a.PRODUCT_PRICE,
a.PRODUCT_IMAGE
from 
products a,categories b,departments c
where a.PRODUCT_CATEGORY_ID=b.CATEGORY_ID and b.CATEGORY_DEPARTMENT_ID=c.DEPARTMENT_ID
order by c.DEPARTMENT_NAME ,b.CATEGORY_NAME;"""
    dbConn = DbConnector(True, logger)
    try:
        result = dbConn.execute_sql(sql)
        rows = pd.DataFrame(result.fetchall(), columns=['CATEGORY_NAME','DEPARTMENT_NAME','PRODUCT_NAME','PRODUCT_PRICE','PRODUCT_IMAGE'])
        dfhtml = rows.to_html()
    except Exception as e:
        logger.logError(str(e))
        dfhtml = str(e)
    finally:
        dbConn.close_connection()

    return dfhtml


app.run(host='0.0.0.0', port=8080, debug=True)
