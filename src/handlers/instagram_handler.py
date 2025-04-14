import os
import time
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

load_dotenv()

def create_driver():
    chrome_options = Options()
    chrome_options.add_argument(
        "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36"
    )
    chrome_options.add_argument("--window-size=1920,1080")
    service = Service(ChromeDriverManager().install())
    return webdriver.Chrome(service=service, options=chrome_options)

def login(driver):
    INSTAGRAM_USER = os.getenv("INSTAGRAM_USER")
    INSTAGRAM_PASS = os.getenv("INSTAGRAM_PASS")

    driver.get("https://www.instagram.com/")
    time.sleep(5)

    username_input = driver.find_element(By.NAME, "username")
    password_input = driver.find_element(By.NAME, "password")

    username_input.send_keys(INSTAGRAM_USER)
    password_input.send_keys(INSTAGRAM_PASS)
    password_input.send_keys(Keys.ENTER)

    time.sleep(10)

def send_message(driver, target_user, message):
    driver.get(f"https://www.instagram.com/{target_user}/")
    time.sleep(5)

    try:
        message_button = driver.find_element(By.XPATH, "//div[text()='Message']")
        message_button.click()
        time.sleep(5)

        wait = WebDriverWait(driver, 10)
        message_box = wait.until(EC.presence_of_element_located((By.XPATH, "//div[@role='textbox']")))

        message_box.send_keys(message)
        message_box.send_keys(Keys.ENTER)
        time.sleep(5)
        print(f"Mensagem enviada para {target_user}")
    except Exception as e:
        print(f"Erro ao tentar enviar para {target_user}: {e}")

def send_messages_to_users(usernames: list[str], message: str):
    driver = create_driver()
    try:
        login(driver)
        for user in usernames:
            send_message(driver, user, message)
    finally:
        driver.quit()
