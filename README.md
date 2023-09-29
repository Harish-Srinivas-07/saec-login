# 🌟 SAEC College Login Portal Automation 🚀

Welcome to the **SAEC College Login Portal Automation** project! 🤖

This project is an automation script developed during my study period for SAEC College's login portal. It serves the purpose of gaining practical experience in web automation, enhancing understanding of web security, and applying cybersecurity concepts. 💻🔐

## 🏫 About SAEC College 🎓

SAEC College is a prestigious educational institution known for its dedication to excellence in engineering education. S.A. Engineering College offers students an advantageous atmosphere with state-of-the-art facilities, distinguished mentors, and a pleasant educational environment. The institution provides employability and communication skills for the development of students. It focuses on shaping students to become self-disciplined, self-dependent, and self-confident individuals. SAEC pulls out all the stops to mold students' careers in such a way that they excel in all fine distinctions of life. 🌐🎓

- **College Website**: [https://saec.ac.in](https://saec.ac.in) 🌐
- **SAEC Student Login Portal**: [https://coe.saec.ac.in/exam/studentlogin/login.php](https://coe.saec.ac.in/exam/studentlogin/login.php) 🔑
- **SAEC Fees Payment (for name extraction)**: [https://www.saec.ac.in/onlinefeepayment](https://www.saec.ac.in/onlinefeepayment) 💰

## 🎯 Project Objectives 🚀🎯

- Automate the login process for SAEC College's login portal using Python, Selenium, and Requests.
- Demonstrate web automation techniques for interacting with dynamic web pages.
- Explore web security and authentication mechanisms to understand potential vulnerabilities.
- Develop practical skills in handling web forms, HTTP requests, and session management.

## 🧰 Technical Details ⚙️🧰

This project relies on the following technologies and libraries:

- Python 3.x
- Selenium: A powerful tool for web automation.
- Requests: A Python library for making HTTP requests.
- Microsoft Edge WebDriver: Required for Edge browser automation.
- Time: Python's standard library for handling time and date operations.
- Re: Python's regular expression library, used for pattern matching in the script.

You can ensure you have these dependencies installed before running the project. Additionally, please take note of the updated code provided, which includes these imports.

## 🤖 How It Works 🌐🤖

1. The script sends an HTTP POST request to the SAEC College API endpoint to fetch data.
2. Based on the API response, it extracts relevant information.
3. The automation script uses Selenium to interact with the login page:
   - It enters your SAEC College credentials.
   - Navigates through the portal to perform actions like accessing exam results, personal details, retrieving fees details, and changing the password to "Hacked@123" without authorization.
   - Retrieves a name from the UG fees payment portal database.
   - Combines the date of birth (DOB) to crack the password.
4. The script ensures secure handling of credentials and automates the logout process when needed. 🔐🕒

Please note that unauthorized password changes are performed for educational purposes and should not be used without proper authorization. Fees details are retrieved using email and phone numbers, which are obtained from profile information and open-source resources with AES encryption.

## 💻 Installation 🛠️💻

1. **Clone the repository**:

    ```bash
    git clone https://github.com/Harish-Srinivas-07/saec-login.git
    ```
    
2. **Install dependencies through cmd**:
   
   ```bash
   pip install requests
   pip install selenium
   ```

3. **Download the Microsoft Edge WebDriver** and add it to your system's PATH. You can download it from [Microsoft Edge WebDriver](https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/).
4. **Run the code** by pressing **F5** in the Python shell. 🚀

## ▶️ Usage 🕹️▶️

1. **Run the Python script.**

2. Follow the on-screen prompts to interact with the SAEC College login portal. 🖥️

## 🎮 Actions 🤖🎮

Here's a detailed breakdown of the actions performed by the SAEC College Login Portal Automation tool:

- **Home - login page**: The starting point for logging into the SAEC College portal.

- **June 2023 Marks**: Access your exam results for June 2023.

- **Personal Details**: Retrieve your personal information stored in the portal's database.

- **Exam Performance**: Access detailed information about your exam performance.

- **Internal Assessment Details**: Obtain information about internal assessments and your performance in them.

- **Change Password**:
  - Actual change the password for the logged-in account to "Hacked@123." Note: This action is performed for educational purposes and should not be used without proper authorization.

- **Retrieve Fees Details (using email and phone numbers with AES encryption)**:
  - **Predict Email IDs**:
    - Utilizes the registration number associated with the account to predict email IDs.
  - **Personal Phone Number**:
    - Attempts to retrieve fees details using the personal phone number found on the profile details page.
  - **AES Encryption**:
    - Employs AES encryption to secure the retrieval of fees details.

- **Logout**: Logs out of the SAEC College portal.

Additionally, it's worth noting that the software can identify accounts that have had their passwords changed by this tool, as they will have the password "Hacked@123." This information is provided for educational purposes and should not be used maliciously.

## 👤 Author 👨‍💻

- **Harish Srinivas SR - IV CSE-A 2020 Batch** 🎓
- **GitHub**: [Harish-Srinivas-07](https://github.com/Harish-Srinivas-07) 🌐

---

**Explore the world of web automation, cybersecurity, and practical programming with this project!** 🌐💡
