from django.shortcuts import render

def profile(request):
    """
    Display users profile.
    """

    context = {

    }
    return render(request, 'profiles/profile.html', context)
