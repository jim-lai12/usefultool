# usefultool
 
cookieway 整合selenium,cooklib,requests的cookiejar可以相互切換,存檔,讀取

load():讀取,預設檔名為cookie.txt

save():存檔,預設檔名為cookie.txt

torequestscjs(s):將讀取的cookie轉成requests的cookiejar,s為requests.session

toseleniumcj(driver):將讀取的cookie轉成selenium的cookiejar,driver為webdriver

sele2resq,resq2sele:將其中一個的cookie加到另一個

selcj_cj,reqcj_cj:轉回cooklib的cookiejar形式,用於存檔前
