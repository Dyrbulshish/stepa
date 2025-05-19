import time
from selenium.webdriver.common.by import By

def test_button_add_to_cart_is_present(browser):
    # Открываем страницу товара
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)
    
    # Визуальная проверка (время для просмотра страницы)
    time.sleep(30)
    
    # Поиск кнопки добавления в корзину
    button_locator = "button.btn-add-to-basket"
    button = browser.find_elements(By.CSS_SELECTOR, button_locator)
    
    # Проверка наличия кнопки
    assert len(button) > 0, f"Button with selector '{button_locator}' is not found on the page."
    print(f"\nButton with selector '{button_locator}' is present on the page.")
