from django.shortcuts import render, redirect

def index(request):
    return render(request, 'survey/index.html')

def process(request):
    print 'processing'
    #here is where we would insert things to database

    return redirect(result)

def result(request):

    return render(request, 'survey/result.html')
