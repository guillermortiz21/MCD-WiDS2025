# WiDS2025
WiDS Datathon 2025

# Comenzando: Instalación y Autenticación de Kaggle API

Para bajar los datos y no tenerlos en Github, la formá más sencilla es interactuar con la API pública de Kaggle a través de su línea de comandos (CLI) implementada en Python.

## Instalación

Asegúrate de tener Python y el administrador de paquetes `pip` instalados. Luego, ejecuta el siguiente comando para acceder a la API de Kaggle desde la línea de comandos:

```bash
pip install kaggle
```


Para una instalación local en Linux, la ubicación predeterminada es `~/.local/bin`. En Windows, la ubicación predeterminada es `$PYTHON_HOME/Scripts`.

## Autenticación

Para utilizar la API pública de Kaggle, primero debes autenticarte mediante un token de API.

1. Ve a la pestaña "Settings" en tu perfil de usuario de Kaggle.
2. Selecciona "Create New Token".
3. Esto descargará un archivo llamado `kaggle.json`, que contiene tus credenciales de la API.

Si estás usando la herramienta CLI de Kaggle, esta buscará el token en:

* Linux, macOS y otros sistemas basados en UNIX: `~/.kaggle/kaggle.json`
* Windows: `C:\Users\<tu-usuario>\.kaggle\kaggle.json`

Si el token no se encuentra en la ubicación correcta, se generará un error. Por lo tanto, una vez descargado el token, muévelo desde la carpeta de descargas a la ubicación correspondiente. En este caso, para descargar los datos de la competencia, colócate en la carpeta `/data` y escribe el siguiente comando,

```bash
kaggle competitions download -c widsdatathon2025
```

**Nota**: Hay que estar registrado en la competencia.

Si utilizas la API de Kaggle directamente, la ubicación del token no es relevante, siempre que puedas proporcionar tus credenciales en tiempo de ejecución.

