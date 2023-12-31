
import os
import requests
from dotenv import load_dotenv

load_dotenv()

MAILGUN_API_KEY = os.getenv("MAILGUN_API_KEY")
MAILGUN_DOMAIN = os.getenv("MAILGUN_DOMAIN")
MAILGUN_SENDER_ADDRESS = os.getenv("MAILGUN_SENDER_ADDRESS")



def send_email(recipient_address=MAILGUN_SENDER_ADDRESS, subject="[Shopping Cart App] Testing 123", html_content="<p>Hello World</p>"):
    print("SENDING EMAIL TO:", recipient_address)
    print("SUBJECT:", subject)
    print("HTML:", html_content)

    try:
        request_url = f"https://api.mailgun.net/v3/{MAILGUN_DOMAIN}/messages"
        message_data = {
            'from': MAILGUN_SENDER_ADDRESS,
            'to': recipient_address,
            'subject': subject,
            'html': html_content,
        }
        response = requests.post(request_url,
            auth=('api', MAILGUN_API_KEY),
            data=message_data
        )
        print("RESULT:", response.status_code)
        print("Email sent successfully!")
        return(response.status_code)
    except requests.exceptions.RequestException as e:
        print(f"Error sending email: {str(e)}")

if __name__ == "__main__":

    # ONLY WANT TO DO IF RUNNING THIS FILE FROM COMMAND LINE
    # (NOT IF IMPORTING A FUNCTION FROM THIS FILE)
    user_address = input("Please enter your email address: ")


    my_content = """

        <img
        src="https://img.freepik.com/free-vector/flat-ice-cream-collection_23-2148982427.jpg"
        alt="image of an ice cream"
        height=100
        >

        <h1>Ice Cream Shop Menu</h1>

        <p>Most popular flavors:</p>

        <ul>
        <li>Vanilla Bean </li>
        <li>Choc </li>
        <li>Strawberry</li>
        </ul>
    """
    send_email(html_content=my_content, recipient_address=user_address)