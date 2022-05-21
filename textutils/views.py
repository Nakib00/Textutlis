# I have created this file - Nakib
from django.http import HttpResponse
from django.shortcuts import render

#This is for index page
def index(request):
    return render(request, 'index.html')

#This is for analyze page
def analyze(request):
    #Get the text
    djtext = request.POST.get('text', 'default')
    #Get CheckBox value
    removepunc=request.POST.get('removepunc','off')
    fullcaps=request.POST.get('fullcaps','off')
    newlineremover=request.POST.get('newlineremover','off')
    extraspaceremover=request.POST.get('extraspaceremover','off')
    charcounter=request.POST.get('charcounter','off')

#it's work for remove punctuations
    if removepunc=="on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed=""

        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed+char

        params = {'purpose': "Removing Punctuations", 'analyzed_text': analyzed}
        # return render(request, 'analyze.html',params)
        djtext=analyzed

#it's work for make UpperCase
    if fullcaps=="on":
        analyzed=""
        for char in djtext:
            analyzed=analyzed + char.upper()

        params = {'purpose': "Change to UpperCase", 'analyzed_text': analyzed}
        # return render(request, 'analyze.html',params)
        djtext=analyzed

#it's work for New line Removing
    if newlineremover=="on":
        analyzed=""
        for char in djtext:
            if char != "\n" and char!="\r":
                analyzed=analyzed + char

        params = {'purpose': "Remove New Line", 'analyzed_text': analyzed}
        # return render(request, 'analyze.html',params)
        djtext=analyzed

#it's work for Extra space remover'
    if extraspaceremover=="on":
        analyzed=""
        for index, char in enumerate(djtext):
            if not(djtext[index]==" " and djtext[index+1]==" "):
                analyzed=analyzed + char

        params = {'purpose': "Extra Space Remove", 'analyzed_text': analyzed}
        # return render(request, 'analyze.html',params)
        djtext=analyzed

#it's work for Characters containing
    if charcounter=="on":
        count=0
        for index, char in enumerate(djtext):
            count+=1

        analyzed = count
        params = {'purpose': "Characters containing", 'analyzed_text': analyzed}
        # return render(request, 'analyze.html',params)
        djtext=analyzed

# #it's work for can't select any CheckBox
#     else:
#         return HttpResponse('Error POST')

    if(removepunc != "on" and newlineremover!="on" and extraspaceremover!="on" and fullcaps!="on" and charcounter!="on"):
        return HttpResponse("please select any operation and try again")

    return render(request, 'analyze.html', params)
