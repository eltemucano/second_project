from django.shortcuts import render
from time import gmtime, strftime, localtime

import locale
locale.setlocale(locale.LC_ALL, 'es-ES') 
# Create your views here.

def index(request):
    date_time = localtime();
    context = {
        "time": strftime("%H:%M:%S %p", date_time),
        "date": strftime("%d de %B de %Y", date_time),
    }
    return render(request,'index.html', context)