# Python Flet

## Initual setup

Create a virtual environment:
python3 -m venv .venv

Activate the virtual environment:

source .venv/bin/activate 

Install Flet:

pip install 'flet[all]'

Create flet app:

flet create

## Run the app

flet run

flet run --web 

 Utile mentre si sta scrivendo il codice perchè avvia l'app all'interno del browser e, dopo aver apportato modifiche al codice, basterà aggiornare il browser per vedere l'effetto (nella maggior parte delle tipologie di modifiche, ad esempio quelle grafiche)

flet run --android

 Crea un QR code che può essere scansionato tramite mobile Android (dove preventivamente è stato installata l'app di Flet)


For more details on running the app, refer to the [Getting Started Guide](https://flet.dev/docs/getting-started/).

## Build the app

### Introduction
E' importante che i pacchetti utilizzati siano nel file requirements.txt nella directory principale del progetto:

```pip freeze > requirements.txt```

Example:

```
flet build apk \ 
--project "nome dell'app" \
--org "com.nome organizzazione" \
--requirements pytubefix \
--include-assets assets

```


### Android

```
flet build apk -v
```

For more details on building and signing `.apk` or `.aab`, refer to the [Android Packaging Guide](https://flet.dev/docs/publish/android/).

### iOS

```
flet build ipa -v
```

For more details on building and signing `.ipa`, refer to the [iOS Packaging Guide](https://flet.dev/docs/publish/ios/).

### macOS

```
flet build macos -v
```

For more details on building macOS package, refer to the [macOS Packaging Guide](https://flet.dev/docs/publish/macos/).

### Linux

```
flet build linux -v
```

For more details on building Linux package, refer to the [Linux Packaging Guide](https://flet.dev/docs/publish/linux/).

### Windows

```
flet build windows -v
```

For more details on building Windows package, refer to the [Windows Packaging Guide](https://flet.dev/docs/publish/windows/).