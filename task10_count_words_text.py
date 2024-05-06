# Пользователь вводит текст (строка). Словом считается последовательность непробельных символов идущих подряд.
# Слова разделены одним или большим числом пробелов. Определить сколько различных слов содержится в тексте.

# input: She sells sea shells on the sea shore The shells that she sells are sea shells I'm sure. So if she sells sea shells on the sea shore I'm sure that the shells are sea shore shells

# output: 14

stroka = input().split()
# по скольку нам нужны Уникальные слова, то нам помогут Множества
set_1 = set()
for i in stroka:
    set_1.add(i.lower()) #  добавляем слово в наше множество в Нижнем регистре
print(len(set_1)) # выводим длинну множества