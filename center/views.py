from django.shortcuts import render
from .models import Center
import datetime as dt
import pandas as pd
import os
from django.conf import settings
from django.core.files.storage import FileSystemStorage

# Create your views here.
def importCSV(request):               
    try:
        if request.method == 'POST' and request.FILES['myfile']:
          
            myfile = request.FILES['myfile']        
            fs = FileSystemStorage()
            filename = fs.save(myfile.name, myfile)
            uploaded_file_url = fs.url(filename)
            excel_file = uploaded_file_url
            # print(excel_file) 
            empexceldata = pd.read_csv("."+excel_file,encoding='utf-8')
            # print(type(empexceldata))
            dbframe = empexceldata
            for dbframe in dbframe.itertuples():
                 
                # fromdate_time_obj = dt.datetime.strptime(dbframe.DOB, '%d-%m-%Y')
                obj = Center.objects.create(name=dbframe.name,description=dbframe.description, price=dbframe.price,
                                                tags=dbframe.tags, imageUrl=dbframe.imageUrl, optionName=dbframe.optionName, hidden=dbframe.hidden, 
                                                weight=dbframe.weight, prepaymentPercent=dbframe.prepaymentPercent, hideBuyBtn=dbframe.hideBuyBtn,
                                                bonusesPercent=dbframe.bonusesPercent)
                # print(type(obj))
                obj.save()
            context =  {'uploaded_file_url': uploaded_file_url}
            return render(request, 'importexcel.html',context)    
    except Exception as identifier:            
        print(identifier)
     
    return render(request, 'importexcel.html',{})