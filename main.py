import requests
from fastapi import Request, FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from fastapi import Body
from fastapi import Request
from fastapi import FastAPI, UploadFile, File
from fastapi.responses import JSONResponse
from fastapi.responses import PlainTextResponse
from fastapi.middleware.cors import CORSMiddleware
import time
from hanspell import spell_checker


app = FastAPI()


ALLOW_ORIGINS = [
    "http://127.0.0.1:5500",
    "http://localhost:5500",
    "http://127.0.0.1:3000",
    "http://localhost:3000",
    "http://127.0.0.1:5501",
    "http://localhost:5501",
    "https://hj-sp.github.io",
    "https://crystal-0109.github.io",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=ALLOW_ORIGINS,
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
    expose_headers=["*"],
    max_age=600,
)


class TextInput(BaseModel):
    content: str
    style: str = "default"
    offset: int = 0
    source: str = "rewrite"

class StyleChangeRequest(BaseModel):
    text: str
    style: str


@app.post("/editorGrammar")
async def editorGrammar(content: TextInput):
    print(content.content)
    print()

    result = spell_checker.check(content.content)

    print(f"원문        : {result.original}")
    print(f"수정된 문장 : {result.checked}")
    print(f"오류 수     : {result.errors}")
    print(f"단어별 상태 : {list(result.words.keys())}")
    print(f"검사 시간   : {result.time:.4f}초")
    print("-" * 40)

    return {
        "original": result.original,
        "checked": result.checked,
        "errors": result.errors,
        # "words": list(result.words.keys()),
        "time": result.time,
    }
