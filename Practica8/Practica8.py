from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
import json

#esto es lo que se modifico ↓↓

parser = argparse.ArgumentParser()
parser.add_argument('-to', help='Destinatario:')
parser.add_argument('-subject', help= 'Asunto:')
parser.add_argument('-message', help='Mensaje:')
args = parser.parse_args()

destinatario = str(to)
asunto = str(args.subject)
message = str(args.message)

#esto es lo que se modifico ↑↑

data = {}
with open('pass.json') as f:
        data = json.load(f)
msg.attach(MIMEText(message, 'plain'))

msg['From'] = data['user']
msg['To'] = destinatario
msg['Subject'] = asunto

#create server
server = smtplib.SMTP('smtp.office365.com:587')
server.starttls()
# Login Credentials for sending the mail
server.login(data['user'], data['pass'])
# send the message via the server.
server.sendmail(msg['From'], receipents, msg.as_string())
server.quit()

print("successfully sent email to %s:" % (msg['To']))