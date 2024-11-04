## Getting Started
1. Clone the repo
```commandline
git clone https://github.com/SaifuddinSaifee/figgi-io-backend.git
```
2. install the dependencies
```commandline
pip install -r requirements.txt
```

3. Start the server
```commandline
uvicorn app.main:app --reload --port 8000
```



## Project Structure
```commandline
figgi-io-backend/
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── config.py
│   ├── dependencies.py
│   ├── routers/
│   │   ├── __init__.py
│   │   ├── conversation.py
│   │   ├── image.py
│   │   ├── video.py
│   │   ├── music.py
│   │   ├── code.py
│   │   └── settings.py
│   ├── services/
│   │   ├── __init__.py
│   │   ├── conversation_service.py
│   │   ├── image_service.py
│   │   ├── video_service.py
│   │   ├── music_service.py
│   │   └── code_service.py
│   └── models/
│       ├── __init__.py
│       └── schemas.py
├── requirements.txt
└── .env
```