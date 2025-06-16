from flask import Flask, render_template

app = Flask(__name__) # __name__代表目前執行的模組

@app.route("/") 
def cctv():
    # 定義CCTV影像的URL
    cctv_url = 'https://trafficvideo4.tainan.gov.tw/7c26a9dd'
    # 渲染cctv.html模板，並將cctv_url傳遞給模板
    return render_template("cctv.html", cctv_url=cctv_url)

if __name__=="__main__": # 如果以主程式執行
    # 啟動伺服器，設定debug=True方便開發時除錯
    # 在生產環境中，請移除或設定debug=False
    app.run(debug=True)
