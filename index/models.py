from django.db  import models
import time

class Word(models.Model):
    word = models.CharField(max_length=15, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.word

import random

def simulate_monkey_learning(word):
    monkey_word = ['_'] * len(word)  # Palabra inicial con espacios vacíos
    attempts = 0

    print("El mono está intentando aprender la palabra...\n")

    while ''.join(monkey_word) != word:
        for i, char in enumerate(word):
            if monkey_word[i] == '_':  # Si la posición no está resuelta
                random_letter = random.choice('abcdefghijklmnñopqrstuvwxyzABCDEFGHIJKLMNÑOPQRSTUVWXYZ')
                attempts += 1
                if random_letter == char:  # Coincidencia
                    monkey_word[i] = char
                    break  # Ir a la siguiente letra
    return ''.join(monkey_word), attempts