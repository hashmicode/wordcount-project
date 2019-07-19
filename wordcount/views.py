from django.http import HttpResponse
from django.shortcuts import render
import operator

def homepage(request):
    #return render(request, 'home.html',{'name':'khurram hashmi'})
    return render(request, 'home.html')

# def eggs(request):
#    return HttpResponse("<h1>Eggs are great!</h1>")

def count(request):
    fulltext = request.GET['fulltext']
    wordcount = {}
    wordlist = fulltext.split()
    for word in wordlist:
        if word in wordcount:
            wordcount[word] += 1
        else:
            wordcount[word] = 1

    sortedwords = sorted(wordcount.items(), key=operator.itemgetter(1), reverse= True)

    return render(request, 'count.html', {'fulltext': fulltext,'count': len(wordlist), 'wordcount': sortedwords})

def about(request):
    return render(request, 'about.html')
