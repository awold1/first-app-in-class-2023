from app.email_service import send_email

def test_email_send():

    assert send_email() == 200

test_email_send()