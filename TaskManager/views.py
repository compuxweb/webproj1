from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def homepage(request):
    return render(request, 'home.html')

def aboutpage(request):
    return render(request, 'about.html')

def countpage(request):
    fulltext = request.GET['fulltext']
    wordlist = fulltext.split()
    freq = dict()
    for word in wordlist:
        if word in freq:
            freq[word] += 1
        else:
            freq[word] = 1

    sorted_freq = sorted(freq.items(), key=lambda x: x[1], reverse=True)
    
    return render(request, 'count.html', {'fulltext':fulltext, 'count':len(wordlist), 'freq':sorted_freq})
