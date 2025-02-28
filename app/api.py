from fastapi import APIRouter, Query
from datetime import date

router = APIRouter()

@router.get("/search")
def search_hotels(
    endereco: str,
    check_in: date,
    check_out: date,
    adultos: int = Query(ge=1, description="Número de adultos"),
    criancas: int = Query(ge=0, description="Número de crianças"),
    quartos: int = Query(ge=1, description="Número de quartos"),
    paginas: int = Query(ge=1, description="Número de páginas a serem procuradas")
):
 # Aqui será implementado o web scraping futuramente
    return {
        "status": "OK",
        "message": "A busca por hotéis foi iniciada. Os resultados serão processados em breve.",
        "parameters": {
            "endereco": endereco,
            "check_in": check_in,
            "check_out": check_out,
            "adultos": adultos,
            "criancas": criancas,
            "quartos": quartos,
        }
    }
