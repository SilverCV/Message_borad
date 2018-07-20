from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
# Create your views here.
def index(request):
	msglist = []
	if request.method == "POST":
		user_a = request.POST.get('userA',None)
		user_b = request.POST.get('userB',None)
		msg = request.POST.get('msg',None)
		date = datetime.now()
		with open("msg.txt",'a+') as f:
			f.write('{}--{}--{}--{}'.format(user_a,user_b,msg,date.strftime("%Y-%m-%d %H:%M:%S")))

	if request.method == 'GET':
		user_c = request.GET.get('userC',None)
		if user_c is not None:
			with open('msg.txt','r') as f:
				for line in f:
					linedata = line.split('--')
					if linedata[1] == user_c:
						msglist.append({'userA':linedata[0],'userB':linedata[1],'msg':linedata[2],'time':linedata[3]})
	return render(request,'index.html',{'data':msglist})