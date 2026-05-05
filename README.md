# CertiFlow API

**CertiFlow API** é um motor criptográfico open-source projetado para geração e validação de certificados escolares em alta escala.

Este projeto baseia-se nos princípios de **Clean Architecture**, permitindo extrema facilidade de manutenção e troca de componentes (como banco de dados ou mensageria).

## Segurança Criptográfica (SHA-256)

Para evitar fraudes, cada certificado gerado pelo sistema recebe uma assinatura criptográfica unívoca utilizando o algoritmo **SHA-256**.
A assinatura é gerada através da combinação determinística dos dados do Aluno (ex: matrícula) e do Evento Acadêmico. 

Essa chave pode ser codificada em um **QR Code** no PDF, permitindo que a instituição valide a integridade do certificado emitido de forma instantânea na plataforma, sem depender de carimbos físicos.

## O Desafio (Hackathon)

Este repositório é fornecido como a infraestrutura "casca" do motor criptográfico. 
Para completar o sistema no Hackathon, os alunos deverão resolver os seguintes desafios de engenharia na camada de **Application** e **Infrastructure**:

1. **Parser de CSV em Alta Performance:** O Estado fornece a lista de alunos aprovados em um arquivo `.csv`. Você deve construir a lógica para ler este arquivo, instanciar as entidades `StudentModel` e tratá-las.
2. **Orquestração de Filas com Celery:** Gerar milhares de PDFs via Weasyprint consome muita CPU e memória, e faria a API HTTP travar. Você deve integrar o **Celery** (com Redis ou RabbitMQ) no caso de uso `GenerateBatchCertificatesUseCase` para despachar a renderização dos PDFs e envio de e-mails para *workers* assíncronos trabalhando em background.

## Estrutura do Projeto

*   **`domain/`**: Entidades e regras do negócio (`StudentModel`, lógica SHA-256).
*   **`application/`**: Casos de uso de geração em lote e validação de integridade. (Aqui começa o desafio!)
*   **`interface_adapters/`**: Controladores HTTP do FastAPI.
*   **`infrastructure/`**: Renderização em PDF (Weasyprint), Filas (Celery) e templates HTML (Jinja2).

## Como Instalar

```bash
git clone <url-do-seu-repositorio>
cd certiflow-api
python -m venv venv
# Ative o ambiente (venv\Scripts\activate no Windows ou source venv/bin/activate no Linux/Mac)
pip install -r requirements.txt
```

Boa sorte! Que seus workers processem os PDFs de forma veloz e resiliente!
