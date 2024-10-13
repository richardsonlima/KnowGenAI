import gradio as gr
import json
import zipfile
from datetime import datetime
import tempfile

# Função para gerar o arquivo ZIP
def generate_zip(produto, segmento, jornada, questionario):
    linhas = questionario.strip().split("\n")
    
    dados = []
    pergunta = None
    resposta = None

    for linha in linhas:
        linha = linha.strip()
        if linha.startswith("Pergunta:"):
            if pergunta and resposta:
                dados.append({
                    "titulo": f"Título-{len(dados) + 1}: {pergunta[:30]}",
                    "produto": produto,
                    "segmento": segmento,
                    "jornada": jornada,
                    "pergunta": pergunta,
                    "resposta": resposta
                })
            pergunta = linha.replace("Pergunta:", "").strip()
            resposta = None  
        elif linha.startswith("Resposta:"):
            resposta = linha.replace("Resposta:", "").strip()
    
    if pergunta and resposta:
        dados.append({
            "titulo": f"Título-{len(dados) + 1}: {pergunta[:30]}",
            "produto": produto,
            "segmento": segmento,
            "jornada": jornada,
            "pergunta": pergunta,
            "resposta": resposta
        })

    with tempfile.NamedTemporaryFile(delete=False, suffix=".zip") as temp_zip_file:
        with zipfile.ZipFile(temp_zip_file, "w") as z:
            for idx, row in enumerate(dados):
                json_filename = f"pergunta_resposta_{idx + 1}.json"
                z.writestr(json_filename, json.dumps(row, ensure_ascii=False, indent=4))

    return temp_zip_file.name

def gradio_generate_zip(produto, segmento, jornada, questionario):
    return generate_zip(produto, segmento, jornada, questionario)

# Função para RAG-Enhanced Knowledge Base
def rag_enhanced_knowledge_base():
    return "RAG-Enhanced Knowledge Base generated."

# Função para In-Context Learning
def in_context_learning():
    return "In-Context Learning applied."

# Função para atualizar a interface
def update_interface(selected_option):
    if selected_option == "Gerar JSON files":
        return gr.update(visible=True), gr.update(visible=False), gr.update(visible=False)
    elif selected_option == "RAG-Enhanced Knowledge Base":
        return gr.update(visible=False), gr.update(visible=True), gr.update(visible=False)
    elif selected_option == "In-Context Learning":
        return gr.update(visible=False), gr.update(False), gr.update(True)

# Função para atualizar o idioma
def update_language(selected_language):
    lang = {
        "en": {
            "welcome": "Welcome to KnowGenAI",
            "description": "This application allows you to generate JSON files, create RAG-enhanced knowledge bases, and apply in-context learning.",
            "option_label": "Choose an option",
            "generate_zip": "Generate ZIP",
            "rag_knowledge": "Generate RAG Knowledge Base",
            "icl_learning": "Apply In-Context Learning",
            "product": "Product",
            "segment": "Segment",
            "journey": "Journey",
            "questionnaire": "Questionnaire",
            "question_placeholder": "Enter the questionnaire in the format:\n\nQuestion: What is your name?\nAnswer: John\n\nQuestion: How old are you?\nAnswer: 30",
            "download_zip": "Download ZIP file"
        },
        "pt": {
            "welcome": "Bem-vindo ao KnowGenAI",
            "description": "Esta aplicação permite gerar arquivos JSON, criar bases de conhecimento aprimoradas por RAG e aplicar aprendizado em contexto.",
            "option_label": "Escolha uma opção",
            "generate_zip": "Gerar ZIP",
            "rag_knowledge": "Gerar Base de Conhecimento RAG",
            "icl_learning": "Aplicar Aprendizado em Contexto",
            "product": "Produto",
            "segment": "Segmento",
            "journey": "Jornada",
            "questionnaire": "Questionário",
            "question_placeholder": "Digite o questionário no formato:\n\nPergunta: Qual é seu nome?\nResposta: João\n\nPergunta: Qual é sua idade?\nResposta: 30",
            "download_zip": "Baixar arquivo ZIP"
        }
    }
    
    selected_text = lang[selected_language]
    return (
        gr.update(value=selected_text["welcome"]),
        gr.update(value=selected_text["description"]),
        gr.update(choices=[selected_text["generate_zip"], selected_text["rag_knowledge"], selected_text["icl_learning"]]),
        gr.update(label=selected_text["option_label"]),
        gr.update(label=selected_text["product"]),
        gr.update(label=selected_text["segment"]),
        gr.update(label=selected_text["journey"]),
        gr.update(label=selected_text["questionnaire"]),
        gr.update(placeholder=selected_text["question_placeholder"]),
        gr.update(label=selected_text["download_zip"])
    )

# Interface Gradio
with gr.Blocks() as demo:
    gr.Markdown("# KnowGenAI")
    
    with gr.Row():
        with gr.Column(scale=1):
            gr.Markdown("## Menu")
            selected_option = gr.Radio(label="Escolha uma opção", choices=["Gerar JSON files", "RAG-Enhanced Knowledge Base", "In-Context Learning"], value="Gerar JSON files")
            language_selector = gr.Radio(label="Select Language", choices=["en", "pt"], value="en")
            
        with gr.Column(scale=3):
            welcome_text = gr.Markdown("Welcome to KnowGenAI")
            description_text = gr.Markdown("This application allows you to generate JSON files, create RAG-enhanced knowledge bases, and apply in-context learning.")
            
            # Componente principal onde as opções aparecerão
            with gr.Group(visible=True) as main_content:
                # Componentes para Gerar JSON files
                with gr.Group(visible=True) as json_group:
                    produto = gr.Textbox(label="Product")
                    segmento = gr.Textbox(label="Segment")
                    jornada = gr.Textbox(label="Journey")
                    questionario = gr.Textbox(label="Questionnaire", 
                        placeholder="Enter the questionnaire in the format:\n\nQuestion: What is your name?\nAnswer: John\n\nQuestion: How old are you?\nAnswer: 30", lines=10)
                    output_file = gr.File(label="Download ZIP file")
                    generate_button = gr.Button("Generate ZIP")
                    generate_button.click(gradio_generate_zip, inputs=[produto, segmento, jornada, questionario], outputs=output_file)
                
                # Componentes para RAG-Enhanced Knowledge Base
                with gr.Group(visible=False) as rag_group:
                    rag_btn = gr.Button("Generate RAG Knowledge Base")
                    rag_output = gr.Textbox(label="RAG Output")
                    rag_btn.click(rag_enhanced_knowledge_base, outputs=rag_output)

                # Componentes para In-Context Learning
                with gr.Group(visible=False) as icl_group:
                    icl_btn = gr.Button("Apply In-Context Learning")
                    icl_output = gr.Textbox(label="ICL Output")
                    icl_btn.click(in_context_learning, outputs=icl_output)

            # Atualizar a interface com base na seleção do menu
            selected_option.change(update_interface, inputs=selected_option, outputs=[json_group, rag_group, icl_group])
            language_selector.change(update_language, inputs=language_selector, outputs=[welcome_text, description_text, selected_option, selected_option, produto, segmento, jornada, questionario, output_file])

# Inicia a interface Gradio
if __name__ == "__main__":
    demo.launch()
