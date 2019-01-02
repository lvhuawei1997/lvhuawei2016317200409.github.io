from django.shortcuts import render, HttpResponse
from django.shortcuts import redirect
from django.shortcuts import render_to_response
from login import models, forms
from login.models import Land, Product, Dosage, CropRecords, Recovery
import datetime

from django.conf import settings


# Create your views here.


def index(request):
	pass
	return render(request, 'login/index.html')


# def login(request):
#     if request.session.get('is_login', None):
#         return render(request, 'login/index.html', locals())
#     if request.method == "POST":
#         login_form = forms.UserForm(request.POST)
#         message = "请检查填写的内容！"
#         if login_form.is_valid():
#             username = login_form.cleaned_data['username']
#             password = login_form.cleaned_data['password']
#             identity = login_form.cleaned_data['identity']
#             try:
#                 user = models.User.objects.get(name=username)
#                 if user.identity == 'farmer' and user.password == password:
#                     request.session['is_login'] = True
#                     request.session['user_id'] = user.id
#                     request.session['user_name'] = user.name
#                     return render(request, 'login/farmer.html', locals())
#                 elif user.identity == 'technician' and user.password == password:
#                     request.session['is_login'] = True
#                     request.session['user_id'] = user.id
#                     request.session['user_name'] = user.name
#                     return render(request, 'login/technician.html', locals())
#                 elif user.identity == 'marketer' and user.password == password:
#                     request.session['is_login'] = True
#                     request.session['user_id'] = user.id
#                     request.session['user_name'] = user.name
#                     return render(request, 'login/marketer.html', locals())
#                 else:
#                     message = "密码不正确！"
#             except:
#                 message = "用户不存在！"
#         return render(request, 'login/login.html', locals())
#
#     login_form = forms.UserForm()
#     return render(request, 'login/login.html', locals())
# def login(request):
#     if request.method == "POST":
#         username = request.POST.get('username', None)
#         password = request.POST.get('password', None)
#         if username == "admin"and password == "20181225":
#         	return render(request, 'login/farmer.html')
#     return render(request, 'login/login.html')

def login(request):
	if request.session.get('is_login', None):
		return render(request, 'login/index.html', locals())
	if request.method == "POST":
		username = request.POST.get('username', None)
		password = request.POST.get('password', None)
		user = models.User.objects.get(name=username)
		if username == "admin" and password == "20181225":
			request.session['is_login'] = True
			request.session['user_id'] = user.id
			request.session['user_name'] = user.name
			return render(request, 'login/farmer.html')
		elif username == "tech" or username == "tech2" and password == "20181225":
			request.session['is_login'] = True
			request.session['user_id'] = user.id
			request.session['user_name'] = user.name
			return render(request, 'login/technician.html')
		elif username == "market" and password == "20181225":
			request.session['is_login'] = True
			request.session['user_id'] = user.id
			request.session['user_name'] = user.name
			return render(request, 'login/marketer.html')
		else:
			return render(request, 'login/index.html')
	return render(request, 'login/login.html')


def register(request):
	if request.session.get('is_login', None):
		# 登录状态不允许注册。你可以修改这条原则！
		return redirect("/index/")
	if request.method == "POST":
		register_form = forms.RegisterForm(request.POST)
		message = "请检查填写的内容！"
		if register_form.is_valid():  # 获取数据
			username = register_form.cleaned_data['username']
			password1 = register_form.cleaned_data['password1']
			password2 = register_form.cleaned_data['password2']
			identity = register_form.cleaned_data['identity']
			if password1 != password2:  # 判断两次密码是否相同
				message = "两次输入的密码不同！"
				return render(request, 'login/register.html', locals())
			else:
				same_name_user = models.User.objects.filter(name=username)
				if same_name_user:  # 用户名唯一
					message = '用户已经存在，请重新选择用户名！'
					return render(request, 'login/register.html', locals())

				# 当一切都OK的情况下，创建新用户

				new_user = models.User()
				new_user.name = username
				new_user.password = password1
				new_user.identity = identity
				new_user.save()
				return redirect('/login/')  # 自动跳转到登录页面
	register_form = forms.RegisterForm()
	return render(request, 'login/register.html', locals())


def logout(request):
	if not request.session.get('is_login', None):
		# 如果本来就未登录，也就没有登出一说
		return redirect("/index/")
	request.session.flush()
	# 或者使用下面的方法
	# del request.session['is_login']
	# del request.session['user_id']
	# del request.session['user_name']
	return redirect("/index/")


# 查看土地
def land(request):
	land_list = Land.objects.all()
	return render(request, "land/land.html", {"land_list": land_list})


def addland(request):
	if request.method == 'POST':
		id = request.POST.get("id")
		zone = request.POST.get("zone")
		landmark = request.POST.get("landmark")
		lot = request.POST.get("lot")
		position = request.POST.get("position")
		area = request.POST.get("area")
		if id == '':
			return HttpResponse('<h3 stytle="color:#c7254e">ID不能为空</h3>')

		land_obj = Land.objects.create(id=id, zone=zone, landmark=landmark, lot=lot, position=position, area=area)
		return redirect("/land/")
	return render(request, 'land/addland.html', locals())


def delland(request, id):
	land_obj = models.Land.objects.filter(pk=id).first()
	land_obj.delete()
	return redirect("/land/")


def editland(request, id):
	land_obj = Land.objects.filter(pk=id).first()
	if request.method == 'POST':
		zone = request.POST.get("zone")
		landmark = request.POST.get("landmark")
		lot = request.POST.get("lot")
		position = request.POST.get("position")
		area = request.POST.get("area")

		Land.objects.filter(pk=id).update(id=id, zone=zone, landmark=landmark, lot=lot, position=position, area=area)
		return redirect("/land/")
	return render(request, 'land/editland.html', {"land_obj": land_obj})


# 查看配肥和配药
def dosage(request):
	dosage_list = Dosage.objects.all()
	return render(request, "dosage/dosage.html", {"dosage_list": dosage_list})


def adddosage(request):
	if request.method == 'POST':
		id = request.POST.get("id")
		dosage_date = request.POST.get("dosage_date")
		muck_name = request.POST.get("muck_name")
		tlc = request.POST.get("tlc")
		twlr = request.POST.get("twlr")
		naworm = request.POST.get("naworm")
		if id == '':
			return HttpResponse('<h3 stytle="color:#c7254e">ID不能为空</h3>')

		dosage_obj = Dosage.objects.create(id=id, dosage_date=dosage_date, muck_name=muck_name, tlc=tlc, twlr=twlr, naworm=naworm)
		return redirect("/dosage/")
	return render(request, 'dosage/adddosage.html', locals())


def deldosage(request, id):
	dosage_obj = models.Dosage.objects.filter(pk=id).first()
	dosage_obj.delete()
	return redirect("/dosage/")


def editdosage(request, id):
	dosage_obj = Dosage.objects.filter(pk=id).first()
	if request.method == 'POST':
		dosage_date = request.POST.get("dosage_date")
		muck_name = request.POST.get("muck_name")
		tlc = request.POST.get("tlc")
		twlr = request.POST.get("twlr")
		naworm = request.POST.get("naworm")

		Dosage.objects.filter(pk=id).update(dosage_date=dosage_date, muck_name=muck_name, tlc=tlc, twlr=twlr, naworm=naworm)
		return redirect("/dosage/")
	return render(request, 'dosage/editdosage.html', {"dosage_obj": dosage_obj})


def returnfarmer(request):
	return render(request, 'login/farmer.html', locals())


# 查看生产资料
def product(request):
	product_list = Product.objects.all()
	return render(request, "product/product.html", {"product_list": product_list})


def addproduct(request):
	if request.method == 'POST':
		id = request.POST.get("id")
		purchase_date = request.POST.get("purchase_date")
		product_name = request.POST.get("product_name")
		purchase_number = request.POST.get("purchase_number")
		purchase_price = request.POST.get("purchase_price")
		remark = request.POST.get("remark")
		if id == '':
			return HttpResponse('<h3 stytle="color:#c7254e">ID不能为空</h3>')

		product_obj = Product.objects.create(id=id, purchase_date=purchase_date, product_name=product_name, purchase_number=purchase_number, purchase_price=purchase_price, remark=remark)
		return redirect("/product/")
	return render(request, 'product/addproduct.html', locals())


def delproduct(request, id):
	product_obj = models.Product.objects.filter(pk=id).first()
	product_obj.delete()
	return redirect("/product/")


def editproduct(request, id):
	product_obj = Product.objects.filter(pk=id).first()
	if request.method == 'POST':
		purchase_date = request.POST.get("purchase_date")
		product_name = request.POST.get("product_name")
		purchase_number = request.POST.get("purchase_number")
		purchase_price = request.POST.get("purchase_price")
		remark = request.POST.get("remark")

		Product.objects.filter(pk=id).update(id=id, purchase_date=purchase_date, product_name=product_name, purchase_number=purchase_number, purchase_price=purchase_price, remark=remark)
		return redirect("/product/")
	return render(request, 'product/editproduct.html', {"product_obj": product_obj})


# 查看农作记录
def croprecords(request):
	croprecords_list = CropRecords.objects.all()
	return render(request, "croprecords/croprecords.html", {"croprecords_list": croprecords_list})


def addcroprecords(request):
	if request.method == 'POST':
		id = request.POST.get("id")
		croprecords_date = request.POST.get("croprecords_date")
		land_id = request.POST.get("land_id")
		tlc = request.POST.get("tlc")
		crop_name = request.POST.get("crop_name")
		naworm = request.POST.get("naworm")
		nanosu = request.POST.get("nanosu")

		croprecords_obj = CropRecords.objects.create(id=id, croprecords_date=croprecords_date, land_id=land_id, tlc=tlc, crop_name=crop_name,naworm=naworm, nanosu=nanosu)
		return redirect("/croprecords/")
	return render(request, 'croprecords/addcroprecords.html', locals())


def delcroprecords(request, id):
	croprecords_obj = models.CropRecords.objects.filter(pk=id).first()
	croprecords_obj.delete()
	return redirect("/croprecords/")


def editcroprecords(request, id):
	croprecords_obj = CropRecords.objects.filter(pk=id).first()
	if request.method == 'POST':
		croprecords_date = request.POST.get("croprecords_date")
		land_id = request.POST.get("land_id")
		tlc = request.POST.get("tlc")
		crop_name = request.POST.get("crop_name")
		naworm = request.POST.get("naworm")
		nanosu = request.POST.get("nanosu")

		CropRecords.objects.filter(pk=id).update(croprecords_date=croprecords_date, land_id=land_id, tlc=tlc, crop_name=crop_name, naworm=naworm, nanosu=nanosu)
		return redirect("/croprecords/")
	return render(request, 'croprecords/editcroprecords.html', {"croprecords_obj": croprecords_obj})

# 查看实际采收记录
def recovery(request):
	recovery_list = Recovery.objects.all()
	return render(request, "recovery/recovery.html", {"recovery_list": recovery_list})


def addrecovery(request):
	if request.method == 'POST':
		id = request.POST.get("id")
		recovery_date = request.POST.get("recovery_date")
		vegetables_name = request.POST.get("vegetables_name")
		recovery_number = request.POST.get("recovery_number")
		price = request.POST.get("price")

		recovery_obj = Recovery.objects.create(id=id, recovery_date=recovery_date, vegetables_name=vegetables_name, recovery_number=recovery_number, price=price)
		return redirect("/recovery/")
	return render(request, 'recovery/addrecovery.html', locals())


def delrecovery(request, id):
	recovery_obj = models.Recovery.objects.filter(pk=id).first()
	recovery_obj.delete()
	return redirect("/recovery/")


def editrecovery(request, id):
	recovery_obj = Recovery.objects.filter(pk=id).first()
	if request.method == 'POST':
		id = request.POST.get("id")
		recovery_date = request.POST.get("recovery_date")
		vegetables_name = request.POST.get("vegetables_name")
		recovery_number = request.POST.get("recovery_number")
		price = request.POST.get("price")

		Recovery.objects.filter(pk=id).update(id=id, recovery_date=recovery_date, vegetables_name=vegetables_name, recovery_number=recovery_number, price=price)
		return redirect("/recovery/")
	return render(request, 'recovery/editrecovery.html', {"recovery_obj": recovery_obj})


def page_not_found(request):
	return render_to_response('error/404.html')


def page_error(request):
	return render_to_response('error/500.html')
