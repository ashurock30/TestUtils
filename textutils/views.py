# I have created this file  - Ashutosh
from string import punctuation
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    # params = {'name': 'Ashutosh', 'Place': 'Pune'}
    return render(request, 'index.html')
    # return HttpResponse('''<h1>Hello Ashutosh</h1> <a href="http://127.0.0.1:8000/removepunc"> removepunc </a>''')

def analyze(request):
    # Get the text
    djtext = request.POST.get('text', 'default')
    print(djtext)
    
    # Check Box Values
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    remover = request.POST.get('remover', 'off')
    extraspaceremover = request.POST.get('spaceremover', 'off')
    charcounter = request.POST.get('charcounter', 'off')
    # Check which checkbox is on
    if removepunc == "on":
        punctuations = '''!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char

        params = {'purpose': 'Remove Punctuations', 'analyzed_text': analyzed}
        djtext = analyzed
        # return render(request, 'analyze.html', params)

    if fullcaps == "on":
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.capitalize()
        params = {'purpose': 'Changed to Upper', 'analyzed_text': analyzed}
        djtext = analyzed
        # return render(request, 'analyze.html', params)

    if remover == "on":
        analyzed = ""
        for char in djtext:
            if char != "\n" and char != "\r":
                analyzed = analyzed + char
        params = {'purpose': 'Removed New Lines', 'analyzed_text': analyzed}
        djtext = analyzed
        #  return render(request, 'analyze.html', params)

    if extraspaceremover == "on":
        analyzed = ""
        for index, char in enumerate(djtext):
            if not(djtext[index] == " " and djtext[index+1] == " "):
                analyzed = analyzed + char

        params = {'purpose': 'Removed Spaces', 'analyzed_text': analyzed}
        djtext = analyzed
        # return render(request, 'analyze.html', params)
        
    if charcounter == "on":
        analyzed = ""
        analyzed = len(djtext)

        params = {'purpose': 'Char Count', 'analyzed_text': analyzed}
        # return render(request, 'analyze.html', params)
    
    
    if(removepunc != "on" and remover!="on" and extraspaceremover!="on" and fullcaps!="on" and charcounter != "on"):
        return HttpResponse("please select any operation and try again")

    return render(request, 'analyze.html', params)
    

# def removepunc(request):
#     # Get the text
#     print(request.GET.get('text', 'default'))
#     # Analyze the text
#     return HttpResponse("remove punc")

# def capfirst(request):
#     return HttpResponse("Capatalize First")

# def newlineremove(request):
#     return HttpResponse('''<h1>Remove New Line</h1> <a href='/'> back </a>''')


# def spaceremoval(request):
#     return HttpResponse('''<h1>Remove Space</h1> <a href='/'> back </a>''')


# def charcounter(request):
#     return HttpResponse('''<h1>Count Char</h1> <a href='/'> back </a>''')
