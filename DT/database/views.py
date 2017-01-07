from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, Http404, HttpResponseRedirect
from .models import Day, Transaction, DayForm
from django.template import loader
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView


from datetime import date, timedelta

import plotly
from plotly.graph_objs import Bar, Scatter, Figure, Layout
import plotly.plotly as py



# main, lastMonth, lastTwoWeek method shows the transaction record for customer
def main(request):
	transaction_list = Day.objects.all().filter()
	template = loader.get_template('database/main.html')
	context = {
	  'transaction_list': transaction_list,
	}
	return HttpResponse(template.render(context, request))


'''
class Transaction_list(ListView):
	model = Day
	context_object_name = 'transaction_list'
	template_name = 'database/main.html'
'''

def thisMonth(request):
	transaction_list = Day.objects.all().filter(date__month=date.today().month, date__year=date.today().year)
	template = loader.get_template('database/main.html')
	context = {
	  'transaction_list': transaction_list,
	}
	return HttpResponse(template.render(context, request))

def lastMonth(request):
	thisMonth = date.today().month
	if thisMonth > 1:
		transaction_list = Day.objects.all().filter(date__month=date.today().month - 1, date__year=date.today().year)
	elif thisMonth == 1:
		transaction_list = Day.objects.all().filter(date__month= 12, date__year = date.today().year-1)
	template = loader.get_template('database/main.html')
	context = {
	  'transaction_list': transaction_list,
	}
	return HttpResponse(template.render(context, request))


def lastTwoWeek(request):
	weekday = date.today().weekday()
	endDay = date.today() - timedelta(days=weekday+1)
	startDay = endDay - timedelta(weeks=2) + timedelta(days=1)
	transaction_list = Day.objects.all().filter(date__range=(startDay, endDay))
	template = loader.get_template('database/main.html')
	context = {
	  'transaction_list': transaction_list,
	}
	return HttpResponse(template.render(context, request))

## =======================================================================================================================
'''
def main(request):
	transaction_list = Day.objects.all().filter(date__month=date.today().month, date__year=date.today().year)
	template = loader.get_template('database/main.html')
	form = DayForm()
	context = {
	  'transaction_list': transaction_list,
	  'form': form,
	}
	if request.method == 'GET':
		return HttpResponse(template.render(context, request))
	else:
		form = DayForm(request.POST)
		if form.is_valid():
			date_input = form.cleaned_data['date']
			year, month, day = date_input.split('-')
			Day.objects.create(date=date(Y,M,D))
			form = DayForm()
			return HttpResponse(template.render(context, request))
		else:
			return HttpResponse(template.render(context, request))

'''


def specific_trans(request, year, month, day):
	try:
		day_transaction = Day.objects.get(date = date(int(year),int(month), int(day)))
	except Day.DoesNotExist:
		raise Http404("The date you request does not exist")
	total = 0
	for t in day_transaction.transaction_set.all():
		total += t.amount

	template = loader.get_template('database/trans.html')
	context = {
	  'one_day_transaction': day_transaction.transaction_set.all(),
	  'total': total,
	  'year': year,
	  'month': month,
	  'day': day,
	  'date': '{0}-{1}-{2}'.format(year, month, day),
	}
	return HttpResponse(template.render(context, request))


class DayCreate(CreateView):
	model = Day
	fields = ['date']


def addDay(request):
	try:
		Y = int(request.POST['Year'])
		M = int(request.POST['Month'])
		D = int(request.POST['Day'])
		Day.objects.create(date=date(Y,M,D))
	except KeyError:
		return HttpResponseRedirect('/database/')
	return HttpResponseRedirect('/database/')
	#return main(request)



def addTransaction(request, year, month, day):
	day_transaction = get_object_or_404(Day, date = date(int(year),int(month), int(day)))
	u = request.POST['type']
	a = request.POST['amount']
	d = request.POST['des']
	day_transaction.transaction_set.create(usage=u, amount=float(a), des=d)
	return specific_trans(request, year, month, day)
	

# A view to display all of the request.META data

def display_meta(request):
	values = request.META.items()
	html = ''
	for k, v in values:
		html += '<tr><td>{0}</td> <td>{1}</td></tr>'.format(k, v)
	return HttpResponse('<table>{0}</table>'.format(html))



def category(request):
	all_days = Day.objects.all()
	cloth = 0
	restaurant = 0
	grocery = 0
	bill = 0
	other = 0

	for day in all_days:
		all_trans = day.transaction_set.all()
		cloth += len([tran for tran in all_trans if tran.usage == 'cloth'])
		restaurant += len([tran for tran in all_trans if tran.usage == 'restaurant'])
		grocery += len([tran for tran in all_trans if tran.usage == 'grocery'])
		bill += len([tran for tran in all_trans if tran.usage == 'bill'])
		other = len([tran for tran in all_trans if tran.usage == 'other'])
	total = cloth+restaurant+grocery+bill+other

	data = [{'labels': ['Cloth', 'Restaurant', 'Grocery', 'Bill', 'Others'],
		          'values': [cloth/total, restaurant/total, grocery/total, bill/total, other/total],
		          'type': 'pie'}]
	layout = Layout(title= 'Summary By Category')
	fig = Figure(data=data, layout=layout)
	py.image.save_as(fig, './database/static/database/images/my_plot.png')

	template = loader.get_template('database/category.html')
	return HttpResponse(template.render(request))


# this is practice
from .forms import ContactForm

def add_date(request):
	if request.method == 'POST':
		form = ContactForm(request.POST)
		if form.is_valid():
			return HttpResponse("Thank you")
	else:
		form = ContactForm()
	return render(request, 'database/add_date_practice.html', {'form': form})


    


		



