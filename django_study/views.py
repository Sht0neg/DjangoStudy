from django.shortcuts import redirect

def index_redirect(req):
    return redirect("/products/")