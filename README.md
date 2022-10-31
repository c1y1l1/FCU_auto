# FCU_auto
逢甲大學選課系統

* 目的：因為逢甲大學選課系統凌晨四點會強制登出，所以希望製作一個程式，自動輸入帳號、密碼、驗證碼並登入。
* 說明：透過`selenium`執行輸入、點擊，並用`OCR`辨識驗證碼。
  * `截圖.py`：針對驗證碼物件截圖
  <div align="center">
  <img src=https://github.com/c1y1l1/FCU_auto/blob/main/image_rm/captcha.png height="10%" width="10%"/>
  </div>
  
  * `處理.py`：將取得的圖片，用`PIL`做濾波、灰度、二值化處理
  <div align="center">
  <img src=https://github.com/c1y1l1/FCU_auto/blob/main/image_rm/deal.png height="10%" width="10%"/>
  </div>
  
  * `自動選課_gh.py`：
* 使用方法：
