from  modeltranslation.translator import TranslationOptions , translator
from Product_Module.models import  ProductCategory, Product, ProductBrand

class ProductCategoryTranslationOptions(TranslationOptions):
    fields = ['title']
translator.register(ProductCategory, ProductCategoryTranslationOptions)

class ProductTranslationOptions(TranslationOptions):
    fields = ['title', 'short_description', 'description']
translator.register(Product, ProductTranslationOptions)


class ProductBrandTranslationOptions(TranslationOptions):
    fields = ['Title']
translator.register(ProductBrand, ProductBrandTranslationOptions)



