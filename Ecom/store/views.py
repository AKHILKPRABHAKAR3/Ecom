from django.shortcuts import render,redirect
from django.views.generic import View,ListView,CreateView
from store.models import Category,Product,Cart,Order
from store.forms import Registerform,LoginForm,orderform
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.contrib.auth import authenticate,login,logout
from django.utils.decorators import method_decorator

# Create your views here.
def login_required(fn):
    def wrapper(request,*args,**kwargs):
        if request.user.is_authenticated:
            return fn(request,*args,**kwargs)
        else:
            return redirect("login")
    return wrapper




class Home(ListView):
    # def get(self,request,*args,**kwargs):
    #     return render(request,"store\index.html")
    model=Category
    template_name="store/index.html"
    context_object_name="data"



    
# class Register(View):
#     def get(self,request,*args,**kwargs):
#         return render(request,"store\register.html")
    
class Collections(View):
    # model=Category
    # template_name="store/index.html"
    # context_object_name="data"
    
    def get(self,request,*args,**kwargs):
        data=Category.objects.all()
        return render(request,"store\index.html",{"data":data})
    
class products(View):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("id")
        data=Product.objects.filter(category_id=id)
        name=Category.objects.get(id=id)
        return render(request,"store\products.html",{"data":data,"name":name})

class product_details(View):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("id")
        p_data=Product.objects.filter(id=id)
        return render(request,"store\product_details.html",{"p_data":p_data})
    
class RegisterView(CreateView):
    template_name="store/register.html"
    form_class=Registerform
    model=User
    success_url=reverse_lazy("login")

class LoginView(View):
    def get(self,request,*args,**kwargs):
        form=LoginForm
        return render(request,"store/login.html",{"form":form})
    
    def post(self,request,*args,**kwargs):
        form=LoginForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            u_name=form.cleaned_data.get("username")
            password=form.cleaned_data.get("password")
            user_obj=authenticate(request,username=u_name,password=password)
            if user_obj:
                print("valid credential")
                login(request,user_obj)
                return redirect("home")
            else:
                print("invalid credential")
                return redirect("register")
            
class Logout(View):
    def get(self,request,*args,**kwargs):
        logout(request)
        return redirect("register")
@method_decorator(login_required,name="dispatch")
class Addcartview(View):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        data=Product.objects.get(id=id)
        Cart.objects.create(item=data,user=request.user)
        print("added successfully")
        return redirect("cartdetails")
    
class Delete_cart(View):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        Cart.objects.get(id=id).delete()
        return redirect("cartdetails")

@method_decorator(login_required,name="dispatch")
class Cartdetailview(View):
    def get(self,request,*args,**kwargs):
        data=Cart.objects.filter(user=request.user)
        return render(request,"store/cart.html",{"data":data})
    

class OrderView(View):
    def get(self,request,*args,**kwargs):
        form=orderform
        return render(request,"store/orderpage.html",{"form":form})
    def post(self,request,*args,**kwargs):
        id=kwargs.get("id")
        data=Product.objects.get(id=id)
        form=orderform(request.POST)
        if form.is_valid():
            qs=form.cleaned_data.get("address")
            Order.objects.create(order_item=data,customer=request.user,address=qs)
            return redirect("home")
        return redirect("cart")
    
class OrderList(View):
    def get(self,request,*args,**kwargs):
        data=Order.objects.filter(customer=request.user)
        return render(request,"store/orderlist.html",{"data":data})
    
class Order_Delete(View):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("id")
        Order.objects.get(id=id).delete()
        return redirect("orderlist")
    
class Searchview(View):
    def get(self,request,*args,**kwargs):
        query= request.GET.get('q')
        if query:
            results=Product.objects.filter(name__icontains=query)
        else:
            results=None
        return render(request,"store/search_result.html",{"results":results})

    
