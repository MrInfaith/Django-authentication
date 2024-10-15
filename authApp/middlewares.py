from django.shortcuts import redirect 

# *********** Autheticated prevent directly go to home *********

def auth(view_function):
    def wrapped_view(request,*args,**kwargs):
        if request.user.is_authenticated==False:
            return redirect('login')
        return view_function(request,*args,**kwargs)
    return wrapped_view


# ********** prevent directly go to login from home ***********

def guest(view_function):
    def wrapped_view(request,*args,**kwargs):
        if request.user.is_authenticated:
            return redirect('home')
        return view_function(request,*args,**kwargs)
    return wrapped_view