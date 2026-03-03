from fastapi import FastAPI

app = FastAPI()

cursos = {
   1 : {"titulo" : "Python-Programação para Leigos ", "aulas" : 112, "horas" : 58},
   2 : {"titulo" : "Python-Algoritmo e Lógica de Programação", "aulas" : 87, "horas" : 67},
   3 : {"titulo" : "C++", "aulas" : 16, "horas" : 40} 
}

if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", host="0.0.0.0", port=8000, log_level="info", reload=True)

