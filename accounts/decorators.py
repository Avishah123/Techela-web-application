from django.http import HttpResponse
from django.shortcuts import redirect
from .models import *


def head_required(view_func):
    def wrapper_func(request, *args, **kwargs):
        user = request.user
        if user.is_head:
            return view_func(request, *args, **kwargs)
        else:
            return redirect('warning')
    return wrapper_func
