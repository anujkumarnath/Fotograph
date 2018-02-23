from django.shortcuts import render,redirect
from airtable import Airtable
import os

AT=Airtable(os.environ.get('AIRTABLE_PHOTOSTABLE_BASE_ID'),
                          'Fotograph',
                          api_key=os.environ.get('AIRTABLE_API_KEY'))
# Create your views here.
def home_page(request):
    user_query=str(request.GET.get('query',''))
    search_result=AT.get_all(formula="FIND('"+ user_query.lower() +"',LOWER({Caption}))")
    stuff_for_frontend={'search_result':search_result}
    return render(request, 'photos/photos_stuff.html', stuff_for_frontend)
def add(request):
    if request.method=="POST":
        data={
            "Caption": request.POST.get("caption"),
            "Photo" : [{"url":request.POST.get("url")}],
            "Date" : request.POST.get("date"),
            "Rating" : int(request.POST.get("rating")),
            "Comment" : request.POST.get("comment")
        }
        print(data)
        AT.insert(data)
    return redirect('/')
