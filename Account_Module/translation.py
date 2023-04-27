from Account_Module.models import User
from modeltranslation.translator import TranslationOptions, translator


class UserTranslationOptions(TranslationOptions):
    fields = ('about_user', 'first_name', 'last_name')

translator.register(User, UserTranslationOptions)