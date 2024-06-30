# Proyecto Tasks App

Este proyecto es una aplicación web para la gestión de tareas, construida con un frontend en JavaScript y un backend en Django.

## Características

- Crear, actualizar y eliminar tareas.
- Marcar tareas como completadas.
- Interfaz de usuario simple y fácil de usar.

## Requisitos

- Python 3.x
- Node.js y npm

## Instalación

1. Clona este repositorio en tu máquina local:

   ```bash
   git clone https://github.com/Fernan-Pro/tasks_app.git
   cd tasks_app
   ```

2. Instala las dependencias del backend:

   ```bash
   cd backend
   pip install -r requirements.txt
   ```

3. Instala las dependencias del frontend:

   ```bash
   cd ../frontend
   npm install
   ```

## Uso

1. Inicia el servidor backend:

   ```bash
   cd backend
   python manage.py runserver
   ```

2. Inicia el servidor frontend:

   ```bash
   cd ../frontend
   npm start
   ```

3. Abre tu navegador y navega a `http://localhost:3000` para usar la aplicación.

## Estructura del Proyecto

```plaintext
.
├── README.md
├── backend
│   ├── manage.py
│   ├── requirements.txt
│   └── ...
└── frontend
    ├── package.json
    ├── src
    │   ├── index.js
    │   └── ...
    └── ...
```

- `backend`: Contiene el código y dependencias del servidor backend hecho con Django.
- `frontend`: Contiene el código y dependencias del cliente frontend.

## Contacto

Para cualquier consulta o sugerencia, puedes contactarme a través de ferqtexwinner@gmail.com.
