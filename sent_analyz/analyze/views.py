from django.shortcuts import render
from .forms import LinkForm
from .models import Links
from .yt import comments
from .analyze import SentimentAnalyzer

# Create your views here.

def index(request):
    form = LinkForm()
    if request.method == 'POST':
        form = LinkForm(request.POST)
        if form.is_valid():
            form.save()
    
    context = {'form': form}
    return render(request, 'analyze/index.html', context)


def output(request):
    urls = Links.objects.all()[0]
    urls = str(urls).split('=')[1]
    url = comments(urls)
    sa = SentimentAnalyzer()
    sa = sa.analyze(url)
    sa1 = sa[0]
    sa2 = sa[1]
    sa3 = sa[2]
    context = {'urls1': sa1, 'urls2': sa2, 'urls3': sa3} 
    return render(request, 'analyze/output.html', context)