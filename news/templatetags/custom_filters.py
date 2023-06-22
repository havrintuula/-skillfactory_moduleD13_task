from django import template


register = template.Library()

censored_words = {'COVID-19': 'C*******', 'covid19': 'c*******',
                  'COVID19': 'C*******', 'ковид':'к****', 'ковида': 'к*****'}

@register.filter()
def censor(value):
    censor_replace = str(value)
    for key in censored_words.keys():
        censor_replace = censor_replace.replace(key, censored_words[key])
    return censor_replace
