import os
import pymysql
import dot
from datetime import datetime
## AWS RDS CONFIG START

#device_id = os.getenv('DEVICE_ID')
rds_host = os.getenv('RDS_URL')
rds_user = os.getenv('RDS_USER')
rds_pass = os.getenv('RDS_PASS')
rds_db = os.getenv('RDS_DB')


conn = pymysql.connect(host= rds_host,port = 3306,user = rds_user, password = rds_pass,db = rds_db)
cur=conn.cursor()

# def insert_details(mimetype,name,count,time):
#     cur.execute("INSERT INTO firstlast(mimetype,name,count,time) VALUES (%s,%s,%s,%s)", (mimetype,name,count,time))
#     conn.commit()

# def get_details():
#     cur.execute("SELECT *  FROM firstlast")
#     details = cur.fetchall()
#     return details

# def exec_env(value):
#     cmd = 'select {} from env_variables where DEVICE_ID LIKE "{}"'.format(value,device_id)
#     cur.execute(cmd)
#     details = cur.fetchone()[0]
#     return details
def get_cam(camera_id):
    cmd = 'select id,deviceId,siteId,potentialId from camera_devices where cameraId LIKE "{}"'.format(camera_id)
    cur.execute(cmd)
    details = cur.fetchone()
    return details  


def get_device(device_id):
    cmd = 'select deviceName,deviceTypeId,siteId,temp_range,age_range,Demographics,device_ip from devices where deviceId={}'.format(device_id)
    cur.execute(cmd)
    details = cur.fetchone()
    return details


def get_latlng(site):
    cmd = 'select latitude,longitude from sites where siteId={}'.format(site)
    cur.execute(cmd)
    details = cur.fetchone()
    return details    

def get_rule_id(rule):
    cmd = 'select id from rules where name LIKE "{}"'.format(rule)
    cur.execute(cmd)
    details = cur.fetchone()[0]
    return details

def get_asset_id(site,r_id,d_type,d_id):
    cmd = "select asset from rule_engine where site_id={} and rule={} and device_type={} and device_id={}".format(site,r_id,d_type,d_id)
    cur.execute(cmd)
    details = cur.fetchone()[0]
    print(details)
    return details     

def get_asset(a_id):
    cmd = 'select asset from assets where id={}'.format(a_id)
    cur.execute(cmd)
    details = cur.fetchone()[0]
    return details

def insert_details(site,device_id,name,mimetype,count,gender_age,rule):
    timestamp = datetime.now()
    cur.execute("INSERT INTO AV_raw_data(site_id,device,name,mimetype,count,gender_age,timestamp,rule) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)",(site,device_id,name,mimetype,count,str(gender_age),str(timestamp),rule))
    conn.commit()

# def get_dev_type(device_name):
#     cmd = 'select id from device_type where deviceType LIKE "{}"'.format(device_name)
#     cur.execute(cmd)
#     details = cur.fetchone()[0]
#     return details

## AWS RDS CONFIG END
