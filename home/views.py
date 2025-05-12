from django.shortcuts import render

def home(request):
    posted = [
        {
            'username' : 'nina_chan',
            'post' : 'Hari ini langitnya cerah',
            'time' : '2025-05-01 08.30',
            'img' : 'https://picsum.photos/200/300'
         },
        {
            'username' : 'nina_chan',
            'post' : 'Hari ini langitnya cerah',
            'time' : '2025-05-01 08.30',
            'img' : 'https://picsum.photos/200/300'
         },
        {
            'username' : 'kevin_chan',
            'post' : 'Ini langitnya cerah',
            'time' : '2025-05-01 08.30',
            'img' : 'https://picsum.photos/200/300'
        },
        {
            'username' : 'fajar_sadboy',
            'post' : 'Hari ini cerah',
            'time' : '2025-05-01 08.30',
            'img' : 'https://picsum.photos/200/300'
        },

    ]
    return render (request,'home.html', {'posting' : posted})
def login(request):
    return render (request,'login.html')
def registrasi(request):
    return render (request,'registrasi.html')
def beranda(request):
    # biodata = {
        #   'username' : 'zarmed',
        # 'nama': 'zarabeys',
        # 'foto-profil' : 'https://picsum.photos/200/200'
    # }
    feed = [
        {
            'username' : 'hanik_nyik',
            'caption' : 'Keindahan',
            'img' : 'https://picsum.photos/200/300',
            'profil' : 'https://picsum.photos/200/200'
        },
        {
            'username' : 'hanik_nyik',
            'caption' : 'Keindahan',
            'img' : 'https://picsum.photos/200/300',
            'profil' : 'https://picsum.photos/200/200'
        },
        {
            'username' : 'hanik_nyik',
            'caption' : 'Keindahan',
            'img' : 'https://picsum.photos/200/300',
            'profil' : 'https://picsum.photos/200/200'
        },
        {
            'username' : 'hanik_nyik',
            'caption' : 'Keindahan',
            'img' : 'https://picsum.photos/200/300',
            'profil' : 'https://picsum.photos/200/200'
        },
        {
            'username' : 'hanik_nyik',
            'caption' : 'Keindahan',
            'img' : 'https://picsum.photos/200/300',
            'profil' : 'https://picsum.photos/200/200'
        },
        {
            'username' : 'hanik_nyik',
            'caption' : 'Keindahan',
            'img' : 'https://picsum.photos/200/300',
            'profil' : 'https://picsum.photos/200/200'
        },
        {
            'username' : 'hanik_nyik',
            'caption' : 'Keindahan',
            'img' : 'https://picsum.photos/200/300',
            'profil' : 'https://picsum.photos/200/200'
        },
        {
            'username' : 'hanik_nyik',
            'caption' : 'Keindahan',
            'img' : 'https://picsum.photos/200/300',
            'profil' : 'https://picsum.photos/200/200'
        },
        {
            'username' : 'hanik_nyik',
            'caption' : 'Keindahan',
            'img' : 'https://picsum.photos/200/300',
            'profil' : 'https://picsum.photos/200/200'
        },
        {
            'username' : 'hanik_nyik',
            'caption' : 'Keindahan',
            'img' : 'https://picsum.photos/200/300',
            'profil' : 'https://picsum.photos/200/200'
        },
    ]
    return render (request,'beranda.html', {'feed':feed})
def chat(request):
    return render (request,'chat.html')
def profil(request):
    datauser = {
        'username' : 'zarmed', 
        'foto_profil' : 'https://picsum.photos/200/200',
        'nama': 'zarabeys',
        'bio' : 'sebebas lautan',
        'url' : 'www.instagram.com/zarmed'
    }
    profile = [
        {
            'feed' : 'https://picsum.photos/200/300'
        },
        {
            'feed' : 'https://picsum.photos/200/300'
        },
        {
            'feed' : 'https://picsum.photos/200/300'
        },
        {
            'feed' : 'https://picsum.photos/200/300'
        },
        {
            'feed' : 'https://picsum.photos/200/300'
        },
        {
            'feed' : 'https://picsum.photos/200/300'
        },
        

    ]
    return render (request,'profil.html', {'profil':profile, 'user':datauser})
def mypost(request):
    return render (request,'mypost.html')
# Create your views here.
