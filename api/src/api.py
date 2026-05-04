from fastapi import FastAPI
from .routes.routes import routes
from fastapi.middleware.cors import CORSMiddleware

description = """
`@Projeto` Lumi\n
`@Autores` Isabelle Sales, Lucas Dantas, Marcus Monteiro, Marcus Azevedo e Samuel Abrahão\n
`@Feito em` Abril 10, 2026\n

### Descrição
Uma API que faz integração de dados de diferentes instituições bancárias por meio de APIs de Open Finance, fornecendo-as ao o usuário para que ele visualize e gerencie suas informações financeiras de forma centralizada.
"""

app = FastAPI(
    title='Lumi - Open Finance Integration API',
    description=description,
    version='V1.0'
)

app.add_middleware(
  CORSMiddleware,
  allow_origins=["*"],
  allow_credentials=True,
  allow_methods=["*"],
  allow_headers=["*"],
)

for route in routes:
    app.include_router(route.router)