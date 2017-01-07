from django.conf.urls import include, url
from .views import main, thisMonth, lastMonth, lastTwoWeek, specific_trans, addDay, addTransaction, DayCreate, display_meta, category, add_date


app_name = 'database'
urlpatterns = [
    url(r'^$', main, name='main'),
    #url(r'^$', Transaction_list.as_view(), name='main'),

    url(r'^thisMonth/$', thisMonth, name='thisMonth'),
    url(r'^lastMonth/$', lastMonth, name="lastMonth"),

    url(r'^lastTwoWeeks/$', lastTwoWeek, name='lastTwoWeek'),
    # /main/transaction/2016-10-12/
    url(r'^transaction/(?P<year>[0-9]{4})-(?P<month>[0-9]{1,2})-(?P<day>[0-9]{1,2})/$', specific_trans, name="specific"),
    url(r'^day/$', addDay, name='addDay'),
    url(r'^addTransaction/(?P<year>[0-9]{4})-(?P<month>[0-9]{1,2})-(?P<day>[0-9]{1,2})/$', addTransaction, name='addTransaction'),

    # /database/day/add/
    url(r'^day/add/$', DayCreate.as_view(), name='day_create'),

    url(r'^meta/$', display_meta, name='meta'),
    url(r'^category/$', category, name='category'),

    url(r'^add_date_practice/$', add_date, name='add_practice'),

]