from django.db import models
from django.core.urlresolvers import reverse
from django import forms

'''
 This is the database for Day

 +---------------------------+
 |        Day                |
 |---------------------------|
 |          |                |
 |   date   |   DateField    |
 |          |                |
 |----------|----------------|
 |          |                |
 | numTran  | IntegerField   | 
 |          |                |
 +---------------------------+

'''
class Day(models.Model):
	'''
	  This is a table to store day information
	'''
	date = models.DateField()
	numTran = models.PositiveIntegerField(default=0)

	def get_absolute_url(self):
		return reverse('database:specific', kwargs={'year': date.year, 'month': date.month, 'day': date.day})

	def __str__(self):
		return "{0}-{1}-{2}".format(self.date.year, self.date.month, self.date.day)

	def total(self):
		total = 0
		for t in self.transaction_set.all():
			total += t.amount
		total = format(total, '.2f')
		return total

	def numTrans(self):
		return self.transaction_set.count()

	class Meta:
		ordering = ['date']


class DayForm(forms.ModelForm):
	class Meta:
		model = Day
		exclude = ['numTran']



'''
 This is the database for Transaction

 +---------------------------+
 |        Transaction        |
 |---------------------------|
 |          |                |
 |   day    |   Model:Day    |
 |          |                |
 |----------|----------------|
 |          |                |
 | usage    |   CharField    | 
 |          |                |
 |---------------------------|
 |          |                |
 |  amount  |   FloatField   |
 |          |                |
 |---------------------------|
 |          |                |
 |   des    |   TextField    |
 |          |                |
 +---------------------------+

'''

class Transaction(models.Model):
	'''
      This is a table to store transactions in specific day
	'''

	usage_choice = (
		('cloth', 'cloth'),
		('restaurant', 'restaurant'),
		('grocery', 'grocery'),
		('bill', 'bill'),
		('other', 'other'),
		)

	day = models.ForeignKey(Day, on_delete=models.CASCADE)
	usage = models.CharField(max_length=20, choices=usage_choice, default='cloth')
	amount = models.FloatField()
	des = models.TextField('description', blank=True)

	def __str__(self):
		return "{0} {1}-{2}-{3} (${4})".format(self.usage, 
			       self.day.date.year, self.day.date.month, self.day.date.day, self.amount)

	class Meta:
		ordering = ['day']


class TransactionForm(forms.ModelForm):
	class Meta:
		model = Transaction
		exclude = ['day']


