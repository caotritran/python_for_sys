#backup source code and mysql


import datetime, sh, os

time_now = str(datetime.date.today())
### Backup Source ###
print "backup source..."
source_path = "/home/admin/web/cocghe.tk/public_html"
backup_source_dir = "/root/backup_source"

if not os.path.exists(backup_source_dir):
    sh.mkdir(backup_source_dir)

target_source = "source" + "." + time_now + ".zip"
target_cmd_source = sh.zip("-r", backup_source_dir + "/" + target_source, source_path)
print "done..."
print "backup database..."

### Backup Database ###
database_name = "admin_cocdata"
user_name = "root"
pass_user = "xtehMuVpX349"

backup_db_dir = "/root/backup_db"

if not os.path.exists(backup_db_dir):
    sh.mkdir(backup_db_dir)

target_db = "db" + "." + time_now + ".sql"
#target_cmd_db = sh.mysqldump("-u", user_name, "-p" + pass_user, database_name, ">", backup_db_dir + "/" + target_db)
target_cmd_db = os.system("mysqldump -u " + user_name + " -p" + pass_user + " " + database_name + " >" + backup_db_dir + "/" + target_db)
print "done"
