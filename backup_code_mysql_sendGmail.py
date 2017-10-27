#backup source code and mysql


import datetime, sh, os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

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

### sendmail to gmail ###

from_address = "tritran@azdigi.com"
from_pass = "password_here"
to_address = "caotritran.14@gmail.com"

msg = MIMEMultipart()

msg["From"] = from_address
msg["To"] = to_address
msg["Subject"] = "Backup hang ngay"

body = "file backup ngay %s" % time_now
msg.attach(MIMEText(body, "plain"))

attachment_1 = open(backup_source_dir + "/" + target_source, "rb")
attachment_2 = open(backup_db_dir + "/" + target_db, "rb")

#dinh kem file vao gmail
part_1 = MIMEBase("application", "octet-stream")
part_1.set_payload(attachment_1.read())
encoders.encode_base64(part_1)
part_1.add_header("Content-Disposition", "attachment; filename=%s" % target_source)


###
part_2 = MIMEBase("application", "octet-stream")
part_2.set_payload(attachment_2.read())
encoders.encode_base64(part_2)
part_2.add_header("Content-Disposition", "attachment; filename=%s" % target_db)

msg.attach(part_2)
msg.attach(part_1)
try:

    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login(from_address, from_pass)
    server.sendmail(from_address, to_address, msg.as_string())
    server.quit()
    print "Sendmail Success!!!"
except:
    print "Co loi xay ra..."
