# Copyright © 2022 mightyK1ngRichard <dimapermyakov55@gmail.com>
import json
import re


# TODO: создать список юзеров, которым можно отправлять токсичные смс. И функцию на True False.

def check_user_text(text: str, filename: str = 'DATA_WORD/data.json'):
    """
    Если в тексте присутствует слово из data.json, возвращаю ответ на это слово. Иначе, None.
    """
    with open(filename, encoding='utf-8') as data:
        WORDS = json.load(data)

    # Делим текст по словам. И проверяем каждое.
    for el in re.split(r'(\W+)', text):
        word = el.lower()
        res = [WORDS[key][word] for key, el in WORDS.items() if word in list(el.keys())]
        if len(res) != 0:
            return str(*res)
    return None

# print(check_user_text('ПРИВЕТ стая, как твои дела?', '../DATA_WORD/data.json'))
