import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

USER = 'soongon@gmail.com'
PASSWORD = ''

send_from = USER
send_to = ['ssgoni@naver.com', '', '']


def create_message():
    msg = MIMEMultipart('alternative')
    msg['Subject'] = '안녕하세요'
    msg['From'] = send_from
    msg['To'] = ', '.join(send_to)

    part_plain = MIMEText('본문입니다.', 'plain')
    # part_html = MIMEText(html, 'html')
    msg.attach(part_plain)
    # msg.attach(part_html)
    return msg


def send_mail(msg):
    with smtplib.SMTP('smtp.gmail.com', 587) as server:
        server.starttls()
        server.login(USER, PASSWORD)
        server.sendmail(send_from, send_to, msg.as_string())


def main():
    msg = create_message()
    send_mail(msg)
    print('send ok..')


if __name__ == '__main__':
    main()
