from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.core.files.storage import FileSystemStorage
from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render

from study.form import FlashcardSetForm
from study.models import flashcardSet, flashcard


# Create your views here.
def index(request):
    return render(request, 'index.html')


@csrf_exempt  # if you're not sending CSRF in fetch, but better to use token
def delete_flashcard(request, card_id):
    if request.method == "POST":
        card = get_object_or_404(flashcard, id=card_id)
        card.delete()
        return JsonResponse({"deleted": True})
    return JsonResponse({"deleted": False}, status=400)


def index(request):
    return render(request, 'index.html')


def InputText(request):
    return render(request, 'InputText.html')


def inputFile(request):
    return render(request, 'inputFile.html')


def load(request):
    return render(request, 'load.html')


def NameFlashcards(request):
    if request.method == "POST":
        form = FlashcardSetForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('card')  # or wherever you want after saving
    else:
        form = FlashcardSetForm()
    return render(request, 'NameFlashcards.html', {'form': form})


def card(request):
    cards = flashcard.objects.all()
    context = {'cards': cards}
    return render(request, 'card.html', context)


def saveDeck(request):
    return render(request, "SaveTheDeck.html")


def leaveDeck(request):
    return render(request, "LeaveTheDeck.html")


def InputVoice(request):
    return render(request, "InputVoice.html")


def toggle_favourite(request, card_id):
    if request.method == "POST":  # only allow POST
        card = get_object_or_404(flashcard, id=card_id)
        card.favourite = not card.favourite
        card.save()
        return JsonResponse({"favourite": card.favourite})


def Flashcard(request):
    flashcards = flashcardSet.objects.all()
    context = {"flashcards": flashcards}
    return render(request,
                  'flashcard.html', context)


def summary_options(request):
    return render(request, 'summary_options.html')


def summary_voice(request):
    return render(request, 'summary_voice.html')  # create later


def summary_notes(request):
    if request.method == 'POST' and request.FILES.get('notes_file'):
        uploaded_file = request.FILES['notes_file']
        fs = FileSystemStorage()
        filename = fs.save(uploaded_file.name, uploaded_file)
        file_url = fs.url(filename)
        # You can process the file here or pass it to the next page
        return redirect('summary_finalize')  # redirect after upload
    return render(request, 'summary_notes.html')


def summary_finalize(request):
    return render(request, 'summary_finalize.html')


def flashcards_generate(request):
    return render(request, 'flashcards_generate.html')


def assignment_grading(request):
    # Example: fetch assignments from the database
    assignments = [
        {"title": "Math Homework", "student": "Ali", "score": 85},
        {"title": "Science Project", "student": "Ayşe", "score": 92},
        {"title": "History Essay", "student": "Mehmet", "score": None},  # not graded yet
    ]

    context = {
        "assignments": assignments
    }

    return render(request, "assignment_grading.html", context)


def hcid(request):
    return render(request, 'hcid.html')


def create_account(request):
    if request.method == 'POST':
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 != password2:
            return render(request, 'create_account.html', {'error': 'Passwords do not match.'})

        if User.objects.filter(username=email).exists():
            return render(request, 'create_account.html', {'error': 'Email already registered.'})

        user = User.objects.create_user(username=email, email=email, password=password1)
        user.save()
        login(request, user)
        return redirect('welcome')

    return render(request, 'create_account.html')


def sign_in(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        user = authenticate(request, username=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('welcome')
        else:
            return render(request, 'sign_in.html', {'error': 'Invalid credentials.'})

    return render(request, 'sign_in.html')


def welcome(request):
    return render(request, 'welcome.html')


def info(request):
    return render(request, 'info.html')


def info2(request):
    return render(request, 'info2.html')


def generate_summary_info(request):
    return render(request, 'generate_summary_info.html')


def assignment_grading_info(request):
    return render(request, 'assignment_grading_info.html')
