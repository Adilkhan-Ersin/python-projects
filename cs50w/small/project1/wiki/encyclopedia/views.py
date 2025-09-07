from django.shortcuts import render
from markdown2 import Markdown
import random
from . import util

def convert_markdown_to_html(title):
    content = util.get_entry(title)
    markdowner = Markdown()
    if content == None:
        return None
    else:
        return markdowner.convert(content)

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def entry(request, title):
    html_content = convert_markdown_to_html(title)
    if html_content == None:
        return render(request, "encyclopedia/error.html", {
            "message": "Page does not exist"
        })
    else:
        return render(request, "encyclopedia/entry.html", {
            "title": title,
            "content": html_content
        })

def search(request):
    if request.method == "POST":
        query = request.POST.get("q")
        entries = convert_markdown_to_html(query)
        if entries is not None:
            return render(request, "encyclopedia/entry.html", {
                "title": query,
                "content": entries
            })
        else:
            allEntries = util.list_entries()
            recommendation = []
            for entry in allEntries:
                if query.lower() in entry.lower():
                    recommendation.append(entry)
            return render(request, "encyclopedia/search.html", {
                "recommendation": recommendation
            })

def new(request):
    if request.method == "GET":
        return render(request, "encyclopedia/new.html")
    else:
        title = request.POST['title']
        content = request.POST['content']
        titleExists = util.get_entry(title)
        if titleExists is not None:
            return render(request, "encyclopedia/error.html", {
                "message": "Page already exists"
            })
        else:
            util.save_entry(title, content)
            html_content = convert_markdown_to_html(title)
            return render(request, "encyclopedia/entry.html", {
                "title": title,
                "content": html_content
            })

def edit(request):
    if request.method == 'POST':
        title = request.POST['entry_title']
        content = util.get_entry(title)
        return render(request, "encyclopedia/edit.html", {
            "title": title,
            "content": content
        })

def save_edit(request):
    if request.method == 'POST':
        title = request.POST['title']
        content = request.POST['content']
        util.save_entry(title, content)
        html_content = convert_markdown_to_html(title)
        return render(request, "encyclopedia/entry.html", {
            "title": title,
            "content": html_content
        })

def rand(request):
    entries = util.list_entries()
    randomEntry = random.choice(entries)
    html_content = convert_markdown_to_html(randomEntry)
    return render(request, "encyclopedia/entry.html", {
        "title": randomEntry,
        "content": html_content
    })
