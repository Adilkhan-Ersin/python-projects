from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.db.models import Sum
import json
import random
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from .models import User, Post, Transaction
# Create your views here.
def index(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("403"))
    # Calculate total income and expense
    total_income = Transaction.objects.filter(transaction_type='IN').aggregate(total_income=Sum('amount'))
    total_expense = Transaction.objects.filter(transaction_type='EX').aggregate(total_expense=Sum('amount'))
    
    if total_income['total_income'] is None:
        total_income['total_income'] = 0
    if total_expense['total_expense'] is None:
        total_expense['total_expense'] = 0

    total_amount = total_income['total_income'] - total_expense['total_expense']

    # Fetch all goals submitted by the current user
    all_goals = Post.objects.filter(user=request.user).order_by('-id')

    # Prepare a list to hold all goals with their progress
    goals_with_progress = []

    # Iterate over each goal and calculate its progress
    for goal in all_goals:
        goal_name = goal.content
        goal_amount = goal.amount
        current_progress = 0
        
        if goal_amount > 0:
            current_progress = (total_amount / goal_amount) * 100
            current_progress = round(current_progress)
            if current_progress > 100:
                current_progress = 100
        else:
            current_progress = 0

        if goal.color:
            goal_color = goal.color
        else:
            colors = ['#ffbe0b', '#fb5607', '#ff006e', '#8338ec', '#3a86ff', '#00b09b', '#ff006e', '#8338ec', '#3a86ff', '#00b09b']
            goal_color = random.choice(colors)

        # Add the goal along with its progress to the list
        goals_with_progress.append({
            'goal_name': goal_name,
            'goal_amount': goal_amount,
            'current_progress': current_progress,
            'color': goal_color,
            'goal_id': goal.id
        })

    context = {
        'total_amount': total_amount,
        'goals': all_goals,
        'total_income': total_income['total_income'],
        'total_expense': total_expense['total_expense'],
        'goals_with_progress': goals_with_progress,  # Pass the list of goals with progress
    }

    return render(request, 'dashboard/index.html', context)

@login_required
def submit_goal(request):
   if request.method == "POST":
     goal_name = request.POST['goal_name']
     goal_amount = request.POST['goal_amount']
     
     colors = ['#ffbe0b', '#fb5607', '#ff006e', '#8338ec', '#3a86ff', '#00b09b', '#ff006e', '#8338ec', '#3a86ff', '#00b09b']
     goal_color = random.choice(colors)

     goal = Post(user=request.user, content=goal_name, amount=goal_amount, color=goal_color)
     goal.save()
     return HttpResponseRedirect(reverse("index"))
   
@login_required
def edit_goal(request, post_id):
  if request.method == "POST":
    data = json.loads(request.body)

    try:
      editPost = Post.objects.get(pk=post_id, user=request.user)
    except Post.DoesNotExist:
      return JsonResponse({"message": "Post not found"}, status=404)
    
    editPost.content = data.get('content', editPost.content)
    editPost.amount = data.get('goal_amount', editPost.amount)
    editPost.save()
    return JsonResponse({"message": "Success", "data": {"content": editPost.content, "goal_amount": editPost.amount}})
  
@login_required
def delete_goal(request, post_id):
  if request.method == "POST":
    try:
       goal_delete = Post.objects.get(pk=post_id, user=request.user)
    except Post.DoesNotExist:
       return JsonResponse({"message": "Post not found"})
    
    goal_delete.delete()
    return JsonResponse({"message": "Success"})

@login_required
def submit_transaction(request):
   if request.method == "POST":
     income = request.POST['income']
     expense = request.POST['expense']
     description = request.POST['description']

     if income:
        Transaction.objects.create(
            user=request.user,
            amount=income,
            transaction_type='IN',
            description=description
        )

     if expense:
        Transaction.objects.create(
            user=request.user,
            amount=expense,
            transaction_type='EX',
            description=description
        )
     return HttpResponseRedirect(reverse("index"))
def charts(request):
  if not request.user.is_authenticated:
     return HttpResponseRedirect(reverse("403"))
  return render(request, 'dashboard/charts.html',)

@login_required
def charts_data(request):
  transactions = Transaction.objects.filter(user=request.user)
  
  # Line chart data
  income_data = transactions.filter(transaction_type='IN').values_list('date', 'amount')
  expense_data = transactions.filter(transaction_type='EX').values_list('date', 'amount')

  # Pie chart data
  total_income = transactions.filter(transaction_type='IN').aggregate(total_income=Sum('amount'))
  total_expense = transactions.filter(transaction_type='EX').aggregate(total_expense=Sum('amount'))
  
  data = {
    'line_chart': {
      'income_data': list(income_data),
      'expense_data': list(expense_data),
    },
    'pie_chart': {
      'total_income': total_income['total_income'],
      'total_expense': total_expense['total_expense'],
    },
  }
  return JsonResponse(data)
def tables(request):
  if not request.user.is_authenticated:
    return HttpResponseRedirect(reverse("403"))
  
  # Get all transactions for the logged-in user 
  transactions = Transaction.objects.filter(user=request.user)
    
  # Calculate total income, total expense, and total balance
  total_income = sum(t.amount for t in transactions if t.transaction_type == Transaction.INCOME)
  total_expense = sum(t.amount for t in transactions if t.transaction_type == Transaction.EXPENSE)
  total_balance = total_income - total_expense

  context = {
    'transactions': transactions,
    'total_income': total_income,
    'total_expense': total_expense,
    'total_balance': total_balance
  }

  return render(request, 'dashboard/tables.html', context)

def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        email = request.POST.get("email")
        password = request.POST.get("password")

        if not email or not password:
            return render(request, "dashboard/login.html", {
                "message": "Both fields are required."
            })
        # Find the user by email
        try:
            user_obj = User.objects.get(email=email)
        except User.DoesNotExist:
            return render(request, "dashboard/login.html", {
                "message": "Invalid email and/or password."
            })

        user = authenticate(request, username=user_obj.username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "dashboard/login.html", {
                "message": "Invalid email and/or password."
            })
    else:
        return render(request, "dashboard/login.html")
    

def register_view(request):
    if request.method == "POST":
        firstName = request.POST.get("firstName")
        lastName = request.POST.get("lastName")
        username = firstName + " " + lastName
        email = request.POST.get("email")

        # Ensure password matches confirmation
        password = request.POST.get("password")
        confirmation = request.POST.get("confirmation")
        if password != confirmation:
            return render(request, "dashboard/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "dashboard/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "dashboard/register.html")
    
def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))

def forgot_view(request):
    return render(request, "dashboard/forgot-password.html")

def not_found(request):
    return render(request, "dashboard/404.html")

def error(request):
    return render(request, "dashboard/403.html")