from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .models import User, Category, Listing, Comment, Bid

def listing(request, id):
  listingData = Listing.objects.get(pk=id)
  watchlist = request.user in listingData.watchlist.all()
  comments = Comment.objects.filter(listing=listingData)
  isOwner = request.user.username == listingData.owner.username
  return render(request, "auctions/listing.html", {
    "listing": listingData,
    "watchlist": watchlist,
    "comments": comments,
    "isOwner": isOwner,
  })

def closeAuction(request, id):
  listingData = Listing.objects.get(pk=id)
  listingData.isActive = False
  listingData.save()
  comments = Comment.objects.filter(listing=listingData)
  isOwner = request.user.username == listingData.owner.username
  return render(request, "auctions/listing.html", {
    "listing": listingData,
    "watchlist": watchlist,
    "comments": comments,
    "isOwner": isOwner,
    "update": True,
    "message": "Congratulations! Auction Closed",
  })

def addComment(request, id):
  if request.method == "POST":
    comment = request.POST['comment']
    currentUser = request.user
    listingData = Listing.objects.get(pk=id)
    comment = Comment(
        author=currentUser,
        comment=comment,
        listing=listingData,
        )

    comment.save()
    return HttpResponseRedirect(reverse("listing", args=(id,)))

def remove_watchlist(request, id):
    listingData = Listing.objects.get(pk=id)
    currentUser = request.user
    listingData.watchlist.remove(currentUser)
    return HttpResponseRedirect(reverse("listing", args=(id,)))

def add_watchlist(request, id):
    listingData = Listing.objects.get(pk=id)
    currentUser = request.user
    listingData.watchlist.add(currentUser)
    return HttpResponseRedirect(reverse("listing", args=(id,)))

def watchlist(request):
    currentUser = request.user
    listings = currentUser.watchlist.all()
    return render(request, "auctions/watchlist.html", {
        "listings": listings,
    })


def index(request):
    activeListings = Listing.objects.filter(isActive=True)
    allCategoties = Category.objects.all()
    return render(request, "auctions/index.html", {
        "listings": activeListings,
        "categories": allCategoties,
    })

def displayCategory(request):
    if request.method == "POST":
      categoryFromForm = request.POST['category']
      category = Category.objects.get(categoryName=categoryFromForm)
      activeListings = Listing.objects.filter(isActive=True, category=category)
      allCategoties = Category.objects.all()
      return render(request, "auctions/index.html", {
          "listings": activeListings,
          "categories": allCategoties,
      })


def createListing(request):
    if request.method == "GET":
      allCategoties = Category.objects.all()
      return render(request, "auctions/create.html", {
        "categories": allCategoties,
      })
    else:
        # get data from form
        title = request.POST['title']
        description = request.POST['description']
        price = request.POST['price']
        image = request.POST['imageUrl']
        category = request.POST['category']
        # username
        currentUser = request.user
        # get category
        categoryData = Category.objects.get(categoryName=category)
        # craeate bid
        newBid = Bid(bid=int(price), user=currentUser)
        newBid.save()
        # create new listing
        newListing = Listing(
            title=title,
            description=description,
            price=newBid,
            imageUrl=image,
            category=categoryData,
            owner=currentUser,
            )
        # insert data into database
        newListing.save()
        # redirect to index
        return HttpResponseRedirect(reverse("index"))

def addBid(request, id):
    if request.method == "POST":
        newBid = request.POST['newBid']
        listingData = Listing.objects.get(pk=id)
        watchlist = request.user in listingData.watchlist.all()
        comments = Comment.objects.filter(listing=listingData)
        isOwner = request.user.username == listingData.owner.username
        if int(newBid) > listingData.price.bid:
            updateBid = Bid(user=request.user, bid=int(newBid))
            updateBid.save()
            listingData.price = updateBid
            listingData.save()
            return render(request, "auctions/listing.html", {
                "listing": listingData,
                "message": "Success",
                "update": True,
                "watchlist": watchlist,
                "comments": comments,
                "isOwner": isOwner,
            })
        else:
             return render(request, "auctions/listing.html", {
                "listing": listingData,
                "message": "Failed",
                "update": False,
                "watchlist": watchlist,
                "comments": comments,
                "isOwner": isOwner,
            })

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
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auctions/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")
