from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect
from django.views import generic
from .models import Album,Song
from django.views.generic import View
from .forms import ContactForm,SignInForm,AddalbumForm,AddSongForm
from django.core.mail import send_mail
from django.contrib.auth import authenticate,login,logout
from django.shortcuts import get_object_or_404

def IndexView(request):
    context = Album.objects.filter(pk__in=range(1,8))
    return render(request,'music/index.html',{'all_albums': context})

class ContactView(View):
    form_class = ContactForm
    template_name = "music/contact.html"
    def get(self,request):
        form = self.form_class(None)
        return render(request,self.template_name,{'form':form,})

    def post(self,request):
        form = self.form_class(request.POST)

        if form.is_valid():
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            sender = form.cleaned_data['sender']
            receivers = ['gaurav_setia@yahoo.com']
            send_mail(subject, message, sender, receivers)
            return redirect('music:thanks')
        return render(request, self.template_name, {'form':self.form_class(None),'error_message':"Please Fill the Form again",})

def thankyou(request):
    template_name = "music/thanks.html"
    return render(request,template_name)


class Signin(View):
    form_class =  SignInForm
    template_name = "music/signin.html"
    def get(self,request):
        form = self.form_class(None)
        return render(request,self.template_name,{"form":form,})

    def post(self,request):
        form = self.form_class(request.POST)

        if form.is_valid():

            user = form.save(commit=False)
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            email = form.cleaned_data['email']
            user.set_password(password)
            user.save()

            user = authenticate(username=username,password=password)
            if user is not None:
                if user.is_active:
                    login(request,user)
                    logged = request.user.is_authenticated()
                    return render(request,'music/index.html',{'all_albums':Album.objects.all(),'logged':logged})
            return render(request, self.template_name, {"form": form,})
        return render(request, self.template_name, {"form": form,})



def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username,password=password)

        if user is not None:
            if user.is_active:
                login(request,user)
                logged = request.user.is_authenticated()
                return render(request, 'music/index.html', {'all_albums': Album.objects.all(), 'logged': logged})
            return render(request, 'music/index.html', {'all_albums': Album.objects.all(), 'error_message': 'Your Account is not active'})
        return render(request, 'music/index.html',{'all_albums': Album.objects.all(), 'error_message': 'Wrong Username or password'})
    else:
        logged = request.user.is_authenticated()
        if logged:
            return render(request, 'music/index.html',{'all_albums': Album.objects.all(), 'error_message': 'You are already logged in'})
        else:
            return render(request,'music/login.html')



def logout_user(request):
    if request.user.is_authenticated():
        logout(request)
        return render(request,"music/index.html",{'all_albums':Album.objects.all(),'error_message': 'You have successfully logged out'})
    else:
        return render(request, 'music/index.html',{'all_albums': Album.objects.all(), 'error_message': 'Login First :)'})

class add_album(View):
    form_class = AddalbumForm
    template_name = 'music/add.html'
    def get(self,request):
        form = self.form_class(None)
        return render(request,'music/add.html', {'form':form })

    def post(self,request):

        form = self.form_class(request.POST or None,request.FILES or None)
        if not request.user.is_authenticated():
            return render(request, 'music/index.html',{'all_albums': Album.objects.all(), 'error_message': 'Login First :)'})
        if form.is_valid():
            album = form.save(commit=False)
            album.user = request.user
            album.album_logo = request.FILES['album_logo']
            album.save()
            return render(request, 'music/index.html',{'all_albums': Album.objects.all(), 'error_message': 'Album successfully added'})
        return render(request, template_name, {'form': form,})

def songs(request):
    if not request.user.is_authenticated():
        return render(request, 'music/index.html',{'all_albums': Album.objects.all(), 'error_message': 'Login First :)'})
    try:
        song_id = []
        user_albums = Album.objects.filter(user=request.user)
        for album in user_albums:
            for song in album.song_set.all():
                song_id.append(song.pk)

        user_songs = Song.objects.filter(pk__in=song_id)
    except:
        user_songs = []
    return render(request, 'music/songs.html', {'song_list': user_songs,})


class addsong(View):
    form_class = AddSongForm
    template_name = 'music/addsong.html'

    def get(self,request):
        form = self.form_class(None)
        return render(request,'music/addsong.html',{'form':form,})

    def post(self,request):
        form = self.form_class(request.POST or None, request.FILES or None)
        if form.is_valid():
            form.save()
        return render(request, 'music/index.html', {'all_albums': Album.objects.all()})




def albums(request):
    all_albums = Album.objects.filter(user=request.user)
    return render(request,'music/albums.html',{'all_albums': all_albums})

class details(generic.DetailView):
    model = Album
    template_name = 'music/details.html'


def songdelete(request,pk):
    song = Song.objects.get(pk=pk)
    song.delete()
    all_albums = Album.objects.filter(user=request.user)
    return render(request, 'music/albums.html', {'all_albums': all_albums})









