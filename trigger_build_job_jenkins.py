import requests

jenkins_job_name = "tritest"
Jenkins_url = "http://172.16.1.240:8080"
jenkins_user = "admin"
jenkins_pwd = "admin"
buildWithParameters = True
jenkins_params = {'token': 'pY4Ms9OHKa'}

try:
    auth= (jenkins_user, jenkins_pwd)
    crumb_data= requests.get("{0}/crumbIssuer/api/json".format(Jenkins_url),auth = auth,headers={'content-type': 'application/json'})
    print(crumb_data.json())
    print(crumb_data.status_code)
    if str(crumb_data.status_code) == "200":
        data = requests.get("{0}/job/{1}/build".format(Jenkins_url,jenkins_job_name),auth=auth,params=jenkins_params)
        #print(data.headers)

        if str(data.status_code) == "201":
            print ("Jenkins job is triggered")
        else:
            print ("Failed to trigger the Jenkins job")

    else:
        print("Couldn't fetch Jenkins-Crumb")


except Exception as e:
    print ("Failed triggering the Jenkins job")
    print ("Error: " + str(e))
    raise e
