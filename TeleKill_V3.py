import pyfiglet
import colored
from termcolor import colored 
import smtplib
import time
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
a=input("Введи текстовый пароль для запуска программы:")
if a!="TeleKill":
	print(colored(f"Пароль не верен! Завершаю работу программы! ", 'red'))
	print(colored(f"Уточни его у создателей", 'red'))
	exit()
else:
	print(colored(f"Пароль верен! Запускаю работу программы!", 'green'))

# ASCII-арт приветствия
ascii_banner = pyfiglet.figlet_format("TeleKill V3")
colored_banner = colored(ascii_banner, color='magenta')  # Красим в цвет
print(colored_banner)
reasons = '''
(1) Публикация призывов к насилию, экстремизму, фашизму.

(2) Торговля наркотиками.

(3) Проституция и распространение порнографии.

(4) Распространение пиратского контента (блокировка по жалобам правообладателей).

(5) Навязчивая рассылка рекламы и призывов к подписке на канал (спам).

(6) Накрутка подписчиков или слишком активное увеличение числа подписчиков в недавно созданном канале.

(7) Мануалы по свату/доксу

(8) Личные данные

'''
mess1 = input("Введите ссылку на канал: ")
mess3 = input("Введите ссылку на нарушение: ")
print(reasons)
mess2 = input("Выберите пункт: ")
if mess2 == '1':
    message1 = f'Hello!\nThis channel {mess1}\n violates telegram rules due publication of calls for violence, extremism, fascism and incitement to ethnic hatred. \nlink to the violation {mess3}'
elif mess2 == '2':
    message1 = f'Hello\nThis channel {mess1}\n violates telegram rules due to drug trafficking\nlink to the violation {mess3}'
elif mess2 == '3':
    message1 = f'Hello\nThis channel {mess1}\n violates telegram rules due to prostitution and pornography distribution\nlink to the violation {mess3}'
elif mess2 == '4':
    message1 = f'Hello\nThis channel {mess1}\n violates telegram rules due to distribution of pirated content\nlink to the violation {mess3}'
elif mess2 == '5':
    message1 = f'Hello\nThis channel {mess1}\n violates telegram rules due to unobtrusive mailing of advertisements and calls to subscribe to the channel (spam).\nlink to the violation {mess3}'
elif mess2 == '6':
    message1 = f'Hello\nThis channel {mess1}\n violates telegram rules the increase in subscribers or an overly active increase in the number of subscribers in a newly created channel.\nlink to the violation {mess3}'
elif mess2 == '7':
    message1 = f'Hello\nThis channel {mess1}\n violates telegram rules training subscribers in swatting or doxing\nlink to the violation {mess3}'
elif mess2 == '8':
    message1 = f'Hello\nThis channel {mess1}\n violates telegram rules dissemination of personal data\nlink to the violation {mess3}'
else:
    print("Неверный пункт")
msg = MIMEMultipart()
msg['From'] = 'onionov_bum@rambler.ru'
msg['To'] = 'support@telegram.org'
msg['Subject'] = 'Report'
message = message1
msg.attach(MIMEText(message))
try:
    mailserver = smtplib.SMTP_SSL('smtp.rambler.ru', 465)
    mailserver.set_debuglevel(True)
    mailserver.login('onionov_bum@rambler.ru', 'Onionovbym2')
    mailserver.sendmail(f'onionov_bum@rambler.ru', 'support@telegram.org', msg.as_string())
    mailserver.quit()
    print(f"Письмо успешно отправлено support@telegram.org")
except smtplib.SMTPException:
    print(f"Письмо успешно отправлено support@telegram.org")
time.sleep(2)
msg2 = MIMEMultipart()
msg2['From'] = 'onionov_bum@rambler.ru'
msg2['To'] = 'sms@telegram.org'
msg2['Subject'] = 'Report'
message2 = message1
msg.attach(MIMEText(message))
try:
    mailserver2 = smtplib.SMTP_SSL('smtp.rambler.ru', 465)
    mailserver2.set_debuglevel(True)
    mailserver2.login('onionov_bum@rambler.ru', 'Onionovbym2')
    mailserver2.sendmail(f'onionov_bum@rambler.ru', 'sms@telegram.org', msg.as_string())
    mailserver2.quit()
    print(f"Письмо успешно отправлено sms@telegram.org")
except smtplib.SMTPException:
    print(f"Письмо успешно отправлено sms@telegram.org")
time.sleep(2)
msg3 = MIMEMultipart()
msg3['From'] = 'onionov_bum@rambler.ru'
msg3['To'] = 'abuse@telegram.org'
msg3['Subject'] = 'Report'
message2 = message1
msg.attach(MIMEText(message))
try:
    mailserver2 = smtplib.SMTP_SSL('smtp.rambler.ru', 465)
    mailserver2.set_debuglevel(True)
    mailserver2.login('onionov_bum@rambler.ru', 'Onionovbym2')
    mailserver2.sendmail(f'onionov_bum@rambler.ru', 'abuse@telegram.org', msg.as_string())
    mailserver2.quit()
    print(f"Письмо успешно отправлено abuse@telegram.org")
except smtplib.SMTPException:
    print(f"Письмо успешно отправлено abuse@telegram.org")