Проект для тестирования промптов. Входной файл: input.txt, выходной лежит в папке output.

Начало работы:
0) git clone <ссылка на репозиторий>
1) Создаем виртуальное окружение в папке проекта: python3.11 -m venv venv
2) Активируем виртуальное окружение: venv\Scripts\Activate.ps1
3) Устанавливаем зависимости: pip install -r requirements.txt
4) Запускаем код: python3.11 main.py

Для изменения промпта необходимо через текстовый редактор(не через гит) менять sys_prompt в файле summarizer