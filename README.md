# FCU_auto
逢甲大學選課系統

* 目的：因為逢甲大學選課系統凌晨四點會強制登出，所以希望製作一個程式，自動輸入帳號、密碼、驗證碼並登入。
* 說明：透過`selenium`執行輸入、點擊，並用`OCR`辨識驗證碼。
  * `截圖.py`：針對驗證碼物件截圖
  <div align="center">
  <img src=https://github.com/c1y1l1/FCU_auto/blob/main/image_rm/captcha.png height="10%" width="10%"/>
  </div>
  
  * `處理.py`：將取得的圖片，用`PIL`做濾波、灰度、二值化處理，再用`pytesseract`(OCR套件)辨識並回傳文字
  <div align="center">
  <img src=https://github.com/c1y1l1/FCU_auto/blob/main/image_rm/deal.png height="11%" width="11%"/>
  </div>
  
  * `自動選課_gh.py`：主程式，運行此就好
* 使用方法：
1. 依照連結內容安裝OCR[【Python OCR 使用手冊】圖片轉文字 超簡單上手](https://ithelp.ithome.com.tw/articles/10283765)
2. 將欲選科目關注
3. 執行`自動選課_gh.py`程式，會出現小視窗，輸入學號、密碼後，點選開始選課即可
  <div align="center">
  <img src=https://github.com/c1y1l1/FCU_auto/blob/main/image_rm/window.png height="35%" width="35%"/>
  </div>
  
  
