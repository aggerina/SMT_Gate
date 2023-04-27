from modeltranslation.translator import TranslationOptions, translator
from News_Module.models import News, NewsComment, NewsCategory


class NewsTranslationOptions(TranslationOptions):
    fields = ['title', 'short_description', 'text', ]


translator.register(News, NewsTranslationOptions)


class NewsCategoryTranslationOptions(TranslationOptions):
    fields = ['title']


translator.register(NewsCategory, NewsCategoryTranslationOptions)


class NewsCommentTranslationOptions(TranslationOptions):
    fields = ['text']


translator.register(NewsComment, NewsCommentTranslationOptions)
