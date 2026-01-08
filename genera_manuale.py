import os
from openai import OpenAI

#per lanciare lo script entrare in ambiente virtuale con il comando: "source path/to/venv/bin/activate" e poi lanciare "python genera_manuale.py"

#chiave API 
API_KEY = "sk-"

#nome modello da utilizzare
MODEL_NAME = "gpt-5.2"

#cartella di origine dei file di input
SOURCE_FOLDER = ""

#cartella di destinazione dei file di output
OUTPUT_FOLDER = ""

#estensioni file da analizzare
ALLOWED_EXTENSIONS = {'.py', '.js', '.php', '.html', '.sql'}

#estensioni da ignorare
IGNORE_DIRS = {'node_modules', 'venv', '__pycache__', 'dist', 'build'}

#setup client
client = OpenAI(api_key=API_KEY)

def leggi_file(filepath):
    """Questa funzione legge il contenuto di un file di codice"""
    try:
        with open(filepath, 'r', encoding='utf-8', errors='ignore') as file:
            return file.read()
    except Exception as e:
        print(f"Errore nella lettura del file {filepath}: {e}")
        return None
    
def genera_documentazione(nome_file, codice):
    """Questa funzione chiama l'API per generare una documentazione (guida utente) dal codice"""

    #prompt API
    system_prompt = """Sei un esperto sviluppatore software. Il tuo compito è analizzare il codice sorgente fornito e scrivere una guida operativa per operatori e staff del Call Center su tutte le funzionalità permesse all'utente finale.
    REGOLE FONDAMENTAL:
    1. Non spiegare il codice tecnico (niente funzioni, variabili, array, classi)
    2. Spiega l'azione: cosa permette di fare questo codice all'utente finale?
    3. Se il codice è solo infrastruttura tecnica e non ha impatto sull'utente, scrivi solo 'Nessun impatto operativo rilevante'
    4. Usa un linguaggio chiaro, passo-passo
    5. Formatta l'output in Markdown con titoli e sottotitoli appropriati 
    """
    user_prompt = f"""Analizza il seguente file: {nome_file}

    ```
    {codice}
    ```

    Scrivi la documentazione operativa relativa a questo file.
    """

    try:
        response = client.chat.completions.create(
            model=MODEL_NAME,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt}
            ],
            temperature=0.2, #bassa temperature per risposte più precise e meno creative
        )
        return response.choices[0].message.content
    except Exception as e:
        print(f"Errore API nel file {nome_file}: {e}")
        return None
    
def main():
    """Funzione per processare i file e generare la documentazione"""
    # SICUREZZA: Aggiunge la cartella di output a quelle da ignorare, evita che lo script legga i manuali che sta creando
    if OUTPUT_FOLDER:
        nome_cartella_output = os.path.basename(os.path.normpath(OUTPUT_FOLDER))
        IGNORE_DIRS.add(nome_cartella_output)

    #crea cartella output se non esiste
    if not os.path.exists(OUTPUT_FOLDER):
        os.makedirs(OUTPUT_FOLDER)
        print(f"Cartella '{OUTPUT_FOLDER}' creta.")

    print(f"Inizio analisi con modello {MODEL_NAME}")

    #scansiona la cartella di origine ricorsivamente
    for root, dirs, files in os.walk(SOURCE_FOLDER):
        #rimuoviamo le cartella ignorate dalla scansione
        dirs[:] = [d for d in dirs if d not in IGNORE_DIRS]

        for file in files:
            #saltiamo file con _old o _OLD nel nome
            if "_old" in file.lower():
                print(f"Salto file obsoleto: {file}")
                continue

            ext = os.path.splitext(file)[1]
            if ext in ALLOWED_EXTENSIONS:
                filepath = os.path.join(root, file)
                relative_path = os.path.relpath(filepath, SOURCE_FOLDER)

                print(f"Analisi del file: {relative_path}...")

                codice = leggi_file(filepath)
                if codice and len(codice) > 50: #ignora file con meno di 50 caratteri  
                  
                   doc = genera_documentazione(relative_path, codice)
                
                   if doc: 
                       #crea il percorso per il file di output mantendendo la struttura
                       output_path = os.path.join(OUTPUT_FOLDER, relative_path) + ".md"
                       os.makedirs(os.path.dirname(output_path), exist_ok=True)

                       with open(output_path, 'w', encoding='utf-8') as file_out:
                           file_out.write(doc)

                       print(f" -> Documentazione generata e salvata in: {output_path}")
                else:
                    print("Saltato (vuoto/corto)")

    print("Analisi completata.")

if __name__ == "__main__":
    main()
                    



