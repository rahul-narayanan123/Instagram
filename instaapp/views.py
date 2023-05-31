from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
from.models import Post,Comment
from .models import Profile
from.forms import ProfileForm,PostForm,CommentForm
from django.contrib.auth.decorators import login_required



# Create your views here.


def index(request):
    if request.method == 'POST':
        uname=request.POST['username']
        password1=request.POST['password']
        user=auth.authenticate(username=uname,password=password1)
        if user:
            auth.login(request,user)
            return redirect('/home')
        else:
           messages.info(request,"password not matching")
        return redirect('/')

    else:
        return render(request,'index.html',) 

def register(request):
     if request.method =='POST':
        username=request.POST['username']
        fname=request.POST['firstname']
        lname=request.POST['lastname']
        email=request.POST['email']
        password1=request.POST['password']
       

      

        if User.objects.filter(username=username).exists():
            #  return HttpResponse("username taken")
            messages.info(request,"username taken")
            return redirect('register')
            
        elif User.objects.filter(email=email).exists():
            #  return HttpResponse("email taken")
             messages.info(request,"email taken")
             return redirect('register')   
        else:
            user=User.objects.create_user(username=username,email=email,first_name=fname,last_name=lname,password=password1)
            user.save()
            return redirect('/')   
     else:

            return render(request, 'register.html')
     

def home(request):
          a=Post.objects.all()
          form=CommentForm()

          return render(request, 'home.html',{'a':a,'form':form})



        


def myprofile(request):
     
    if request.method == 'POST':   
        form=ProfileForm(request.POST,request.FILES)
        if form.is_valid():
            abc=form.save(commit=False)
            abc.user=request.user
            abc.save()
            return redirect('/')
    else:
        if Profile.objects.filter(user=request.user.id).exists():
            profile=Profile.objects.get(user=request.user.id)   
                # products=Posts.objects.filter(user=request.user.id)
            ab=Post.objects.filter(user=request.user.id)
            
            return render(request,'profile.html',{'profile':profile,'d':ab})
        
        else:
            form=ProfileForm()
            return render(request,'addprofile.html',{'form':form})
         


def logout(request):
    auth.logout(request)        
    return redirect('/') 

def editprofile(request):

    if request.method == 'POST':
        profile=Profile.objects.get(user=request.user.id)
        profile2 = ProfileForm(request.POST,request.FILES,instance=profile )

        if profile2.is_valid():
            profile2.save()
            return redirect('/myprofile')



    else:
        profile=Profile.objects.get(user=request.user.id)
        form = ProfileForm(instance=profile)
        return render(request,'editprofile.html',{'form':form})
    


def addpost(request):

    if request.method == 'POST':
        form=PostForm(request.POST,request.FILES)

        if form.is_valid():
            # post=form.save(commit=False)
            # post.user=request.user
            # post.save()
            form.save()
            return redirect('/home')
    else:
        form=PostForm()   


        return render(request,'addpost.html',{'form':form}) 
    






def editpost(request,id):
   
    if request.method == "POST":
        a = Post.objects.get(id=id)
        form = PostForm(request.POST,request.FILES,instance=a )

        if form.is_valid():
            form.save()
            return redirect('/myprofile')
    else:
        a = Post.objects.get(id=id)
        form = PostForm(instance=a)
        return render(request,'editpost.html',{'form':form})
    


def deletepost(request,a):
    a=Post.objects.get(id=a)
    a.delete()
    return redirect('myprofile')     


def search(request):  
    if request.method == 'POST':
        search = request.POST['search'] 
        pro=Profile.objects.filter(name__icontains=search)
        return render(request,'search.html',{'search':search,'p':pro})

    else:
        return render(request,'search.html')
    


def viewpage(request,id):

    if request.method == 'POST':

        form=CommentForm(request.POST)
        pro=Post.objects.get(id=id)

        if form.is_valid():
            abc=form.save(commit=False)
            abc.user=request.user       
            abc.post=pro
            abc.save()
            return  redirect(f'/comment/{id}')
    else:
        abc=Post.objects.get(id=id)  

        cmt=Comment.objects.filter(post=abc)

        form=CommentForm()
      

        return render(request,'comment.html',{"a":abc, "form":form,"cmt":cmt})  
    

# def viewpage(request):
#     abc=Post.objects.get(id=stud_id)

#     form=commentForm()

#     return render(request,'home.html',{'form':form})

def profileadds(request,id):

   ab=Profile.objects.get(id=id)
   b=Post.objects.filter(user=ab.user)

   return render(request,'profileadd.html',{'a':b,'d':ab})

def searchprofile(request,id):

   ab=Profile.objects.get(id=id)
   b=Post.objects.filter(user=ab.user)

   return render(request,'searchprofile.html',{'a':b,'d':ab})