import pysftp

with pysftp.Connection("103.221.221.144", username="admin", password="zxcasdqwe123@@@") as sftp:
    with sftp.cd("web/cocghe.tk/public_html"):
        a = open("/home/tritran/Desktop/python_learn/lab1.py", "rb")
        sftp.put("/home/tritran/Desktop/python_learn/lab1.py")