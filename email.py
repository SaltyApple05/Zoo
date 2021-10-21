import smtplib, ssl

port = 465

sender, password = "themaniscracked@gmail.com", "MyMan123*"

#sender = "themaniscracked@gmail.com"
#password = "MyMan123*"

recieve = "leonhaslar112@gmail.com"

message = """\
Subject: Python Email

TEST
"""

context = ssl.create_default_context()

print("LETS GO!")

with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
  server.login(sender, password)
  server.sendmail(sender, recieve, message)

print("SENT")