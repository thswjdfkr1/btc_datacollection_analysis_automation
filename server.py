import markdown
from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles

app = FastAPI()
app.mount("/static", 
          StaticFiles(directory="C:/Users/thswj/Desktop/aa"),
          name='static')

class Report(BaseModel):
    btc_report: str

md_path = "C:/Users/thswj/Desktop/aa/btc_report.md"


@app.post("/api/btc_report")
def receive_report(data: Report):
    with open(md_path, "w", encoding="utf-8") as f:
        f.write(data.btc_report)
    print("보고서 수신 완료:", md_path)
    return {"status": "success"}

@app.get("/api/btc_report", response_class=HTMLResponse)
# def home():
#     return "<h1>FastAPI 서버 실행 중</h1>"

def get_report():
    try:
        with open(md_path, "r", encoding="utf-8") as f:
            md_content = f.read()
            md_content = md_content.replace('images/chart_1301.png',
                                            '/static/images/chart_1301.png')
            # return f"<pre>{md_content}</pre>"
            html_content = markdown.markdown(md_content, extensions=['fenced_code', 'tables'])
            return html_content
    except FileNotFoundError:
        return "<h2>보고서 파일을 찾을 수 없습니다.<h2>"
    
# if __name__ == "__main__":
#     import uvicorn
#     uvicorn.run(app, host="127.0.0.1", port=8000)