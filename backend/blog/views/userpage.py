from django.shortcuts import render


def userpage(request):
    user = {
        "username": "Lavinchi",
        "name": "Kostya",
        "surname": "Kad",
        "email": "sometestmail@test.com",
        "birthday": "01.01.1990",
        "status": "admin",
        "blogs": [
            {
                "title": "Python blog"
            },
            {
                "title": "Scala blog"
            },
            {
                "title": "Roblox blog"
            }
        ]
    }
    context = {
        "user": user
    }
    return render(request, 'blog/userpage.html', context)
