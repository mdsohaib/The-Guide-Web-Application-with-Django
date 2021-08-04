# This file is created by me

from django.http import HttpResponse
from django.shortcuts import render
import string
from textblob import TextBlob
import wikipedia  
#from spellchecker import SpellChecker
#spell = SpellChecker()
def index(response):
    return render(response, 'index.html')

def guide(request):
    #Get the text
    djtext = request.POST.get('text', 'default')
    removep = request.POST.get('removepunc', 'off')
    upperc = request.POST.get('uppercase', 'off')
    lowerc = request.POST.get('lower', 'off')
    newlrem = request.POST.get('newlineremove', 'off')
    extraspace = request.POST.get('extraspaceremove', 'off')
    charcount = request.POST.get('charcount', 'off')
    spell = request.POST.get('spell', 'off')
    wiki = request.POST.get('wiki', 'off')
    stp = request.POST.get('stp', 'off')
    params = {'name': 'Error is', 'string': "You didn't select any operation"}

    if(removep == 'on'):
        res1 = ""
        for i in djtext:
            if(i not in string.punctuation):
                res1 += i
        params = {'name':'Removed Punctuations string is', 'string':res1}
        
        djtext = res1
    if(upperc == 'on'):
        params = {'name': 'Upper Case String is : ', 'string': djtext.upper()}
       
        djtext = djtext.upper()
    if(lowerc == 'on'):
        params = {'name': 'Lower Case String is : ', 'string': djtext.lower()}
        
        djtext = djtext.lower()
    if(newlrem == 'on'):
        res2 = ""
        for i in djtext:
            if not(i=='\n'):
                res2 += i
        params = {'name': 'Removed New Lines', 'string': res2}
       
        djtext = res2
    if(extraspace == 'on'):
        res3 = ""
        for index,char in enumerate(djtext.strip()):
            if not(djtext[index] == ' ' and djtext[index+1]==' '):
                res3 += char
        params = {'name': 'The string without extra space is ', 'string': res3}
      
        djtext = res3
    if(charcount == 'on'):

        params = {'name': 'Number of characters in string is', 'string': "String is : "+ djtext +
                "\nCount is :"+str(len(djtext))}
       
    if(spell == 'on'):
        res5=djtext.lower()
        l=res5.split(" ")
        for i in l:
            b = TextBlob(i)
            c=str(b.correct())
            if c!=i and c!="empty":
                res5=res5.replace(i,c)      
        if(upperc == 'on'):
            params = {'name':'Corrected string is', 'string':res5.upper()}
        else:
            params = {'name':'Corrected string is', 'string':res5}
       
        djtext = res5
    if(wiki == 'on'):
        try:
            result1 = wikipedia.search(djtext, results = 5) 
            result2 = wikipedia.summary(djtext, sentences = 5)  
            res6=result2+"\n\n"+"Enter these words for better accuracy:"+(','.join(result1))
            params = {'name':'Summary For The Word is', 'string':res6}
            djtext = res6
        except:
            res6="Sorry Unable To Generate a Summary for this Word"
            params = {'name':'Summary For The Word is', 'string':res6}
    if(stp == 'on'):
        stop_words = {"ourselves", "hers", "between", "yourself", "but", "again", "there", "about", "once", "during", "out", "very", "having", "with", "they", "own", "an", "be", "some", "for", "do", "its", "yours", "such", "into", "of", "most", "itself", "other", "off", "is", "s", "am", "or", "who", "as", "from", "him", "each", "the", "themselves", "until", "below", "are", "we", "these", "your", "his", "through", "don", "nor", "me", "were", "her", "more", "himself", "this", "down", "should", "our", "their", "while", "above", "both", "up", "to", "ours", "had", "she", "all", "no", "when", "at", "any", "before", "them", "same", "and", "been", "have", "in", "will", "on", "does", "yourselves", "then", "that", "because", "what", "over", "why", "so", "can", "did", "not", "now", "under", "he", "you", "herself", "has", "just", "where", "too", "only", "myself", "which", "those", "i", "after", "few", "whom", "t", "being", "if", "theirs", "my", "against", "a", "by", "doing", "it", "how", "further", "was", "here", "than"}
        s=""
        w =djtext.split()
        for word in w: 
            if word not in stop_words:
                s=s+" "+word
        res7=s
        params = {'name':'After Removal of Stop Words', 'string':res7}
        djtext = res7
    return render(request, 'punc.html', params)
