from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.core.paginator import Paginator
import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from .models import User, Post, Like, Follow

# Main page
def index(request):
    # Get all posts and order them by the latest
    allPosts = Post.objects.all().order_by('-id')
    
    # Paginate the posts (10 per page)
    paginator = Paginator(allPosts, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    allLikes = Like.objects.all()
    # Initialize the list of posts the current user has liked
    whoYouLiked = []
    # Check if the current user has liked any of the posts
    try:
        for like in allLikes:
            if like.user.id == request.user.id:
                whoYouLiked.append(like.post.id)
    except:
        whoYouLiked = []

    return render(request, "network/index.html", {
        "allPosts": allPosts,
        "page_obj": page_obj,
        "whoYouLiked": whoYouLiked,
    })

# Profile
def profile(request, user_id):
    user = User.objects.get(pk=user_id)
    allPosts = Post.objects.filter(user=user).order_by('-id')

    following = Follow.objects.filter(follower=user)
    followers = Follow.objects.filter(following=user)

    try: 
        checkFollow = followers.filter(follower=User.objects.get(pk=request.user.id))
        if len(checkFollow) != 0:
            isFollowing = True
        else:
            isFollowing = False
    except:
        isFollowing = False

    paginator = Paginator(allPosts, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, "network/profile.html", {
        "allPosts": allPosts,
        "page_obj": page_obj,
        "username": user.username,
        "following": following,
        "followers": followers,
        "isFollowing": isFollowing,
        "userProfile": user,
    })
@csrf_exempt
def like(request):
    if request.method == "POST":
        post_id = request.POST.get('id')
        is_liked = request.POST.get('is_liked')
        try:
            post = Post.objects.get(id=post_id)
            if is_liked == 'false':
                post.likes.add(request.user)
                is_liked = 'true'
            elif is_liked == 'true':
                post.likes.remove(request.user)
                is_liked = 'false'
            post.save()

            return JsonResponse({'like_count': post.likes.count(), 'is_liked': is_liked, "status": 201})
        except:
            return JsonResponse({'error': "Post not found", "status": 404})
    return JsonResponse({}, status=400)

# Following
def following(request):
    curuser = User.objects.get(pk=request.user.id)
    followingSomeone = Follow.objects.filter(follower=curuser)
    allPosts = Post.objects.all().order_by('-id')
    followingPosts = []

    for post in allPosts:
        for person in followingSomeone:
            if person.following == post.user:
                followingPosts.append(post)

    paginator = Paginator(followingPosts, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, "network/following.html", {
        "page_obj": page_obj,
    })

def follow(request): 
    userfollow = request.POST['userfollow']
    curuser = User.objects.get(pk=request.user.id)
    followData = User.objects.get(username=userfollow)
    if not Follow.objects.filter(follower=curuser, following=followData).exists():
      fu = Follow(follower=curuser, following=followData)
      fu.save()
    return HttpResponseRedirect(reverse("profile", kwargs={'user_id': followData.id}))

def unfollow(request):
    userfollow = request.POST['userfollow']
    curuser = User.objects.get(pk=request.user.id)
    followData = User.objects.get(username=userfollow)
    try:
      fu = Follow.objects.get(follower=curuser, following=followData)
      fu.delete()
    except Follow.DoesNotExist:
      pass
    return HttpResponseRedirect(reverse("profile", kwargs={'user_id': followData.id}))

# Edit Post
def new(request):
    if request.method == "POST":
      content = request.POST['content']
      user = User.objects.get(pk=request.user.id)
      post = Post(user=user, content=content)
      post.save()
      return HttpResponseRedirect(reverse("index"))
    
def edit(request, post_id):
    if request.method == "POST":
      data = json.loads(request.body)
      editPost = Post.objects.get(pk=post_id)
      editPost.content = data['content']
      editPost.save()
      return JsonResponse({"message": "Success", "data": data['content']})
    
# Login and Logout
def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "network/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "network/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))

# Register new user
def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "network/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "network/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "network/register.html")
