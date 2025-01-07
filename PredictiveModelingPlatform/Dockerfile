# 使用 Python 3.13 slim 作為基礎映像
FROM python:3.13.1-slim

# 安裝必要的系統依賴
RUN apt-get update && apt-get install -y \
    pkg-config \
    default-libmysqlclient-dev \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# 設定工作目錄
WORKDIR /app

# 複製當前目錄的文件到容器內
COPY . .

# 安裝 Python 依賴
RUN pip install --no-cache-dir -r requirements.txt

# 開放端口
EXPOSE 8000

# 設定容器啟動命令
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
