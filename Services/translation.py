from  modeltranslation.translator import TranslationOptions , translator
from Services.models import Service, Team

class ServicesTranslationOptions(TranslationOptions):
    fields = ['Title', 'ShortDescription', 'Description', 'Create_Date']
translator.register(Service, ServicesTranslationOptions)

class TeamsTranslator(TranslationOptions):
    fields = ['Title', 'ShortDescription', 'Description']

translator.register(Team, TeamsTranslator)