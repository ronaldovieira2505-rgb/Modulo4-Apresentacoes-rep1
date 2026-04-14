from fastapi import FastAPI, Form
from fastapi.responses import HTMLResponse, FileResponse
from pptx import Presentation
import os

app = FastAPI()


# 1. O nosso "Front-end" para o MVP
@app.get("/", response_class=HTMLResponse)
async def get_form():
    return """
    <html>
        <head>
            <title>Gerador de Apresentações - MVP</title>
            <style>
                body { font-family: Arial, sans-serif; padding: 50px; background-color: #f4f4f9; }
                .container { background: white; padding: 30px; border-radius: 8px; box-shadow: 0 4px 8px rgba(0,0,0,0.1); max-width: 600px; margin: auto; }
                textarea { width: 100%; padding: 10px; margin-bottom: 20px; border: 1px solid #ccc; border-radius: 4px; }
                button { padding: 10px 20px; background: #6200ea; color: white; border: none; border-radius: 4px; cursor: pointer; font-size: 16px; }
                button:hover { background: #3700b3; }
            </style>
        </head>
        <body>
            <div class="container">
                <h2>MVP: Gerador de Sprint Review 🚀</h2>
                <p>Insira o resumo da Sprint ou cole os commits recentes. O sistema irá gerar um arquivo de apresentação (.pptx).</p>
                <form action="/gerar-pptx" method="post">
                    <textarea name="resumo" rows="8" placeholder="Ex: \n- Refatoração do banco de dados\n- Criação da tela de login\n- Correção de bug no carrinho..."></textarea><br>
                    <button type="submit">Gerar Apresentação</button>
                </form>
            </div>
        </body>
    </html>
    """


# 2. O Back-end: Processamento e Geração do PPTX
@app.post("/gerar-pptx")
async def gerar_pptx(resumo: str = Form(...)):
    # Simulação da IA: Por enquanto, vamos apenas quebrar o texto por quebras de linha
    # No próximo passo, substituiremos isso pela chamada à LLM
    topicos = resumo.split('\n')

    # Criação do arquivo PowerPoint
    prs = Presentation()

    # Slide 1: Capa
    slide_capa = prs.slides.add_slide(prs.slide_layouts[0])
    slide_capa.shapes.title.text = "Sprint Review"
    slide_capa.placeholders[1].text = "Gerado automaticamente pela Plataforma"

    # Slide 2: Tópicos da Sprint
    slide_conteudo = prs.slides.add_slide(prs.slide_layouts[1])
    slide_conteudo.shapes.title.text = "Principais Entregas"
    corpo_texto = slide_conteudo.placeholders[1].text_frame
    corpo_texto.text = "Resumo:"

    # Adiciona cada linha do formulário como um bullet point no slide
    for topico in topicos:
        if topico.strip():
            p = corpo_texto.add_paragraph()
            p.text = topico.strip()
            p.level = 1

    # Salva o arquivo temporariamente
    file_path = "Sprint_Review_MVP.pptx"
    prs.save(file_path)

    # Retorna o arquivo para download automático no navegador
    return FileResponse(
        path=file_path,
        media_type='application/vnd.openxmlformats-officedocument.presentationml.presentation',
        filename="Sprint_Review.pptx"
    )