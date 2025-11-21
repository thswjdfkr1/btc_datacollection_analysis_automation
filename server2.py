from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles

app = FastAPI()
app.mount("/static", 
          StaticFiles(directory="C:/Users/thswj/Desktop/aa"),
          name='static')

html_path = "C:/Users/thswj/Desktop/aa/btc_report.html"

class Report(BaseModel):
    btc_report: str

@app.post("/btc_report")
def receive_report(data: Report):
    with open(html_path, "w", encoding="utf-8") as f:
        f.write(data.btc_report)
    print("보고서 수신 완료:", html_path)
    return {"status": "success"}

@app.get("/btc_report", response_class=HTMLResponse)
def get_html_report():
    try:
        with open(html_path, "r", encoding="utf-8") as f:
            html_content = f.read()
            html_content = html_content.replace('images/chart_1301.png',
                                            '/static/images/chart_1301.png')            
            return html_content
    except FileNotFoundError:
        return "<h2>HTML 보고서 파일을 찾을 수 없습니다.</h2>"