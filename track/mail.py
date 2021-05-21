import requests







def send_simple_message():
    return requests.post(
        "https://api.mailgun.net/v3/manojadhikary.com.np",
        auth=("api", "0ebf8ec5bd32560e3a02f3918b555926-602cc1bf-446bd4a0"),
        data={"from": "Excited User <mailgun@manojadhikary.com.np>",
              "to": ["adkmanoz38@gmail.com",],
              "subject": "Hello",
              "text": "Testing some Mailgun awesomness!"})


send_simple_message()