words = ['scala', 'java', 'go', 'python', 'erlang', 'c++', 'haskel', 'rust', 'clojure']
letter = input('Введите букву: ')

def count_letter(words, letter):
    i = 0
    for word in words:
        if letter in word:
            i += 1
    return i
f = count_letter(words, letter)
if f > 0:
  print(f)
else:
  print('Нет такой буквы, вращайте барабан!')