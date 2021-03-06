import json

import requests
headers = {'Content-Type': 'application/json'}

# target server authenticate url
url_connect = "http://localhost:8069/web/session/authenticate"
# data to connect with database
data_connect = {
    "params": {
        "db": "odoo142",
        "login": "zeinabeng900@gmail.com",
        "password": "admin",
    }
}
# create new session
session = requests.Session()
connect_session = session.post(url=url_connect, data=json.dumps(data_connect), headers=headers)
if connect_session.ok:
    result = connect_session.json()['result']
    if result.get('ocn_token_key'):
        session.cookies['session_id'] = result.get('ocn_token_key')
# ----------------------------

# url to create data coming form skada
url = "http://localhost:8069/scada_table/"
# please send data like this formathttp://localhost:8069/web/session/authenticate
data = [
    ({'speed':20.30}),

]
# post data from skada to odoo to create it
response = session.post(url=url, data=json.dumps({'data': data}), headers=headers)

# response.json()  = {'jsonrpc': '2.0', 'id': None, 'result': '{"success": [29, 30]}'}
print(response.json())
