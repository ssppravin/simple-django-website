from django.shortcuts import render


def profileView(request, userName):
    return render(request, 'Profile.html', {
        'name': userName,
    })