#backup source code and mysql
import datetime, sh, os
import pysftp
 
time_now = str(datetime.date.today())
### Backup Source ###
print "backup source..."
source_path = "/home/admin/web/cocghe.com/public_html"
backup_source_dir = "/root/backup_source"
 
if not os.path.exists(backup_source_dir):
    sh.mkdir(backup_source_dir)
else:
    sh.rm(backup_source_dir, "-rf")
    sh.mkdir(backup_source_dir)
 
#target_source = "source" + "." + time_now + ".zip"
target_source = "source" + ".zip"
target_cmd_source = sh.zip("-r", backup_source_dir + "/" + target_source, source_path)
print "done..."
print "backup database..."
 
### Backup Database ###
database_name = "ten_data_cua_ban"
user_name = "ten_user_cua_ban"
pass_user = "pass_cua_ban"
 
backup_db_dir = "/root/backup_db"
 
if not os.path.exists(backup_db_dir):
    sh.mkdir(backup_db_dir)
else:
        sh.rm(backup_db_dir, "-rf")
        sh.mkdir(backup_db_dir)
 
#target_db = "db" + "." + time_now + ".sql"
target_db = "db" + ".sql"
#target_cmd_db = sh.mysqldump("-u", user_name, "-p" + pass_user, database_name, ">", backup_db_dir + "/" + target_db)
target_cmd_db = os.system("mysqldump -u " + user_name + " -p" + pass_user + " " + database_name + " >" + backup_db_dir + "/" + target_db)
print "done"
 
 
#send file to FTP server
with pysftp.Connection("103.221.221.xxx", username="root", password="pass_cua_ban") as sftp:
    with sftp.cd("/root/backup_web"):
    print "sending source..."
        a = open("/root/backup_source/source.zip", "rb")
        sftp.put("/root/backup_source/source.zip")
    print "sending db..."
    b = open("/root/backup_db/db.sql", "rb")
    sftp.put("/root/backup_db/db.sql")
    print "done at %s" %time_now