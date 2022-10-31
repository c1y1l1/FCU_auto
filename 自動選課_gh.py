# 由於更改pyterract.py讀取檔案位址，須將OCR資料夾，存於同一目錄
# 在點選第一個加選時，選其他項目會導致出錯
# 藉由光學套件OCR直接正面突破驗證碼
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import NoSuchElementException 
from selenium.webdriver.chrome.options import Options
from time import sleep
import random
from 截圖 import get_captcha
from 處理 import deal
import tkinter as tk
import threading

window = tk.Tk()
window.title('選課系統')


def start():
    options = Options()
    options.add_argument("--incognito")
    global chrome
    chrome = webdriver.Chrome(ChromeDriverManager().install(), options=options)
    chrome.maximize_window()

    t = 0
    while True:
        if t == 10:
            print('出現錯誤過多，停止選課')
            exit()
        round_1 = 0
        while round_1 == 0:
            ## =========================
            print('login...................')

            chrome.get("https://course.fcu.edu.tw/")
            email = chrome.find_element(By.ID,"ctl00_Login1_UserName")
            password = chrome.find_element(By.ID,"ctl00_Login1_Password")
            captcha = chrome.find_element(By.ID,"ctl00_Login1_vcode")
            登入 = chrome.find_element(By.ID,'ctl00_Login1_LoginButton')
            ## 截圖==========================
            get_captcha(chrome,'ctl00_Login1_Image1','captcha.png')
            ## 處理==========================
            text = deal('captcha.png')
            sleep(1)
            ## =========================
            email.send_keys(account_entry.get())
            password.send_keys(password_entry.get())
            captcha.send_keys(text)
            sleep(2)
            登入.click
            sleep(1)
            ## =========================
            try:
                chrome.find_element(By.ID,"ctl00_MainContent_TabContainer1_tabSelected_Label3")
                # 已選課表.click
            except NoSuchElementException:
                print('=====================================登入失敗===================================')
                # chrome.close()
            else:
                round_1 = 1
                print('=====================================登入成功===================================')

        round_2 = 0
        已選課表 = chrome.find_element(By.ID,"ctl00_MainContent_TabContainer1_tabSelected_Label3")
        已選課表.click()
        print('=====================================開始加選===================================')
        while round_2 == 0:
            try:
                加選2 = chrome.find_element(By.ID,"ctl00_MainContent_TabContainer1_tabSelected_gvWishList_ctl04_btnAdd")
            except:
                pass
            else:
                加選2.click()
                sleep(random.uniform(1.9,2.1))
                                          
            try:
                加選 = chrome.find_element(By.ID,"ctl00_MainContent_TabContainer1_tabSelected_gvWishList_ctl02_btnAdd")
                加選.click()
                sleep(random.uniform(1.9,2.1))
            except:
                print('=====================================出現錯誤===================================')
                t += 1
                round_2 = 1
                print(t)
def finish():
    chrome.close()

def thread_it(func):
    t = threading.Thread(target=func) 
    t.setDaemon(True) 
    t.start()

warning = tk.Label(text='***開始選課前，請先將欲選科目關注***',bg='red',fg='white',font='Impact')
warning.grid(row=0,column=0,columnspan=4,sticky='we')

account_label = tk.Label(window, text='學號')
account_label.grid(row=1, column=0)
account_entry = tk.Entry(window,bg='paleturquoise')
account_entry.grid(row=1, column=1)

password_label = tk.Label(window, text='密碼')
password_label.grid(row=1, column=2)
password_entry = tk.Entry(window,bg='paleturquoise')
password_entry.grid(row=1, column=3)

start_brtton = tk.Button(window, text='開始選課', bg='gray65', command=lambda: thread_it(start))
start_brtton.grid(row=4,column=0,columnspan=2,sticky='we')
finish_brtton = tk.Button(window, text='結束選課', bg='gray65', command=lambda: thread_it(finish))
finish_brtton.grid(row=4,column=2,columnspan=2,sticky='we')

window.mainloop()