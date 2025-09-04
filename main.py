from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from dotenv import load_dotenv
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import time
import os 

def launch_chrome():
    options = Options()
    # options.add_argument("--headless=new")  # headless mode rapide
    # options.add_argument("--disable-gpu")
    # options.add_argument("--no-sandbox")
    # options.add_argument("--disable-dev-shm-usage")

    driver = webdriver.Chrome(options=options)
    return driver


def send_mail():
    expediteur = os.environ["MAIL"]
    destinataire = os.environ["MAIL"]
    mot_de_passe = os.environ["MAIL_PASSWORD"]

    sujet = "Bot Selenium - Bouton cliqué ✅"
    corps = "https://resell.seetickets.com/fete-de-lhumanite-2025/cart"

    # Création du message
    message = MIMEMultipart()
    message["From"] = expediteur
    message["To"] = destinataire
    message["Subject"] = sujet
    message.attach(MIMEText(corps, "plain"))

    try:
        # Connexion au serveur SMTP de Gmail
        serveur = smtplib.SMTP("smtp.gmail.com", 587)
        serveur.starttls()
        serveur.login(expediteur, mot_de_passe)
        serveur.sendmail(expediteur, destinataire, message.as_string())
        serveur.quit()
        print("📩 Mail envoyé avec succès !")
    except Exception as e:
        print(f"❌ Erreur lors de l'envoi du mail : {e}")



def connect_user(driver):
    driver.get("https://resell.seetickets.com/fete-de-lhumanite-2025/login")

    # Trouver le champ "username" et remplir
    username = driver.find_element(By.ID, "inputEmail")  # ou By.NAME / By.XPATH
    username.send_keys(os.environ["HUMA_MAIL"])

    # Trouver le champ "password" et remplir
    password = driver.find_element(By.ID, "inputPassword")
    password.send_keys(os.environ["HUMA_PASSWORD"])

    # Cliquer sur le bouton "Se connecter"
    login_button = driver.find_element(By.XPATH, "//button[text()='Se connecter']")
    login_button.click()

    time.sleep(3)


def shotgun(driver):

    # driver.get("https://resell.seetickets.com/fete-de-lhumanite-2025/category/5195/fEte-de-l-humanitE-2025-pass-3-jours")
    driver.get("https://resell.seetickets.com/fete-de-lhumanite-2025/category/5196/fEte-de-l-humanitE-2025-camping")
    while True:
        time.sleep(0.5)
        try:
            # Attendre que le bouton apparaisse (max 10s)
            bouton = driver.find_element(By.XPATH, '//button[@title="Ajouter au panier"]')
            bouton.click()
            print("✅ Bouton cliqué !")
            send_mail()
        except:
            print("❌ Bouton pas dispo, on recharge...")
            driver.refresh()
            



if __name__ == "__main__":
    load_dotenv()
    driver = launch_chrome()
    connect_user(driver)
    shotgun(driver)