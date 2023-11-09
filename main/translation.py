# translation.py
from modeltranslation.translator import register, TranslationOptions
from .models import News, Staff, FAQ

@register(News)
class NewsTranslationOptions(TranslationOptions):
    fields = ('headline', 'body_text')

@register(Staff)
class StaffTranslationOptions(TranslationOptions):
    fields = ('title', 'description')

@register(FAQ)
class FAQTranslationOptions(TranslationOptions):
    fields = ('question', 'answer')
