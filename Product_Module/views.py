from django.db.models import Count
from django.http import HttpRequest
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import ListView, DetailView

from Product_Module.models import Product, ProductCategory, ProductBrand


# Create your views here.

# class ProductListView(TemplateView):
#     template_name = 'product_module/Product_List.html'
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         products = Product.objects.all().order_by('-price')[:5]
#         context['products'] = products
#         return context
#
class ProductListView(ListView):
    template_name = 'product_module/Product_List.html'
    model = Product
    context_object_name = 'Products'
    ordering = ['-price']
    paginate_by = 3

    def get_queryset(self):
        query = super(ProductListView, self).get_queryset()
        category_name = self.kwargs.get('cat')
        brand_Name = self.kwargs.get('brand')
        request : HttpRequest = self.request
        print(request.GET)
        Start_Price = request.GET.get('Start_Price')
        End_Price = request.GET.get('End_Price')
        if Start_Price is not None:
            # Product.objects.filter(price__gte=Start_Price)
            query = query.filter(price__gte=Start_Price)
        if End_Price is not None:
            # Product.objects.filter(price__gte=Start_Price)
            query = query.filter(price__lte=End_Price)

        if category_name is not None:
            query = query.filter(category__url_title__iexact=category_name)

        if brand_Name is not None:
            query = query.filter(brand__Title__iexact=brand_Name)
        return query
    # def get_queryset(self):
    #     # base_query = super(ProductListView, self).get_queryset()
    #     # data = base_query.filter(is_active=True)
    #     # return data
    #     return super(ProductListView, self).get_queryset().filter(is_active=True)



class AddProductFavorite(View):
    def post(self, request):
        product_id = request.POST['product_id']
        product = Product.objects.get(pk=product_id)
        request.session['product_favorite'] = product_id
        return  redirect(product.get_absolute_url())


### Products name on html change to Object_list




# class ProductDetailView(TemplateView):
#     template_name = 'product_module/Product_Detail.html'
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         slug = kwargs['slug']
#         product = get_object_or_404(Product, slug=slug)
#         context['product'] = product
#         return context
#
class ProductDetailView(DetailView):
    template_name = 'product_module/Product_Detail.html'
    model = Product

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        loaded_product = self.object
        request = self.request
        # favorit_product_id = request.session['product_favorite']
        favorit_product_id = request.session.get('product_favorite')
        context['Is_favorit'] = favorit_product_id == str(loaded_product.id)
        return  context



def ProductCategoryComponents(request: HttpRequest):
    product_category = ProductCategory.objects.filter(is_active=True, is_delete=False)
    context = {
        'product_category': product_category
    }
    return render(request, 'product_module/Components/ProductCategoryComponents.html' , context)


def Productbrand(request:HttpRequest):
    product_Brand = ProductBrand.objects.annotate(products_Count=Count('product')).filter(Is_active=True)
    context = {
        'Product_Brand': product_Brand
    }
    return render(request, 'product_module/Components/ProductBrand.html', context)



# def product_list(request):
#     products = Product.objects.all().order_by('-price')[:5]
#     number_or_products = products.count()
#     return render(request, 'product_module/Product_List.html', {
#         'products': products,
#         'total_number_of_products': number_or_products,
#     })


# def product_detail(request, slug):
#     # try:
#     #     product = Product.objects.get(id=product_id)
#     # except:
#     #     raise Http404()
#     product = get_object_or_404(Product, slug=slug)
#
#     return render(request, 'product_module/Product_Detail.html', {
#         'product': product
#     })
