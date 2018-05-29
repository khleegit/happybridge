from django.shortcuts import render
from django.http import HttpResponse
from .models import Affiliatedstore
from .models import Consumer
from .models import Delivery


# Create your views here.

def index(request):
	return render(request, 'dash/index.html')


def flot(request):
	return render(request, 'dash/flot.html')


def morris(request):
	return render(request, 'dash/morris.html')


def delivery(request):
	moa = Delivery.objects.all()
	error = False
	if 'bp' in request.GET:
		bp = request.GET['bp']
		if not bp:
			error = True	
		else:
			moa = moa.filter(bp_code__icontains = bp)
			cnt = moa.count()
			return render(request, 'dash/delivery.html', {'moa':moa, 'bp' : bp, 'cnt' : cnt})
	cnt = moa.count()
	return render(request, 'dash/delivery.html', {'moa' : moa, 'cnt': cnt})


def affiliated(request):
	moa = Affiliatedstore.objects.all()
	context = {'moa':moa}
	return render(request, 'dash/affiliated.html', context)


def consumer(request):
	moa = Consumer.objects.all()
	context = {'moa':moa}
	return render(request, 'dash/consumer.html', context)


def tables(request):
	return render(request, 'dash/tables.html')


def forms(request):
	return render(request, 'dash/forms.html')


def panels_wells(request):
	return render(request, 'dash/panels_wells.html')


def buttons(request):
	return render(request, 'dash/buttons.html')


def notifications(request):
	return render(request, 'dash/notifications.html')


def typography(request):
	return render(request, 'dash/typography.html')


def icons(request):
	return render(request, 'dash/icons.html')


def grid(request):
	return render(request, 'dash/grid.html')


def blank(request):
	return render(request, 'dash/blank.html')


def login(request):
	return render(request, 'dash/login.html')
	