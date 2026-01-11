from contextlib import asynccontextmanager

from fastapi import FastAPI
from sqlalchemy import text

from app.api.v1.routers.documents import router
from app.db.session import engine


# To się wykonuje RAZ przy starcie aplikacji
@asynccontextmanager
async def lifespan(app: FastAPI):
    print("STARTUJĘ APLIKACJĘ")
    try:
        # Próbujemy połączyć się z bazą
        async with engine.begin() as conn:
            await conn.execute(text("SELECT 1"))
        print("SUKCES! Połączono z bazą danych PostgreSQL.")
    except Exception as e:
        print(f"BŁĄD! Nie można połączyć z bazą: {e}")
    yield
    print("ZAMYKAM APLIKACJĘ")


app = FastAPI(lifespan=lifespan)
app.include_router(router=router, prefix="/api/v1/documents", tags=["documents"])


@app.get("/")
def read_root():
    return {"status": "ok"}
