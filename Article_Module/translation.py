from modeltranslation.translator import TranslationOptions, translator
from Article_Module.models import Article, ArticleCategory, ArticelComment


class ArticleTranslationOptions(TranslationOptions):
    fields = ['title', 'short_description', 'text', ]


translator.register(Article, ArticleTranslationOptions)


class ArticleCategoryTranslationOptions(TranslationOptions):
    fields = ['title']


translator.register(ArticleCategory, ArticleCategoryTranslationOptions)


class ArticelCommentTranslationOptions(TranslationOptions):
    fields = ['text']


translator.register(ArticelComment, ArticelCommentTranslationOptions)
