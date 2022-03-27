import requests
from requests.auth import HTTPBasicAuth
to_number = 'outgoing_number'
from_number = 'your_twilio_number'
message = 'Thank for your order, we will deliver after our cookie booth sale at around 6pm.'
account_sid = 'your_account_sid'
auth_token = 'your_auth_token'
auth = HTTPBasicAuth(account_sid, auth_token)
url = 'https://api.twilio.com/2010-04-01/Accounts/{}/Messages'.format(account_sid)
values = {  
        'To' : to_number, 
        'From' : from_number,
        'Body' : message,
        }
response = requests.post(url, data = values, auth = auth)

