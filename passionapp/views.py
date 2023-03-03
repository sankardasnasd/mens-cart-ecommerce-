from django.shortcuts import render,redirect
from django.views import View
from django.views.generic.base import RedirectView
from .models import Cart, Customer, Product
from django.db.models import Count
from .forms import CustomerProfileForm, CustomerRegistrationForm
from django.contrib import messages

# Create your views here.
def passionapp(request):
    return render(request,'passionapp')

def home(request):
    return render(request,'home.html')

class CategoryView(View):
    # 1st
    def get(self,request,val):
        # 2nd
        product = Product.objects.filter(category=val)
        # 3rd
        title = Product.objects.filter(category = val).values('title')
        return render(request,'category.html',locals())
    

class CategoryTitle(View):
    def get(self,request,val):
        product = Product.objects.filter(title = val)
        title = Product.objects.filter(category = product[0].category).values('title')
        return render(request,'category.html',locals())
    
class ProductDetail(View):
    def get(self,request,pk):
        product = Product.objects.get(pk = pk)
        return render (request,"productdetail.html",locals())
def about(request):
    return render (request,'about.html')

def contact(request):
    return render (request,'contact.html')

# login authentication
class CustomerRegistrationView(View):
    def get(self,request):
        form = CustomerRegistrationForm()
        return render(request,'customerregistration.html',locals())
    def post(self,request):
        form = CustomerRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Congratulations User registered Successfully')
        else:
            messages.warning(request,"Invalid data require")
        return render(request,'customerregistration.html',locals())
    

class ProfileView(View):
    def get(self,request):
        form = CustomerProfileForm()
        return render(request,'profile.html',locals())
    def post(self,request):
        form = CustomerProfileForm(request.POST)
        if form.is_valid():
            user = request.user
            name = form.cleaned_data['name']
            locality = form.cleaned_data['locality']
            city = form.cleaned_data['city']
            mobile = form.cleaned_data['mobile']
            state = form.cleaned_data['state']
            zipcode =form.cleaned_data['zipcode']

            reg = Customer(user = user,name = name,locality = locality,city = city,mobile = mobile,state= state,zipcode = zipcode)
            reg.save()
            messages.success(request,'Congratulations Your Profile Save Successfully!')
        else:
            messages.warning(request,"Invalid Data Occurs")
        return render(request,'profile.html',locals())
    
# only fetch one or original user can access another user cannot access when it login code = "add = Customer.objects.filter(user = request.user)""

def address(request):
    add = Customer.objects.filter(user=request.user)
    return render(request,'address.html',locals())

class updateAddress(View):
    def get(self,request,pk):
        add = Customer.objects.get(pk = pk)
        form = CustomerProfileForm(instance=add)
        return render(request,'updateAddress.html',locals())
    def post(self,request,pk):
        form = CustomerProfileForm(request.POST)
        if form.is_valid():
            add = Customer.objects.get(pk = pk)
            add.name = form.cleaned_data['name']
            add.locality = form.cleaned_data['locality']
            add.city = form.cleaned_data['city']
            add.mobile = form.cleaned_data['mobile']
            add.state = form.cleaned_data['state']
            add.zipcode = form.cleaned_data['zipcode']
            add.save()
            messages.success(request,'Congratulations Your Profile Updated Successfuly')
        else:
            messages.warning(request,'Invalid credential')
        return redirect('address')
    


def add_to_cart(request):
    user = request.user
    product_id = request.GET.get('prod_id')
    product = Product.objects.get(id = product_id)
    Cart(user=user,product=product).save()
    return redirect('/cart')


def show_cart(request):
    user = request.user
    cart = Cart.objects.filter(user=user)
    return render(request,'addtocart.html',locals())
