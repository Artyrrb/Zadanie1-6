def delnumb(text):
    textrez=('')
    for a in text:
        if a not in ('0','1','2','3','4','5','6','7','8','9'):
            textrez=textrez+a
    return textrez


print('Введите текст, из текста будут удалены цифры:')
a=delnumb(str(input()))
print ('Текст без цифр:',a)
