# Copyright © 2022 mightyK1ngRichard <dimapermyakov55@gmail.com>
import json
import openai
import re


def check_user_text(text: str, filename: str = 'DATA_WORD/data.json'):
    """
    Если в тексте присутствует слово из data.json, возвращаю ответ на это слово. Иначе, None.
    """
    if text.lower() in ['пока', 'бб']:
        return text

    elif text in []:
        return text

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


def make_question(question):
    responde = openai.Completion.create(
        model="text-davinci-003",
        prompt=f"{question}",
        temperature=0.9,
        max_tokens=1000,
        top_p=1,
        frequency_penalty=0.0,
        presence_penalty=0.6,
    )

    return (responde['choices'][0]['text']).strip()
