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
            # Verificar si la palabra ya existe en el archivo .txt
            try:
                file_path = 'db.txt'  # Ruta del archivo .txt
                # Leer las palabras ya guardadas
                with open(file_path, 'r') as file:
                    words = file.read().splitlines()
                
                if word in words:
                    return render(request, 'game.html', {
                        'success': False,
                        'message': "La palabra ya se la enseñaron previamente."
                    })
                
                # Guardar la nueva palabra
                with open(file_path, 'a') as file:
                    file.write(f"{word}\n")

                return redirect('simulate', word=word)

            except FileNotFoundError:
                # Si el archivo no existe, crearlo y guardar la palabra
                with open(file_path, 'w') as file:
                    file.write(f"{word}\n")
                return redirect('simulate', word=word)

        else:
            return render(request, 'game.html', {
                'success': False,
                'message': "La palabra no cumple con las reglas."
            })
    return redirect('index')


def monkey_learn(request, word):
    word=word
    learned_word, p_attempts = simulate_monkey_learning(word)
    return render(request, 'simulate.html', {
        'word': word,
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




#CODIGO PARA USAR SQLITE

# def submit_word(request):
#     if request.method == 'POST':
#         word = request.POST.get('word')
#         if len(word) >= 0 and len(word) <= 100 and word.isalpha():
#             word = word.lower()
#             # Verificar si la palabra ya existe
#             try:

#                 created = Word.objects.get_or_create(word=word)
#                 if created:
#                     return redirect('simulate', word=word)
#                 else:
#                     return render(request, 'game.html', {
#                         'success': False,
#                         'message': "La palabra ya se la enseñaron previamente."
#                     })
#             except IntegrityError:
#                 return render(request, 'game.html', {
#                     'success': False,
#                     'message': "Ocurrió un error al guardar la palabra."
#                 })
#         else:
#             return render(request, 'game.html', {
#                 'success': False,
#                 'message': "La palabra no cumple con las reglas."
#             })
#     return redirect('index')