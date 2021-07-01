# YaTest


### Сценарий поиск в яндексе
Для начала тестирования поиска в яндексе запустите python файл SearchTest.py  
Чтобы получить отчет о тестировании в формате HTML нужно:  
1.  Установить библиотеру pytest_html, выполнив следующую команду в теримнале: pip install pytest_html
2.  В терминале ввести команду:  
  pytest --html=report.html --self-contained-html *SearchTest.py*  
4.  Открыть созданный файл отчета - retort.html


### Сценарий картинки на яндексе
Для начала тестирования поиска в яндексе запустите python файл PictureTest.py  
Чтобы получить отчет о тестировании в формате HTML нужно:  
1.  Установить библиотеру pytest_html, выполнив следующую команду в теримнале: pip install pytest_html
2.  В терминале ввести команду:  
  pytest --html=report.html --self-contained-html *SearchTest.py*  
4.  Открыть созданный файл отчета - retort.html


### Page Object Pattern  
Релизация паттерна выполненна в отдельной директории. Для выполнения тестов, запустите файлы TestYaSearch.py *(Сценарий поиска в яндекс)* и TestYaPic.py *(Сценарий картинки на яндексе)*

### Поддержка браузеров
Поддерживается браузер Google Chrome 91, для работы с ним используется chromedriver

**Chromedriver расположен в корневой папке проекта**  
**Chromedriver установлен для версии Google Chrome 91, для других версий загрузите [драйвер](https://chromedriver.chromium.org/downloads) с поддержкой вашей версии Google Chrome**
