from django.shortcuts import render
from .models import Covid19Data
from .forms import DateForm
from math import isnan
import pandas as pd

def index(request):
	covid19Data = []
	date_picked = ''
	Covid19Data.objects.all().delete()	#Clear old data in DB
	if request.method == 'POST':
		form = DateForm(request.POST)
		date = request.POST.getlist('date_picked')[0]   #YYYY-mm-dd
		x = date.split('-')
		date_picked=(x[1]+'-'+x[2]+'-'+x[0])  #mm-dd-YYYY
		
		getCovidData(date_picked)

		covid19Data = Covid19Data.objects	# Get all data in table

	else:
		form = DateForm()

	return render(request, 'index.html', context={'covid19Data': covid19Data, 'form': form, 'date': date_picked})

def getCovidData(date):
	dataSource = 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_daily_reports/'

	try:
		url = dataSource + date + '.csv'
		df = pd.read_csv(url)

		for k in df.to_numpy():
			# Add data to DB
			Covid19Data.objects.create(
				FIPS = None if isnan(k[0]) else k[0],
				Admin = None if k[1]!=k[1] else k[1],
                Province_State = None if k[2]!=k[2] else k[2],
                Country_Region = None if k[3]!=k[3] else k[3],
                Last_Update = None if k[4]!=k[4] else k[4],
                Lat = None if isnan(k[5]) else k[5],
                Long = None if isnan(k[6]) else k[6],
                Confirmed = None if isnan(k[7]) else k[7],
                Deaths = None if isnan(k[8]) else k[8],
                Recovered = None if isnan(k[9]) else k[9],
                Active = None if isnan(k[10]) else k[10],
                Combined_Key = None if k[11]!=k[11] else k[11],
                Incident_Rate = None if isnan(k[12]) else k[12],
                Case_Fatality_Ratio = None if isnan(k[13]) else k[13],
			)

	except:
		print('Error while get covid data!')

