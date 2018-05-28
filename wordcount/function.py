# from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return render(request, 'home.html')


def count(request):
    user_text = request.GET['text']
    total_count = len(user_text)

    word_dict = {}
    count_word = 0

    for c in user_text:
        if c not in word_dict:
            word_dict[c] = 1
        else:
            word_dict[c] += 1
        if c.isalnum():
            count_word += 1

    count_punctuation = total_count - count_word

    max_word = max(word_dict, key=lambda x: word_dict[x])
    max_value = max(word_dict, key=word_dict.get)
    max_word_value = max(word_dict.items(), key=lambda x:x[1])
    sorted_dict = sorted(word_dict.items(), key=lambda x:x[1], reverse=True)

    return render(request, 'count.html', {'total_count': total_count,
                                          'user_text': user_text,
                                          'word_dict': word_dict,
                                          'max_word_value': max_word_value,
                                          'sorted_dict': sorted_dict,
                                          'count_word': count_word,
                                          'count_punctuation': count_punctuation
                                          })


def about(request):
    return render(request, 'about.html')