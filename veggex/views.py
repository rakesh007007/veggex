from django.shortcuts import render
from django.shortcuts import render
import veggex.views
from django.template.response import TemplateResponse
from django.template import Context, loader
from django.http import HttpResponse
from django.contrib import sessions
from rest_framework import viewsets
#from buyold.quickstart import *
from django.middleware import csrf
from veggex.models import *
from startup.settings import *
from django.contrib.sessions.backends.db import SessionStore
from django.shortcuts import redirect
import logging
from django.core.files.storage import default_storage
logger = logging.getLogger(__name__)
from django.core.files.base import ContentFile

# Create your views here.
def get_or_create_csrf_token(request):
    token = request.META.get('CSRF_COOKIE', None)
    if token is None:
        token = csrf._get_new_csrf_key()
        request.META['CSRF_COOKIE'] = token
    request.META['CSRF_COOKIE_USED'] = True
    return token
def getTotal(cartitems):
    total=0
    for itemm in cartitems:
        total = total+itemm.product.pricePerUnit*itemm.qtyInUnits
    return total

def login(request):
	if ('loggedin' not in request.session):
		return TemplateResponse(request, 'login.html',{'csrf_token':get_or_create_csrf_token(request)})
	else:
		return redirect('/main')
def tryy(request):
	return TemplateResponse(request, 'tryy.html',{'csrf_token':get_or_create_csrf_token(request)})
def checklogin(request):
	if ('loggedin' not in request.session):
		return False
	else:
		return True
def logPost(request):
	mobile = request.POST['mobile']
	password = request.POST['password']
	u= User.objects.filter(mobileNo=mobile).filter(password=password)
	if(len(u)>0):
		request.session['loggedin']=True
		request.session['mobile'] = mobile
		return redirect('/main')
	else:
		return redirect('/login')
def logout(request):
	 if('loggedin' in request.session):
	 	 del request.session['loggedin']
	 if('mobile' in request.session):
	 	del request.session['mobile'] 
	 return TemplateResponse(request, 'logout.html',{'csrf_token':get_or_create_csrf_token(request)})
def account(request):
	if(checklogin(request)==False):
		return redirect('/login')
	mobile =request.session['mobile']
	user = User.objects.get(mobileNo=mobile)
	return TemplateResponse(request, 'account.html',{'user':user,'csrf_token':get_or_create_csrf_token(request)})
def main(request):
	if(checklogin(request)==False):
		return redirect('/login')
	categories =Category.objects.all()
	return TemplateResponse(request, 'main.html',{'categories':categories,'csrf_token':get_or_create_csrf_token(request)})
def get_or_create_cart(user):
	cart = Cart.objects.filter(user=user)
	if(len(cart)==1):
		return cart[0]
	else:
		cart = Cart()
		cart.user=user
		cart.save()
		return cart
def categoryView(request):
	if(checklogin(request)==False):
		return redirect('/login')
	categoryId=request.GET['categoryId']
	category = Category.objects.get(category_id=categoryId)
	products = Product.objects.filter(category=category)
	return TemplateResponse(request, 'categoryView.html',{'products':products,'csrf_token':get_or_create_csrf_token(request)})
def addtocart(request):
	if(checklogin(request)==False):
		return redirect('/login')
	productId = request.POST['productId']
	productId = (int)(productId)
	mobile=request.session['mobile']
	user = User.objects.get(mobileNo=mobile)
	product  = Product.objects.get(product_id=productId)
	qty = request.POST['qty']
	cart = get_or_create_cart(user)
	cartitem=Cartitem()
	cartitem.cart=cart
	cartitem.qtyInUnits = qty
	cartitem.product=product
	cartitem.save()
	return redirect('/cart')
def removeItemPost(request):
	if(checklogin(request)==False):
		return redirect('/login')
	itemId = request.POST['item_id']
	Cartitem.objects.filter(cartitem_id=itemId).delete()
	return redirect('/cart')
def orderStep1(request):
	if ('loggedin' not in request.session):
		return TemplateResponse(request, 'login.html',{'csrf_token':get_or_create_csrf_token(request)})
	else:
		
		return TemplateResponse(request, 'orderstep1.html',{'csrf_token':get_or_create_csrf_token(request)})
def seeOrder(request):
	if ('loggedin' not in request.session):
		return TemplateResponse(request, 'login.html',{'csrf_token':get_or_create_csrf_token(request)})
	else:
		mobile = request.session['mobile']
		user =User.objects.filter(mobileNo=mobile)[0]
		orders = Order.objects.filter(user=user)
		return TemplateResponse(request, 'order.html',{'orders':orders,'csrf_token':get_or_create_csrf_token(request)})
def makeOrder(request):
	if ('loggedin' not in request.session):
		return TemplateResponse(request, 'login.html',{'csrf_token':get_or_create_csrf_token(request)})
	else:
		print 'yoo'
		mobile = request.session['mobile']
		user =User.objects.filter(mobileNo=mobile)[0]
		payment_mode = 'COD'
		cart =get_or_create_cart(user)
		items = Cartitem.objects.filter(cart = cart)
		total=getTotal(items)
		if(len(items)<1):
			print 'no items'
			return HttpResponse('no items to make order')
		else:
			order = Order()
			order.user = user
			order.payment_mode = payment_mode
			order.subtotal=total
			order.status = 'PLACED'
			order.save()
			order_id =order.order_id 
			for itemn in items:
				rak = Orderitem()
				rak.product = itemn.product
				rak.unit=itemn.product.unit
				rak.qtyInUnits = itemn.qtyInUnits
				rak.priceType = itemn.product.priceType
				rak.priceAtThatTime = itemn.product.pricePerUnit
				rak.order = order
				rak.save()
				#fullMsgSender(userId,'Purchase','you have just orderds this shit')
			Cartitem.objects.filter(cart = cart).delete()
			return redirect('/seeOrder')
def cart(request):
	if(checklogin(request)==False):
		return redirect('/login')
	mobile=request.session['mobile']
	user = User.objects.get(mobileNo=mobile)
	cart = get_or_create_cart(user)
	cartitems = Cartitem.objects.filter(cart=cart)
	shippingCost=0
	carttotal=getTotal(cartitems)
	return TemplateResponse(request, 'cart.html',{'carttotal':carttotal,'shippingCost':shippingCost,'cartitems':cartitems,'cart':cart,'csrf_token':get_or_create_csrf_token(request)})


