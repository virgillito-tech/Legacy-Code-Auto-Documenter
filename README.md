# Legacy Code Auto-Documenter 📄🤖

Un set di strumenti Python per analizzare automaticamente il codice sorgente (Legacy Code) e generare documentazione operativa e manuali utente in formato Markdown.

Il progetto include due versioni distinte per adattarsi alle esigenze di privacy e hardware:
1.  **Versione Cloud (OpenAI):** Per la massima qualità di analisi utilizzando GPT-5.
2.  **Versione Locale (Ollama):** Per la massima privacy e costo zero, girando interamente su GPU locale (es. NVIDIA RTX) senza inviare dati all'esterno.

---

## 🇮🇹 Versione Italiana

### Prerequisiti
* Python 3.8 o superiore
* Libreria OpenAI (`pip install openai`)
* (Solo per versione locale) [Ollama](https://ollama.com/) installato

### Installazione
1.  Clona il repository:
    ```bash
    git clone [https://github.com/virgillito-tech/Legacy-Code-Auto-Documenter.git](https://github.com/virgillito-tech/Legacy-Code-Auto-Documenter.git)
    cd Legacy-Code-Auto-Documenter
    ```
2.  Installa le dipendenze:
    ```bash
    pip install openai
    ```

### Guida all'uso

#### Opzione A: Versione Cloud (OpenAI)
Utilizza lo script `genera_manuale.py`. Ideale se non hai hardware potente e vuoi la massima precisione.

1.  Apri il file `genera_manuale.py` con un editor di testo.
2.  Inserisci la tua chiave API nella variabile:
    ```python
    API_KEY = "sk-..." # Incolla qui la tua chiave OpenAI
    ```
3.  Configura le cartelle di input/output:
    ```python
    SOURCE_FOLDER = "./tuo_codice"
    OUTPUT_FOLDER = "./manuali_generati"
    ```
4.  Esegui lo script:
    ```bash
    python genera_manuale.py
    ```

#### Opzione B: Versione Locale (Ollama / Privacy Mode)
Utilizza lo script `genera_manuale_locale.py`. I dati non lasciano mai il tuo computer. Richiede GPU (es. NVIDIA RTX 4060 o superiore consigliata).

1.  Assicurati di aver scaricato un modello (es. Llama 3):
    ```bash
    ollama pull llama3.1
    ```
2.  Apri il file `genera_manuale_locale.py` e verifica che il nome del modello corrisponda:
    ```python
    MODEL_NAME = "llama3.1"
    ```
3.  Esegui lo script (assicurati che Ollama sia attivo):
    ```bash
    python genera_manuale_locale.py
    ```

---

## 🇺🇸 English Version

### Overview
A set of Python tools to automatically analyze source code (Legacy Code) and generate operational documentation and user manuals in Markdown format.

The project features two separate versions to suit privacy and hardware needs:
1.  **Cloud Version (OpenAI):** For top-tier analysis quality using GPT-4o/GPT-5.
2.  **Local Version (Ollama):** For maximum privacy and zero cost, running entirely on local GPU (e.g., NVIDIA RTX) without sending data externally.

### Prerequisites
* Python 3.8+
* OpenAI library (`pip install openai`)
* (For local version only) [Ollama](https://ollama.com/) installed

### Installation
1.  Clone the repository:
    ```bash
    git clone [https://github.com/virgillito-tech/Legacy-Code-Auto-Documenter.git](https://github.com/virgillito-tech/Legacy-Code-Auto-Documenter.git)
    cd Legacy-Code-Auto-Documenter
    ```
2.  Install dependencies:
    ```bash
    pip install openai
    ```

### Usage Guide

#### Option A: Cloud Version (OpenAI)
Use the script `genera_manuale.py`. Best for high precision without needing powerful hardware.

1.  Open `genera_manuale.py` with a text editor.
2.  Insert your API Key in the variable:
    ```python
    API_KEY = "sk-..." # Paste your OpenAI Key here
    ```
3.  Configure input/output folders:
    ```python
    SOURCE_FOLDER = "./your_source_code"
    OUTPUT_FOLDER = "./generated_docs"
    ```
4.  Run the script:
    ```bash
    python genera_manuale.py
    ```

#### Option B: Local Version (Ollama / Privacy Mode)
Use the script `genera_manuale_locale.py`. Data never leaves your machine. Requires a GPU (e.g., NVIDIA RTX 4060 recommended).

1.  Ensure you have pulled a model (e.g., Llama 3):
    ```bash
    ollama pull llama3.1
    ```
2.  Open `genera_manuale_locale.py` and ensure the model name matches:
    ```python
    MODEL_NAME = "llama3.1"
    ```
3.  Run the script (make sure Ollama is running):
    ```bash
    python genera_manuale_locale.py
    ```

---

### Features
* **Recursive Scanning:** Automatically processes subfolders.
* **Smart Filtering:** Ignores system folders (`node_modules`, `venv`) and obsolete files (files containing `_old` in the name).
* **Markdown Output:** Generates ready-to-use `.md` files ideal for wikis or Vector Databases (RAG).

### Disclaimer
This tool uses Large Language Models to generate documentation. Always review the output for accuracy. No API keys are stored in this repository.
