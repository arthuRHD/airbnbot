from zoomconnect_sdk.client import Client

from modules.config import EMAIL, DEST
from modules.server import listen_for_update

with open('token.txt', 'r') as f, open('modules/template.txt', 'r') as msg:
    token = f.read()
    content = msg.read()

sms_robot = Client(api_token=token, account_email=EMAIL)

if __name__ == "__main__":
    listen_for_update(sms_robot, content)
