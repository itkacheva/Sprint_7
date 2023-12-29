
<h1 align="center"><a>Описание тестовых методов для проверки API учебного сервиса «Яндекс.Самокат»</a></h1>

## <p style="color:#9595c9">Установка проекта</p>
1. <b>Клонируйте репозиторий на ваш локальный компьютер:</b>
   <p>git clone https://github.com/itkacheva/Sprint_7.git</p>
2. <b>Перейдите в каталог проекта:</b>
   <p>cd название_репозитория</p>
3. <b>Установите необходимые зависимости:</b>
   <p>pip install -r requirements.txt</p>
## <p style="color:#9595c9">Запуск</p>
Запуск тестов осуществляется с помощью команды <b> pytest</b>
## <p style="color:#9595c9">Пример использования</p>
<pytest tests\test_courier_creat.py
## <p style="color:#9595c9">Реализованные тесты</p>
<p><b style="color:green"> test_courier_creat.py</b> - содержит тесты на ручку «Создать курьера».</p>
<p><b style="color:green">test_courier_login.py</b> - содержит тесты на ручку «Логин курьера».</p>
<p><b style="color:green">test_order_create.py</b> - содержит тесты на ручку «Создать заказ»</p>
<p><b style="color:green">test_order_list.py</b> - содержит на ручку, которая получает список заказов</p>