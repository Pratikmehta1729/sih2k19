from django.shortcuts import render
from blog.models import sampleemp
from django.http import HttpResponse

# Create your views here.
def fetch(request):

	truck_type = str(request.POST.get('truck_type'))
	no_row = int(request.POST.get('no_row'))	


	if(no_row==1):
		d1 = str(request.POST.get('d1'))
		q1 = str(request.POST.get('q1'))
		obj1= sampleemp.objects.all().filter(PRODUCT_CODE=d1)

		return render(request, 'algo.html', {'d1':obj1[0].DIAMETER, 'q1':q1})

	

	elif(no_row==2):
		d1 = str(request.POST.get('d1'))
		q1 = str(request.POST.get('q1'))
		d2 = str(request.POST.get('d2'))
		q2 = str(request.POST.get('q2'))
		obj1= sampleemp.objects.all().filter(PRODUCT_CODE=d1)
		obj2= sampleemp.objects.all().filter(PRODUCT_CODE=d2)
		return render(request, 'algo.html', {'d1':obj1[0].DIAMETER, 'q1':q1, 'd2':obj2[0].DIAMETER, 'q2':q2})


	elif(no_row==3):

		d1 = str(request.POST.get('d1'))
		q1 = str(request.POST.get('q1'))
		d2 = str(request.POST.get('d2'))
		q2 = str(request.POST.get('q2'))
		d3 = str(request.POST.get('d3'))
		q3 = str(request.POST.get('q3'))
		obj1= sampleemp.objects.all().filter(PRODUCT_CODE=d1)
		obj2= sampleemp.objects.all().filter(PRODUCT_CODE=d2)


		obj3= sampleemp.objects.all().filter(PRODUCT_CODE=d3)

		return render(request, 'algo.html', {'d1':obj1[0].DIAMETER, 'q1':q1, 'd2':obj2[0].DIAMETER, 'q2':q2,'d3':obj3[0].DIAMETER, 'q3':q3})




def index(request):
		return render(request, 'index.html')	

