# hands-service
📝 Модуль, загружает контент с web-страницы, находит в тексте номера телефонов и записывает их в файл.

# Подготовка к работе

Необходимо выполнить команду
```bash
git clone https://github.com/1kitten/hands-service.git
```
Данная команда скопирует текующий репозиторий с проектом на ваш локальный компьютер

Далее необходимо заполнить файл <code> urls.txt </code> url адресами, где необходимо произвести поиск номеров телефона
(для примера файл уже заполнен стандартным набором url адресов)

Последним шагом является запуск программы, для этого выполните следующую команду<br>
<b>MacOS, Linux</b>:
```python
python phone_numbers.py
```
<b>Windows</b>:
```python
python .\phone_numbers.py
```

После выполнения скрипта, данные будут записаны в файл <code>founded_numbers.txt</code>
