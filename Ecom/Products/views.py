from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def homw(*args,**kwargs):
	return HttpResponse("<h1>hello</h1>")


def contact(request,*args,**kwargs):
	my_list=[]
	for i in range(1,11):
		my_list.append(i)

	context={
		"list"		: my_list
		}

	return render(request,"contact.html",context)
	
