
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from pathlib import Path
import uvicorn
import socket


app = FastAPI(title="Assetique Demo")

# 獲取當前文件所在目錄
BASE_DIR = Path(__file__).resolve().parent


@app.get("/Assetique/", response_class=HTMLResponse)
async def root():
    """提供 Demo 網頁作為首頁"""
    html_file = BASE_DIR / "Assetique Demo網頁.html"
    if html_file.exists():
        return HTMLResponse(content=html_file.read_text(encoding='utf-8'))
    else:
        return HTMLResponse(content="<h1>找不到 Assetique Demo網頁.html 文件</h1>", status_code=404)


if __name__ == "__main__":
    # 使用 0.0.0.0 讓服務器可以被本地網絡中的其他設備訪問
    host = "0.0.0.0"
    port = 5000

    # 獲取本機 IP 地址
    hostname = socket.gethostname()
    local_ip = socket.gethostbyname(hostname)

    print(f"\n{'='*60}")
    print(f"🚀 Assetique Demo 服務器啟動中...")
    print(f"{'='*60}")
    print(f"📍 本機訪問: http://127.0.0.1:{port}")
    print(f"🌐 局域網訪問: http://{local_ip}:{port}")
    print(f"📚 API 文檔: http://127.0.0.1:{port}/docs")
    print(f"{'='*60}\n")

    uvicorn.run(app, host=host, port=port)
    



