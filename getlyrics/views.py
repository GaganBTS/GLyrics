from django.shortcuts import render
from django.views import View
from .lyrics import Lyrics_Scraping
# Create your views here.
class Homepage(View):
    def get(self,request):
        return render(request,'home.html')
    def post(self,request):
        artist = request.POST['artist']
        song = request.POST['song']
        getlyr = Lyrics_Scraping(artist=artist,song=song)
        mylyrics = getlyr.get_lyrics()
        return render(request,'lyrics.html',{'song':song,'lyrics':mylyrics,'artist':artist})
