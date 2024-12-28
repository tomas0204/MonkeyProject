from django.shortcuts   import render, redirect
from .models            import Word, simulate_monkey_learning
from django.db          import IntegrityError
from django.shortcuts   import render
from django.http import HttpResponse

def hello(request):
    return render(request, 'index.html', {
        'message': request.GET.get('message')
    })

def rules(request):
    return render(request, "rules.html")

def game(request):
    return render(request, "game.html")

def submit_word(request):
    if request.method == 'POST':
        word = request.POST.get('word')
        if len(word) >= 0 and len(word) <= 100 and word.isalpha():
            word = word.lower()
            # Verificar si la palabra ya existe
            try:
                word_obj, created = Word.objects.get_or_create(word=word)
                if created:
                    return redirect('simulate', word_id=word_obj.id)
                else:
                    return render(request, 'game.html', {
                        'success': False,
                        'message': "La palabra ya se la enseñaron previamente."
                    })
            except IntegrityError:
                return render(request, 'game.html', {
                    'success': False,
                    'message': "Ocurrió un error al guardar la palabra."
                })
        else:
            return render(request, 'game.html', {
                'success': False,
                'message': "La palabra no cumple con las reglas."
            })
    return redirect('index')

def monkey_learn(request, word_id):
    
    word_obj = Word.objects.get(id=word_id)
    learned_word, p_attempts = simulate_monkey_learning(word_obj.word)
    return render(request, 'simulate.html', {
        'word': word_obj.word,
        'learned_word': learned_word,
        'attempts': p_attempts
    })

def get_word(request):
    if request.method == 'POST':
        word = request.POST.get('word')
        if word:
            return HttpResponse(word)  # Devuelve la palabra como respuesta
        else:
            return HttpResponse("No se proporcionó ninguna palabra.", status=400)
    return HttpResponse("Solicitud incorrecta", status=405)  # Si no es un POST


def definition(request, word=get_word):

    return render(request, "definition.html", {
        "word": word
    })

def final(request):
    return render(request, "final.html")