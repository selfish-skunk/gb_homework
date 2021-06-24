import re
EMAIL = re.compile(r'(^[a-z0-9-\.]+)@([a-z0-9]+\.[a-z]+)$')
# группировки кгруглыми скобками в регулярном выражении съели мне мозг. Ктож знал, что они потом удобно разбиваются


def email_parse(email):
    found_info = EMAIL.findall(email.lower())
    # .lower переводит в нижний регистр, но можно сделать через регулярное выражение
    if found_info:
        default_data = {}
        default_data.update({'email': found_info})
    else:
        raise ValueError(f'wrong email: {email}')
    print(default_data)

email_parse('Someone@geekbrains.ru')
email_parse('someone@geekbrainsru')
