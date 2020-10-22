import sys

# Получаем слово из первого аргумента командной строки.
word = sys.argv[1]

lenpos = int(len(word)/2)

if len(word)%2 > 0:
 print(word[lenpos])
else:
 print(word[lenpos-1])