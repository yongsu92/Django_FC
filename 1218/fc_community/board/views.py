from django.shortcuts import render
from .models import Board
# Create your views here.

def board_list(request):
    boards = Board.objects.all().order_by('-pk')
    return render(request,'board/board_list.html',{'boards':boards})