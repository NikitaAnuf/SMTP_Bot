import smtplib

from variables import SMTP_HOST, SMTP_PORT, EMAIL_LOGIN, EMAIL_PASSWORD


def send_message(destination: str, text: str) -> tuple[str, bool]:
    try:
        server = smtplib.SMTP(SMTP_HOST, SMTP_PORT)
        server.ehlo()
        server.starttls()
        server.login(EMAIL_LOGIN, EMAIL_PASSWORD)
    except Exception as ex:
        return f"Can't initialize SMTP server - {ex.__str__()}", False

    try:
        message = f'''
        From: {EMAIL_LOGIN}
        To: {destination}
        Subject: Telegram Bot message
        {text}'''
        server.sendmail(EMAIL_LOGIN, destination, message.encode('utf-8'))
    except Exception as ex:
        return f'При отправке сообщения возникла ошибка - {ex.__str__()}', False
    else:
        return 'Сообщение успешно отправлено', True
    finally:
        server.quit()
