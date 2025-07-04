from flask import Flask, render_template

app = Flask(__name__) # __name__代表目前執行的模組

@app.route("/") # 將CCTV頁面設定為網站的首頁
def cctv():
    # 定義CCTV影像的URL
    cctv_url = 'https://trafficvideo4.tainan.gov.tw/7c26a9dd'
    # 渲染cctv.html模板，並將cctv_url變數傳遞給模板
    # 這裡的 cctv_url=cctv_url 是關鍵，左邊是模板中使用的變數名，右邊是Python中的變數
    return render_template("cctv.html", cctv_url=cctv_url)

if __name__=="__main__": # 如果以主程式執行
    # 啟動伺服器，設定debug=True方便開發時除錯
    app.run(debug=True)
