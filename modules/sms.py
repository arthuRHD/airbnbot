"""
Tools to interact with the sms API
"""

def send_sms(client, destinataire, message):
    try:
        oldBalance = client.get_account_balance()
        message = client.send_sms(destinataire, message)
        newBalance = client.get_account_balance()
    except Exception as e:
        print(e)
    else:
        print(f"message sent {message}")
        print(
            f"{oldBalance.get('creditBalance', 0)} -> {newBalance.get('creditBalance', 0)}")
