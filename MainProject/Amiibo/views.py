# To understand the program flow a little better, this is how we got here (I think):
# >>> MainProject.urls reads the URL
# >>> MainProject.urls sees amiibo/ at end of URL so gos to Amiibo.url
# >>> Amiibo.urls reads the URL
# >>> Amiibo.urls, depending on what it reads, one of the functions below is run.

from django.shortcuts import render

# Called when Amiibo/urls.py sees  ''  at the end of the URL
# Returns the HTML file amiibo_home.html
def amiibo_home(request):
    return render(request, 'Amiibo/amiibo_home.html')

# Called when Amiibo/urls.py sees  'yourcollection'  at the end of the URL
# Returns the HTML file amiibo_db.html
def amiibo_db(request):
    return render(request, 'Amiibo/amiibo_db.html')

# Called when Amiibo/urls.py sees  'amiibolist'  at the end of the URL
# Returns the HTML file amiibo_api.html
def amiibo_api(request):
    return render(request, 'Amiibo/amiibo_api.html')

# Called when Amiibo/urls.py sees  'nintendonews'  at the end of the URL
# Returns the HTML file amiibo_news.html
def amiibo_news(request):
    return render(request, 'Amiibo/amiibo_news.html')