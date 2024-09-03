from django import template
import re

register = template.Library()

BAD_WORDS_LIST = ['редиска', 'энергии', 'минеральной', 'дайверы', 'дайверов', 'information']

@register.filter
def censor(text):
    def replace_word(match):
        word = match.group(0)
        return word[0] + '*' * (len(word) - 1)

    pattern = r'\b(' + '|'.join(map(re.escape, BAD_WORDS_LIST)) + r')\b'

    return re.sub(pattern, replace_word, text, flags=re.IGNORECASE)
