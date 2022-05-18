# I have created this file - Nakib
from django.http import HttpResponse
from django.shortcuts import render

#This is for index page
def index(request):
    return render(request, 'index.html')

#This is for analyze page
def analyze(request):
    #Get the text
    djtext = request.GET.get('text', 'default')
    #Get CheckBox value
    removepunc=request.GET.get('removepunc','off')
    fullcaps=request.GET.get('fullcaps','off')
    newlineremover=request.GET.get('newlineremover','off')
    extraspaceremover=request.GET.get('extraspaceremover','off')
    charcounter=request.GET.get('charcounter','off')

#it's work for remove punctuations
    if removepunc=="on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed=""

        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed+char

        params = {'purpose': "Removing Punctuations", 'analyzed_text': analyzed}
        return render(request, 'analyze.html',params)

#it's work for make UpperCase
    elif fullcaps=="on":
        analyzed=""
        for char in djtext:
            analyzed=analyzed + char.upper()

        params = {'purpose': "Change to UpperCase", 'analyzed_text': analyzed}
        return render(request, 'analyze.html',params)

#it's work for New line Removing
    elif newlineremover=="on":
        analyzed=""
        for char in djtext:
            if char != "\n" and char!="\r":
                analyzed=analyzed + char

        params = {'purpose': "Remove New Line", 'analyzed_text': analyzed}
        return render(request, 'analyze.html',params)

#it's work for Extra space remover'
    elif extraspaceremover=="on":
        analyzed=""
        for index, char in enumerate(djtext):
            if not(djtext[index]==" " and djtext[index+1]==" "):
                analyzed=analyzed + char

        params = {'purpose': "Extra Space Remove", 'analyzed_text': analyzed}
        return render(request, 'analyze.html',params)

#it's work for Characters containing
    elif charcounter=="on":
        count=0
        for index, char in enumerate(djtext):
            count+=1

        analyzed = count
        params = {'purpose': "Characters containing", 'analyzed_text': analyzed}
        return render(request, 'analyze.html',params)

#it's work for can't select any CheckBox
    else:
        return HttpResponse('Error You not select the CheckBox')
