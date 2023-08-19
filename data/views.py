from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm
from . models import *
import json
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from . decorators import unauthenticated_user, allowed_users
from django.views.decorators.csrf import csrf_exempt

# @login_required(login_url='sign-in')

# to link user with group
from django.contrib.auth.models import Group

# Create your views here.
@csrf_exempt
def home(request):
    if request.method == "GET":
        userMsg = request.GET.get('userMsg')
        f_nameForNoneUser = request.GET.get('AnonName')
        f_emailForNoneUser = request.GET.get('AnonEmail')
        if request.user.is_authenticated:
            if userMsg is None:
                pass
            else:
                if UserMsg.objects.filter(msg = userMsg,user = request.user.Profile):
                    pass
                else:
                    UserMsg.objects.create(msg = userMsg,name_f=request.user.Profile.name_f,name_l=request.user.Profile.name_l,user = request.user.Profile,email = request.user.Profile.email)
                    messages.success(request, 'Your Message Sent Successfully')
        else:
            if userMsg is None:
                pass
            else:
                if UserMsg.objects.filter(msg = userMsg):
                    pass
                else:
                    UserMsg.objects.create(msg = userMsg,name_for_nonUser = f_nameForNoneUser, email = f_emailForNoneUser)
                    messages.success(request, 'Your Message Sent Successfully')
                    return redirect('home')
    # comment delete
    if request.method == "GET":
        action = request.GET.get('action')
        comId = request.GET.get('ComId')
        comment = Comment.objects.filter(id = comId)
        
        if comId == "":
            pass
        else:
            if comment:
                com = Comment.objects.get(id = comId)
                if action == "delete":
                    comment.delete()
                    return redirect('/#comments')
                elif action == "favourite":
                    com.favourite = True
                    com.save()
                    messages.success(request, 'Comment added to favourite')
                    return redirect('/#comments')
                elif action == "delete-favourite":
                    com.favourite = False
                    com.save()
                    messages.success(request, 'Comment removed from favourite')
                    return redirect('/#comments')
                elif action == "best":
                    com.best = True
                    com.save()
                    messages.success(request, 'Comment added to best')
                    return redirect('/#comments')
                elif action == "delete-best":
                    com.best = False
                    com.save()
                    messages.success(request, 'Comment removed from best')
                    return redirect('/#comments')
                

    # add comment 
    userComment = request.POST.get('commet-user')
    if request.user.is_authenticated:
        if request.method == "POST":
            if Comment.objects.filter(commet = userComment , user = request.user.Profile):
                pass
            else:
                if(userComment != ""):
                    Comment.objects.create(commet = userComment, user = request.user.Profile)
                    return redirect('/#comments')
    projects = Project.objects.all()
    
    context = {
        'comments':Comment.objects.all(),
        'About':About.objects.all(),
        'blog':Plog.objects.all(),
        'projects':projects,
        'social': SocialLinks.objects.all(),
    }
    return render(request, 'index.html', context)

def project_view(request):
    data = json.loads(request.body)
    projectId = data['projectId']
    project = Project.objects.get(id=projectId)
    projectImgs = ProjectPhoto.objects.get(project=project)
    print(projectImgs.img1)
    return JsonResponse(f'{projectImgs.img1},{projectImgs.img2},{projectImgs.img3}', safe=False)

# Dashboard

@login_required(login_url='login')
def dashboard(request):
    # blog data
    if request.method == "GET":
        logo = request.GET.get('logo')
        plogName = request.GET.get('plogName')
        data = Plog.objects.all()[0]
        if logo is not None and plogName is not None:
            data.logo = logo
            data.plogName = plogName
            data.save()
            messages.success(request, 'Update successfully')
    # about
    if request.method == "GET":
        sec1 = request.GET.get('sec1')
        sec2 = request.GET.get('sec2')
        sec3 = request.GET.get('sec3')
        sec4 = request.GET.get('sec4')
        secSkills = request.GET.get('secSkills')
        dataAbout = About.objects.all()[0]
        if sec1 is not None and sec2 is not None and sec3 is not None and sec4 is not None and secSkills is not None:
            dataAbout.aboutS1 = sec1
            dataAbout.aboutS2 = sec2
            dataAbout.aboutS3 = sec3
            dataAbout.aboutS4 = sec4
            dataAbout.aboutSkills = secSkills
            dataAbout.save()
            messages.success(request, 'Update successfully')
    
    # settings
    if request.method == "GET":
        social = SocialLinks.objects.all()[0]
        face = request.GET.get('facebook')
        insta = request.GET.get('instagram')
        git = request.GET.get('github')
        linked = request.GET.get('linkedin')
        # wats = request.GET.get('watsapp')
        if face is not None and insta is not None and git is not None and linked is not None:
            social.facebook = face
            social.instagram = insta
            social.github = git
            social.linkedin = linked
            # social.watsapp = wats
            social.save()
            messages.success(request, 'Update successfully')
    
    if request.user.is_authenticated:
        if request.user.Profile.admin == True or request.user.Profile.assistant == True:
            context = {
                'userMsgs':UserMsg.objects.all(),
                'msgNumber':UserMsg.objects.all().count(),
                'blog':Plog.objects.all(),
                'myblog':Plog.objects.all()[0],
                'about':About.objects.all()[0],
                'users':Profile.objects.all(),
                'users_number':Profile.objects.all().count(),
                'social': SocialLinks.objects.all(),
                'socialInput': SocialLinks.objects.all()[0],
                'projects':Project.objects.all(),
            }
            return render(request, 'pages/dashboard.html',context)
        else:
            return redirect("home")
    else:
        return redirect("home")
    

@csrf_exempt
def editUser(request,pk):
    if request.user.Profile.admin == True:
        user = User.objects.get(id = pk)
        userProfile = Profile.objects.get(user = user)
        if request.method == "POST":
            isAdmin = request.POST.get("admin")
            isAssistant = request.POST.get("assistant")
            if isAdmin == "on":
                userProfile.admin = True
            else:
                userProfile.admin = False
                
            if isAssistant == "on":
                userProfile.assistant = True
            else:
                userProfile.assistant = False
            userProfile.save()
            return redirect(f'/editUser/{user.id}')

        context = {
            'blog':Plog.objects.all(),
            'userId':userProfile,
            'comments': Comment.objects.filter(user=userProfile),
            'comCount': Comment.objects.filter(user=userProfile).count(),
            'msg': UserMsg.objects.filter(user=userProfile),
            'msgCount': UserMsg.objects.filter(user=userProfile).count(),
            'userrr':user,
            'social': SocialLinks.objects.all(),
        }
        return render(request, 'pages/editUser.html', context)
    else:
        return redirect("dashboard")
    
# user profile
@csrf_exempt
def userProfile(request,pk):
    user = User.objects.get(id = pk)
    userProfile = Profile.objects.get(user = user)
    if request.method == "POST":
        f_name = request.POST.get('f_name')
        l_name = request.POST.get('l_name')
        username = request.POST.get('username')
        email = request.POST.get('email')
        image = request.FILES.get('image')
        userProfile.name_f = f_name
        userProfile.name_l = l_name
        if image is not None:
            userProfile.img = image
        user.username = username
        user.email = email
        userProfile.save()
        user.save()
        messages.success(request, 'Update successfully')
    context = {
        'blog':Plog.objects.all(),
        'userId':userProfile,
        'comments': Comment.objects.filter(user=userProfile),
        'comCount': Comment.objects.filter(user=userProfile).count(),
        'msg': UserMsg.objects.filter(user=userProfile),
        'msgCount': UserMsg.objects.filter(user=userProfile).count(),
        'social': SocialLinks.objects.all(),
    }
    return render(request, 'pages/userProfile.html', context)

# edit project
@csrf_exempt
def edit_project(request,pk):
    if request.user.is_authenticated:
        if request.user.Profile.admin == True or request.user.Profile.assistant == True:
            project = Project.objects.get(id = pk)
            projectImgs = ProjectPhoto.objects.get(project=project)
            if request.method == "GET":
                action = request.GET.get('action')
                if action == "delete":
                    project.delete()
                    return redirect('dashboard')
            if request.method == "POST":
                projectName = request.POST.get('projectName')
                projectDescription = request.POST.get('projectDescription')
                projectLink = request.POST.get('link')
                if projectName is not None or projectDescription is not None:
                    image = request.FILES.get('pro-image')
                    project.name = projectName
                    project.description = projectDescription
                    project.link = projectLink
                    # langs used in project
                    js = request.POST.get('javascript')
                    html = request.POST.get('html')
                    css = request.POST.get('css')
                    dj = request.POST.get('django')
                    bootS = request.POST.get('bootstrap')
                    py = request.POST.get('python')
                    bostG = request.POST.get('postgresql')

                    if js == "on":
                        project.js = True
                    else:
                        project.js = False
                    if html == "on":
                        project.html = True
                    else:
                        project.html = False
                    if css == "on":
                        project.css = True
                    else:
                        project.css = False
                    if dj == "on":
                        project.dj = True
                    else:
                        project.dj = False
                    if bootS == "on":
                        project.bootS = True
                    else:
                        project.bootS = False
                    if py == "on":
                        project.py = True
                    else:
                        project.py = False
                    if bostG == "on":
                        project.bostG = True
                    else:
                        project.bostG = False

                    if image is not None:
                        project.img = image
                    project.save()
                    messages.success(request, 'Update successfully')
        
            if request.method == "POST":
                imgNum = request.POST.get('imgNum')
                projectImage = request.FILES.get('proImg')
                if imgNum == 'img1' or imgNum == 'img2' or imgNum == 'img3':
                    if imgNum == 'img1':
                        if(projectImage is not None):
                            projectImgs.img1 = projectImage
                            projectImgs.save()
                    if imgNum == 'img2':
                        if(projectImage is not None):
                            projectImgs.img2 = projectImage
                            projectImgs.save()
                    if imgNum == 'img3':
                        if(projectImage is not None):
                            projectImgs.img3 = projectImage
                            projectImgs.save()

            context = {
                'blog':Plog.objects.all(),
                'project':project,
                'projectImgs':projectImgs,
                'social': SocialLinks.objects.all(),
            }
            return render(request, 'pages/editProject.html', context)
        else:
            return redirect('home')
    else:
        return redirect('home')
# add project
@csrf_exempt
def addProject(request):
    if request.user.is_authenticated:
        if request.user.Profile.admin == True or request.user.Profile.assistant == True:
            if request.method == 'POST':
                name = request.POST.get('name')
                description = request.POST.get('description')
                link = request.POST.get('link')
                mainImg = request.FILES.get('main-img')
                img1 = request.FILES.get('img1')
                img2 = request.FILES.get('img2')
                img3 = request.FILES.get('img3')

                # langs used in project
                js = request.POST.get('javascript')
                html = request.POST.get('html')
                css = request.POST.get('css')
                dj = request.POST.get('django')
                bootS = request.POST.get('bootstrap')
                py = request.POST.get('python')
                bostG = request.POST.get('postgresql')

                newProject = Project(name = name, description = description, img = mainImg, link = link)
                if js == "on":
                    newProject.js = True
                else:
                    newProject.js = False
                if html == "on":
                    newProject.html = True
                else:
                    newProject.html = False
                if css == "on":
                    newProject.css = True
                else:
                    newProject.css = False
                if dj == "on":
                    newProject.dj = True
                else:
                    newProject.dj = False
                if bootS == "on":
                    newProject.bootS = True
                else:
                    newProject.bootS = False
                if py == "on":
                    newProject.py = True
                else:
                    newProject.py = False
                if bostG == "on":
                    newProject.bostG = True
                else:
                    newProject.bostG = False            
                newProject.save()
                if img1 is not None:
                    ProjectPhoto.objects.create(project = newProject, img1 = img1, img2 = img2 , img3 = img3)
                else:
                    ProjectPhoto.objects.create(project = newProject)
                messages.success(request, 'Project added successfully')

            context = {
                'social': SocialLinks.objects.all(),
                'blog':Plog.objects.all(),
            }
            return render(request, 'pages/add-project.html', context)
        else:
            return redirect('home')
    else:
        return redirect('home')





# authentication
@csrf_exempt
@unauthenticated_user
def userLogin(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request,username = username, password = password)
        if user is not None:
            login(request,user)
            messages.success(request, "Login successfully")
            return redirect('home')
        else:
            messages.error(request, "Username or Password incorrect")
            return redirect('login')
    else:
        return render(request, 'pages/login.html')

@csrf_exempt
@unauthenticated_user
def register(request):
    form = CreateUserForm()
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            group = Group.objects.get(name = 'users')
            user.groups.add(group)
            Profile.objects.create(
                user = user,
                name_f = request.POST.get('first_name'),
                name_l = request.POST.get('last_name'),
                email = request.POST.get('email')
            )
            # username = form.cleaned_data.get('username')
            messages.success(request, 'Account created successfully')
            return redirect("login")
        else:
            messages.error(request, 'Account not created')
            
    context = {
        'form':form,
        'users':Profile.objects.all()
    }
        
    return render(request, 'pages/register.html', context)
        
def userLogout(request):
    logout(request)
    messages.error(request, "Logout successfully")
    return redirect('home')