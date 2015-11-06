from django.shortcuts import render_to_response,HttpResponseRedirect,HttpResponse
from models import Book,Author
from forms import Sys,newBook,newAuthor,newBook2
# Create your views here.
def home(request):
    book_list = Book.objects.all()
    if request.method == "POST":
        if (request.POST.get("books")):
            return HttpResponseRedirect("/update/?ISBN=%s"%request.POST.\
            get("books"))
        for book in book_list:
            if(request.POST.has_key((str)(book.ISBN))):
                 Book.objects.get(ISBN = book.ISBN).delete()
                 book_list = Book.objects.all()
                 break
             

#    book_list = []
#    for book in book_all:
#        book_list.append(book.Title)
        
    if request.method == "GET" and request.GET:
        form = Sys(request.GET)
        if form.is_valid():
            cd = form.cleaned_data
            author_q = cd['query']
            try:
                author = Author.objects.get(Name = author_q)
            except:
                return HttpResponse("The author %s doesn't exist"%author_q)
            author_ID = author
            query_result = Book.objects.filter(AuthorID = author_ID)
            query_result2 = []
            for item in query_result:
                query_result2.append(item.Title)
            request.session['query_result'] = query_result2
            request.session['author'] = author.Name
            return HttpResponseRedirect("/query_result/")     
    else:
        form = Sys()
    return render_to_response("home.html",{"form":form,"book_list":book_list})
def show_query_result(request):
    return render_to_response("query_result.html",{'author':request.\
    session['author'],'query_result':request.session['query_result']})
def show_details(request):
    book_ISBN = request.GET.get("ISBN")
    book = Book.objects.get(ISBN = book_ISBN)
    author = book.AuthorID
    return render_to_response("show_details.html",locals())
def add_book(request):
    if request.method =="POST":
        form = newBook(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            try:
                author =  Author.objects.get(Name = cd["Author"])
            except:
                request.session["ISBN"] = cd["ISBN"]
                request.session["Title"] = cd["Title"]
                request.session["Publisher"] = cd["Publisher"]
                request.session["PublishDate"] = (str)(cd["PublishDate"])
                request.session["Price"] = (str)(cd["Price"])
                return HttpResponseRedirect("/add_author/?author=%s"%cd["Author"])  
            b = Book(ISBN = cd["ISBN"],
                     Title = cd["Title"],
                     AuthorID = author,
                     Publisher = cd["Publisher"],
                     PublishDate = cd["PublishDate"],
                     Price = cd["Price"]
                     )
            b.save()
            return HttpResponseRedirect("/success/")
    else:
        form = newBook()
    return render_to_response("add_book.html",{"form":form})
def add_author(request):
    if request.method =="POST":
        form = newAuthor(request.POST)
        if form.is_valid():
            cd = form.cleaned_data 
            a = Author(ID = cd["ID"],
                     Name = cd["Name"],
                     Age = cd["Age"],
                     Country = cd["Country"]
                     )
            a.save()
            b = Book(ISBN = request.session["ISBN"],
                     Title = request.session["Title"],
                     AuthorID = a,
                     Publisher = request.session["Publisher"],
                     PublishDate = request.session["PublishDate"],
                     Price = (float)(request.session["Price"])
                     )
            b.save()
            return HttpResponseRedirect("/success/")
    else:
        form = newAuthor(initial ={'Name':request.GET.get("author")})
    return render_to_response("add_author.html",{"form":form,"author":\
    request.GET.get("author")})
def update(request):
    if request.method == "GET":
        book = Book.objects.get(ISBN = request.GET.get("ISBN"))
        form = newBook2(initial = {"Author":book.AuthorID.Name,"Publisher":\
        book.Publisher,
        "PublishDate":book.PublishDate,"Price":book.Price})
        return render_to_response("update.html",{"form":form})
    else:
        form = newBook2(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            book = Book.objects.get(ISBN= request.GET.get("ISBN"))
            book.Publisher = cd["Publisher"]
            book.PublishDate = cd["PublishDate"]
            book.Price = cd["Price"]
            try:
                author = Author.objects.get(Name = cd["Author"])
            except:
                book.save()
                return HttpResponseRedirect("/add_Author/?ISBN=%s&author=%s"\
                %(book.ISBN,cd["Author"]))
            book.AuthorID = author
            book.save()
            return HttpResponseRedirect("/success/")
        else:
            return render_to_response("update.html",{"form":form})
def success(request):
    return render_to_response("success.html")
def add_Author(request):
    if request.method =="POST":
        form = newAuthor(request.POST)
        if form.is_valid():
            cd = form.cleaned_data 
            a = Author(ID = cd["ID"],
                     Name = cd["Name"],
                     Age = cd["Age"],
                     Country = cd["Country"]
                     )
            a.save()
            b = Book.objects.get(ISBN = request.GET.get("ISBN"))
            b.AuthorID = a
            b.save()
            return HttpResponseRedirect("/success/")
    else:
        form = newAuthor(initial ={'Name':request.GET.get("author")})
    return render_to_response("add_author.html",{"form":form,"author":request.\
    GET.get("author")})