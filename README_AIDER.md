# AIDER

## Installazione
```
python -m pip install aider-install

aider-install
```

## Caricamento Api Key
Creare il file .env all'interno della cartella di progetto con la api key; nell'esempio che segue vi è una api key di Openrouter

```
.env
OPENROUTER_API_KEY=your key
```

## Avvio
Avviare Aider indicando il modello da utilizzare; di seguito due esempi:

```aider --model=openrouter/qwen/qwen3-coder:free```

```aider --model=openrouter/mistralai/devstral-2512:free```

```aider --model=openrouter/deepseek/deepseek-r1-0528:free```

## Persistent Prompt
Per caricare un Persistent Prompt File che indicherà al modello LLL come comportarsi, quali sono gli standard che deve seguire, l'architettura, etc

```/read requirements.md```

## Cambiare modello LLM

```/model openrouter/deepseek/deepseek-r1-0528:free```
