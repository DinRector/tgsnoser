import requests
import random
import string
import pyfiglet
import colored
from termcolor import colored

a=input("Введи текстовый пароль для запуска программы:")
if a!="1234":
	print(colored(f"Пароль не верен! Завершаю работу программы! ", 'red'))
	print(colored(f"Уточни его у создателей", 'red'))
	exit()
else:
	print(colored(f"Пароль верен! Запускаю работу программы!", 'green'))
	
# ASCII-арт приветствия
ascii_banner = pyfiglet.figlet_format("TeleKill V2")
colored_banner = colored(ascii_banner, color='magenta')  # Красим в цвет

print(colored_banner)

def generate_random_email():
    domains = [
        "gmail.com", "yahoo.com", "outlook.com", "mail.ru", "yandex.ru",
        "icloud.com", "zoho.com", "protonmail.com", "gmx.com", "inbox.com",
        "aol.com", "hotmail.com", "mail.com", "rambler.ru", "bk.ru",
        "list.ru", "e1.ru", "qip.ru", "ya.ru", "live.com",
        "msn.com", "comcast.net", "sbcglobal.net", "att.net", "verizon.net",
        "bellsouth.net", "charter.net", "earthlink.net", "mindspring.com", "me.com",
        "mac.com", "fastmail.com", "hushmail.com", "inbox.lv", "mail.kz",
        "mail.bg", "web.de", "freenet.de", "t-online.de", "zoznam.sk",
        "centrum.cz", "seznam.cz", "bigmir.net", "ukr.net", "posteo.net",
        "tut.by", "abv.bg", "tiscali.it", "libero.it", "virgilio.it",
        "alice.it", "btinternet.com", "orange.fr", "wanadoo.fr", "laposte.net",
        "skynet.be", "bluewin.ch", "netcourrier.com", "sfr.fr", "vodafone.it"
    ]
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for _ in range(10)) + '@' + random.choice(domains)

def generate_random_phone_number():
    russian_prefixes = ['+7903', '+7747', '+7705', '+7905', '+7901']
    international_prefixes = [
        '+1', '+44', '+61', '+81', '+86', '+91', '+33', '+49', '+39', '+34',  # США, Великобритания, Австралия, Япония, Китай, Индия, Франция, Германия, Италия, Испания
        '+55', '+7', '+46', '+47', '+31', '+41', '+32', '+45', '+358', '+420', # Бразилия, Россия, Швеция, Норвегия, Нидерланды, Швейцария, Бельгия, Дания, Финляндия, Чехия
        '+36', '+48', '+30', '+351', '+30', '+34', '+27', '+91', '+64', '+66', # Венгрия, Польша, Греция, Португалия, Греция, Испания, ЮАР, Индия, Новая Зеландия, Таиланд
        '+60', '+65', '+63', '+92', '+62', '+90', '+234', '+254', '+51', '+56', # Малайзия, Сингапур, Филиппины, Пакистан, Индонезия, Турция, Нигерия, Кения, Перу, Чили
        '+57', '+505', '+591', '+507', '+52', '+58', '+591', '+598', '+54', '+598', # Колумбия, Никарагуа, Боливия, Панама, Мексика, Венесуэла, Боливия, Уругвай, Аргентина, Уругвай
        '+82', '+98', '+964', '+66', '+84', '+92', '+90', '+94', '+880', '+970',  # Южная Корея, Иран, Ирак, Таиланд, Вьетнам, Пакистан, Турция, Шри-Ланка, Бангладеш, Палестина
    ]
    all_prefixes = russian_prefixes + international_prefixes
    prefix = random.choice(all_prefixes)
    number = ''.join(random.choice(string.digits) for _ in range(7))
    return f"{prefix}{number}"

def send_message(url, payload):
    try:
        response = requests.post(url, data=payload)
        if response.status_code == 200:
            print(colored(f"Сообщение отправлено успешно: {payload}", 'green'))
        else:
            print(colored(f"Не удалось отправить сообщение. Статус-код: {response.status_code}", 'red'))
    except Exception as e:
        print(f"Ошибка при отправке сообщения: {e}")

def main():
    url = "https://telegram.org/support?setln=ru"
    subject = "Support Request"
    
    user_tag = input("Укажите @username жертвы: ")
    message = f"This user {user_tag} spams chats and insults chat participants. Please figure it out!"
    message_count = int(input("Введите количество жалоб: "))

    for _ in range(message_count):
        email = generate_random_email()
        phone = generate_random_phone_number()

        payload = {
            "subject": subject,
            "message": message,
            "email": email,
            "phone": phone  # Предполагаем наличие этого поля, нужно проверить фактически
        }

        send_message(url, payload)

if __name__ == "__main__":
    main()