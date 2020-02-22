import requests
#  документация https://yandex.ru/dev/translate/doc/dg/reference/translate-docpage/

API_KEY = ''
URL = 'https://translate.yandex.net/api/v1.5/tr.json/translate'

def translate_it(text, lang, to_lang):
    """
    https://translate.yandex.net/api/v1.5/tr.json/translate ?
    key=<API-ключ>
     & text=<переводимый текст>
     & lang=<направление перевода>
     & [format=<формат текста>]
     & [options=<опции перевода>]
     & [callback=<имя callback-функции>]
    :param to_lang:
    :return:
    """

    params = {
        'key': API_KEY,
        'text': text,
        'lang': '{}-{}'.format(lang, to_lang),
    }

    response = requests.get(URL, params=params)
    json_ = response.json()
    return ''.join(json_['text'])


# print(translate_it('В настоящее время доступна единственная опция — признак включения в ответ автоматически определенного языка переводимого текста. 
# Этому соответствует значение 1 этого параметра.', 'no'))

def open_txt(file_name):
    with open(file_name, 'r', encoding='utf-8') as f:
        data = [l.strip() for l in f]
        return data

def write_txt(file_name, data):
    with open(file_name, 'w', encoding='utf-8') as f:
        f.write(data)


translated_data_de = translate_it(open_txt('DE.txt'), 'de', 'ru')
print(translated_data_de)
write_txt('TranslatedDE.txt', translated_data_de)

translated_data_es = translate_it(open_txt('ES.txt'), 'es', 'ru')
print(translated_data_es)
write_txt('TranslatedES.txt', translated_data_es)

translated_data_fr = translate_it(open_txt('FR.txt'), 'fr', 'ru')
print(translated_data_fr)
write_txt('TranslatedFR.txt', translated_data_fr)


