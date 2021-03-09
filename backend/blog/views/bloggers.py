__all__ = ['bloggers']


from django.shortcuts import render


def bloggers(request):
    bloggers = [
        {
            "name": "Lavinchi",
            "bio": "some idiot who tryes to create content. Join!",
            "followers": 999,
            "link": "lavinchi's link",
        },
        {
            "name": "roblox",
            "bio": "Lorem ipsum dolor sit, amet consectetur adipisicing elit. Libero, sed eos veniam, consequuntur inventore laboriosam molestiae porro officia nemo atque ea vitae rerum? Perferendis aliquam animi doloribus magnam illum quaerat.",
            "followers": 1000,
            "link": "roblox link",
        },
        {
            "name": "rusakk",
            "bio": "Mary, marry me!",
            "followers": 9999,
            "link": "rusakk link",
        },
        {
            "name": "kirill san",
            "bio": "Lorem ipsum dolor sit amet consectetur adipisicing elit. Doloremque a odit eligendi ea, perspiciatis alias voluptas fugit sequi cupiditate, corrupti autem repudiandae odio minus fugiat nihil dolore praesentium dicta eos.",
            "followers": 1,
            "link": "kirill link",
        },
        {
            "name": "sasher1990",
            "bio": "PLAYING ONLY SETT",
            "followers": 70,
            "link": "sasha link"
        }
    ]
    context = {
        "bloggers": bloggers
    }
    return render(request, 'blog/bloggers.html', context)
