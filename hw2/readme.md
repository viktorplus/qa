# Homework 2 — Selenium + Pytest

Домашнее задание по автоматизированному тестированию веб-интерфейса с использованием **Selenium WebDriver** и **Pytest**.

## Что изучаем

- запуск браузера через Selenium WebDriver;
- поиск элементов на странице;
- клик по ссылкам и кнопкам;
- проверка текста элементов;
- использование `pytest.fixture`;
- открытие и закрытие браузера через фикстуру;
- создание скриншотов;
- управление окном браузера;

# Selenium

`Selenium` — набор инструментов для автоматизации и тестирования веб-приложений.

Основные компоненты:

- **Selenium IDE** — запись и воспроизведение действий в браузере;
- **Selenium WebDriver** — API для управления браузером из кода;

---

# WebDriver

`WebDriver` управляет браузером через специальный драйвер.

Примеры драйверов:

| Браузер | Драйвер |
|---|---|
| Google Chrome | ChromeDriver |
| Mozilla Firefox | GeckoDriver |
| Microsoft Edge | EdgeDriver |
| Safari | SafariDriver |

---

# Установка

Установка Selenium:

```bash
pip install selenium
```

Установка Pytest:

```bash
pip install pytest
```

При необходимости WebDriver Manager:

```bash
pip install webdriver-manager
```

---

# Запуск Chrome

```python
from selenium import webdriver

driver = webdriver.Chrome()
```

Открыть страницу:

```python
driver.get("https://itcareerhub.de/ru")
```

Закрыть браузер:

```python
driver.quit()
```

---

# Pytest fixture для браузера

Фикстура позволяет описать подготовку браузера и его закрытие после теста.

```python
import pytest
from selenium import webdriver


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()

    yield driver

    driver.quit()
```

## Как работает `yield`

Код **до `yield`** выполняется перед тестом:

```python
driver = webdriver.Chrome()
driver.maximize_window()
```

Через:

```python
yield driver
```

объект `driver` передаётся в тест.

Код **после `yield`** выполняется после завершения теста:

```python
driver.quit()
```

---

# Использование фикстуры в тесте

```python
def test_example(driver):
    driver.get("https://itcareerhub.de/ru")
```

Pytest сам найдёт фикстуру с именем `driver` и передаст её в функцию теста.

---

# Поиск элементов

Импорт:

```python
from selenium.webdriver.common.by import By
```

## По тексту ссылки

```python
element = driver.find_element(By.LINK_TEXT, "О нас")
```

## По ID

```python
element = driver.find_element(By.ID, "payment-methods")
```

## По XPath

```python
element = driver.find_element(
    By.XPATH,
    "//*[@id='rec1921734713']/div/div/div[5]/h2"
)
```

---

# Клик по элементу

```python
about_button = driver.find_element(By.LINK_TEXT, "О нас")
about_button.click()
```

Метод `.click()` имитирует нажатие пользователя на кнопку или ссылку.

---

# Проверка текста

Получить текст элемента:

```python
about_company = driver.find_element(By.LINK_TEXT, "О компании")
print(about_company.text)
```

Проверка через `assert`:

```python
assert about_company.text == "О компании"
```

---

# Скриншоты

## Скриншот отдельного элемента

```python
payment_section.screenshot("hw2/screenshots/payment.png")
```

## Скриншот всей страницы

```python
driver.save_screenshot("hw2/screenshots/payment_full.png")
```

---

# Управление окном браузера

Максимизировать:

```python
driver.maximize_window()
```

На весь экран:

```python
driver.fullscreen_window()
```

Свернуть:

```python
driver.minimize_window()
```

Установить размер:

```python
driver.set_window_size(640, 460)
```

---

# Навигация браузера

Назад:

```python
driver.back()
```

Вперёд:

```python
driver.forward()
```

Обновить страницу:

```python
driver.refresh()
```

---

# `time.sleep()`

Можно использовать для обучения и отладки:

```python
import time
time.sleep(2)
```

`time.sleep()` останавливает выполнение программы на указанное количество секунд.

---

# Явные ожидания

Импорты:

```python
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
```

Пример ожидания появления элемента:

```python
about_link = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.LINK_TEXT, "О нас"))
)
```

---


# `urls.py`

URL можно вынести в отдельный файл:

```python
HOMEPAGE = "https://itcareerhub.de/ru"
```

Тогда в тесте:

```python
from urls import HOMEPAGE
```

и:

```python
driver.get(HOMEPAGE)
```

---

# Шпаргалка по Selenium

| Действие | Код |
|---|---|
| Запустить Chrome | `webdriver.Chrome()` |
| Открыть страницу | `driver.get(url)` |
| Найти элемент | `driver.find_element(...)` |
| Найти по тексту ссылки | `By.LINK_TEXT` |
| Найти по ID | `By.ID` |
| Найти по XPath | `By.XPATH` |
| Клик | `element.click()` |
| Получить текст | `element.text` |
| Максимизировать окно | `driver.maximize_window()` |
| Назад | `driver.back()` |
| Вперёд | `driver.forward()` |
| Обновить | `driver.refresh()` |
| Скриншот элемента | `element.screenshot("file.png")` |
| Скриншот страницы | `driver.save_screenshot("file.png")` |
| Закрыть браузер | `driver.quit()` |

---

# Шпаргалка по Pytest

| Команда | Что делает |
|---|---|
| `pytest` | Запустить все найденные тесты |
| `pytest hw2` | Запустить тесты только из `hw2` |
| `pytest hw2 -v` | Подробный вывод |
| `pytest hw2 -s` | Показывать `print()` |
| `pytest hw2 -v -s` | Подробный вывод + `print()` |
| `pytest -k "about"` | Запустить тесты, в имени которых есть `about` |
| `pytest -x` | Остановиться после первой ошибки |
| `pytest --collect-only` | Показать найденные тесты без запуска |

---

# Запуск домашнего задания

Из корня репозитория:

```bash
pytest hw2 -v
```

Если нужно видеть `print()`:

```bash
pytest hw2 -v -s
```

Запустить только тесты способов оплаты:

```bash
pytest hw2 -v -k "payment"
```

---

# Короткая схема Selenium-теста

```text
открыть страницу
      ↓
найти элемент
      ↓
выполнить действие
      ↓
найти результат
      ↓
assert
```

Типичный тест:

```python
def test_something(driver):
    element = driver.find_element(By.LINK_TEXT, "Текст")
    element.click()

    result = driver.find_element(By.ID, "result")

    assert result.text == "Ожидаемый текст"
```
