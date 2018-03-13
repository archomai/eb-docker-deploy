from django.contrib.auth import get_user_model
from django.shortcuts import render, get_object_or_404

User = get_user_model()


def index(request):
    # 모든 유저의 username, img_profile, nickname을 리스트(ul > li)로 보여주는 뷰 생성
    # 이 뷰에는 새 css를 적용 (Bootstrap, static/bootstap/csss/bootstrap.css)를 템플릿에 static 태그로

    users = User.objects.all()

    context = {
        'users': users,
    }

    return render(request, 'index.html', context)
