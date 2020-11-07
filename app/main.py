import uvicorn

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.route import router, auth, snmp

app = FastAPI()
origins = [
    "http://localhost:4200",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

app.include_router(router.router)
app.include_router(auth.router)
app.include_router(snmp.router)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000, debug='true')
