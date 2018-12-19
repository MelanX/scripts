import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Default settings:
dsmtp = ''
dport = ''
dfromname = ''
dfrommail = ''
dpsw = ''
drecipient = ''
dsubject = ''
dmailtext = ''

# server config
smtp = ''.join(input(f'Enter the smtp adress (gmail is "smtp.gmail.com"): {dsmtp}') or dsmtp) # smtp for gmail
port = ''.join(input(f'Enter the port (gmail is "587"): {dport}')) or dport # port for gmail

# user config
fromname = ''.join(input(f'Enter the name which is shown as sender: {dfromname}')) or dfromname # name shown as sender
frommail = ''.join(input(f'Enter your mailadress: {dfrommail}')) or dfrommail # your mail
psw = ''.join(input(f'Enter your mailadress password: {dpsw}')) or dpsw # your password
recipient = ''.join(input(f'Enter the recipients mailadress: {drecipient}')) or drecipient # recipient

# subject as string
subject = ''.join(input(f'Enter the subject: {dsubject}')) or dsubject

# body as string --- format: html
mailtext = ''.join(input(f'Enter the mail body: {dmailtext}')) or dmailtext

print(
    f"""\n\n\nYour name: {fromname}
Your mail: {frommail}
Recipient: {recipient}
Subject: {subject}
Mailtext: {mailtext}""")

send = input('\nDo you want to send this mail (y/n)? ')

# sendmail
if send == 'y':
    msg = MIMEMultipart()
    msg['From'] = fromname
    msg['To'] = recipient
    msg['Subject'] = subject

    # Text
    msgText = MIMEText(mailtext, 'html')
    msg.attach(msgText)

    server = smtplib.SMTP(smtp, port)
    server.starttls()
    server.login(frommail, psw)
    text = msg.as_string()
    server.sendmail(frommail, recipient, text)
    server.quit()
else:
    input('\n\n\nPress enter to exit this program...')
    exit(0)

print(f'\n\nE-mail successfully sent to {recipient}.')
input('Press enter to exit this program...')