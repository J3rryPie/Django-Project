from django.shortcuts import render
from .models import Curri
from django.db.models import Q
from operator import attrgetter
# Create your views here.
def curri_view(request,query=None):
    #query=""
    context = {}
    if request.GET:
        query=request.GET["q"]
        context['query']=str(query)
        #forid=Curri.objects.filter(id=1)
        search = Curri.objects.filter(
            #Q(title__icontains=forid),
            Q(title__icontains=query)
        ).distinct()
        query = sorted(search, key=attrgetter('title'), reverse=True)
        if len(query)==0 :
            queryset = Curri.objects.all()
            context = {
                "con": queryset
            }
        #print(search)
        #print(query)
        #query=Curri.objects.filter(id=forid)
        context['query']=query
    else:
        queryset = Curri.objects.all()
        context = {
            "con": queryset
        }
    return render(request, "curri/all_curri.html", context)

def all_curri(request):
    queryset = Curri.objects.all()
    context = {
        "con": queryset
    }
    return render(request, "curri/all_curri.html", context)

'''def curri_view(request):
    if request.method == 'GET': # this will be GET now
        title =  request.GET.get('curri_view') # do some research what it does
        try:
            status = Curri.objects.filter(title__icontains=title) # filter returns a list so you might consider skip except part
        return render(request,"curri/all_curri.html",{"con":status})
    else:
        return render(request,"curri/all_curri.html",{})'''

'''def get_queryset(query=None):

    a=Curri.objects.filter(title__contains=query)
    print(a)
    return a
    queryset=[]
    #queries=query.split(" ")
    for q in query:
        search=Curri.objects.filter(
            Q(title__icontains=q)
        ).distinct()
        for s in search:
            queryset.append(s)
    if(queryset!=None):
        return queryset
    else:
        return None
'''
