"""
URL configuration for study_app project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings

from study.views import index, Flashcard, InputText, load, NameFlashcards, card, summary_options, summary_voice, \
    summary_notes, summary_finalize, flashcards_generate, assignment_grading, hcid, create_account, sign_in, welcome, \
    info, info2, generate_summary_info, assignment_grading_info, saveDeck, leaveDeck, InputVoice, inputFile, \
    delete_flashcard, toggle_favourite
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', index, name='index'),
    path('', index, name='index'),

    path('flashcards/', Flashcard, name='flashcard'),
    path('flashcards/text/', InputText, name='InputText'),
    path('load/', load, name='load'),
    path('nameFlashcards/', NameFlashcards, name='NameFlashcards'),
    path('card/', card, name='card'),
    path('saveDeck/', saveDeck, name='saveDeck'),
    path('leaveDeck/', leaveDeck, name='leaveDeck'),
    path('InputVoice/', InputVoice, name='InputVoice'),
    path('inputFile/', inputFile, name='inputFile'),
    path("flashcard/<int:card_id>/toggle-favourite/", toggle_favourite, name="toggle_favourite"),
    path("flashcard/<int:card_id>/delete/", delete_flashcard, name="delete_flashcard"),

    path('summary-options/', summary_options, name='summary_options'),
    path('summary/voice/', summary_voice, name='summary_voice'),
    path('summary/notes/', summary_notes, name='summary_notes'),
    path('summary/finalize/', summary_finalize, name='summary_finalize'),
    path('flashcards/generate/', flashcards_generate, name='flashcards_generate'),
    path('assignment_grading/', assignment_grading, name='assignment_grading'),
    path("hcid/", hcid, name='hcid'),

    path('create_account/', create_account, name='create_account'),
    path("sign_in/", sign_in, name='sign_in'),
    path('welcome/', welcome, name='welcome'),
    path('info/', info, name='info'),
    path("info2/", info2, name='info2'),
    path("generate_summary_info/", generate_summary_info, name='generate_summary_info'),
    path("assignment_grading_info", assignment_grading_info, name='assignment_grading_info'),

]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
