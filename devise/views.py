from django.shortcuts import render

import api

# Create your views here.

def index(request):
    return render(request, "index/index.html")

def dashboard(request, days_range=50, currencies="USD"):

    days, rates = api.get_rates(currencies=currencies.split(","), days=days_range)
    page_label = {7: "Week", 30: "Month", 365: "Year"}.get(days_range, "Custom")
    return render(request, "devise/index.html", context={"data": rates,
                                                         "days_labels": days,
                                                         "page_label": page_label,
                                                         "current_currency": currencies
                                                         })