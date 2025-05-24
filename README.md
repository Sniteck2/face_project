# 🧠 Proyecto de Reconocimiento Facial en Tiempo Real con DeepFace + OpenCV

Este proyecto implementa un sistema de reconocimiento facial en tiempo real usando Python, [DeepFace](https://github.com/serengil/deepface) y OpenCV. Detecta rostros desde la cámara, los compara con una lista de personas autorizadas (whitelist) y registra eventos de rostros desconocidos.

---

## 📁 Estructura del Proyecto

```
face_project/
├── main.py                    # Lógica principal de ejecución
├── camera/                    # Módulo para el manejo de cámara
│   └── capture.py
├── detection/                 # Detección de rostros
│   └── detect.py
├── recognition/              # Carga y comparación de embeddings
│   ├── face_matcher.py
│   └── whitelist_loader.py
├── utils/                     # Utilidades (logging, dibujo, helpers)
│   ├── logger.py
│   └── drawer.py
├── known_faces/              # Carpeta con rostros conocidos (jpg/png)
├── logs/                      # Carpeta con eventos registrados
│   └── unknown_faces.csv
├── requirements.txt          # Dependencias
└── README.md                 # Esta documentación
```

---

## ⚙️ Requisitos

- **Python**: 3.11

---

## 📦 Instalación

1. **Clona el repositorio**
   ```bash
   git clone https://github.com/tuusuario/face_project.git
   cd face_project
   ```

2. **Crea un entorno virtual (opcional pero recomendado)**
   ```bash
   python -m venv venv
   venv\Scripts\activate
   ```

3. **Instala las dependencias**
   ```bash
   pip install -r requirements.txt
   ```

   El `requirements.txt` incluye:
   ```text
   deepface==0.0.93
   opencv-python==4.11.0.0
   numpy
   ```

---

## 🚀 Ejecución

Asegúrate de tener imágenes de referencia dentro del directorio `images/` (ej: `juan.jpg`, `maria.png`).

Luego ejecuta el sistema:
```bash
python main.py
```

- Se abrirá la cámara.
- Se detectarán todos los rostros visibles.
- Si un rostro coincide con alguien en el `images/`, se mostrará su nombre.
- Si el rostro es desconocido, se dibujará en rojo y se registrará un evento.

---

## 🧠 Funcionalidades

✅ Reconocimiento facial en tiempo real  
✅ Soporte para múltiples rostros en el mismo frame  
✅ Identificación por nombre sobre el recuadro del rostro  
✅ Registro automático de personas no reconocidas en CSV  
✅ Separación por módulos para fácil mantenimiento  
✅ Compatible con GPU (usando TensorFlow con CUDA si está disponible)  
✅ Optimización con embeddings preprocesados  
✅ Debug desde IntelliJ/PyCharm

---

## 📸 Cómo agregar personas al whitelist

1. Guarda una imagen clara del rostro en la carpeta `known_faces/`
2. El nombre del archivo sin extensión será el identificador (ej: `laura.jpg` → “laura”)
3. El sistema generará automáticamente su embedding al iniciar

---

## 🧪 ¿Cómo funciona el reconocimiento?

- Cada rostro se convierte en un vector numérico (embedding) usando **Facenet512**
- Se calcula la **distancia coseno** entre el rostro detectado y cada rostro conocido
- Si la distancia es menor a **0.3**, se considera la misma persona

---

## 📋 Logs de rostros desconocidos

Cada rostro no identificado se guarda como entrada en:
```
logs/unknown_faces.csv
```

Incluye:
- Timestamp
- Coordenadas del rostro
- Nivel de confianza

---

## 🛠️ Debug en IntelliJ / PyCharm

1. Usa `main.py` como archivo principal.
2. Agrega breakpoints (clic izquierdo en la línea).
3. Corre el script en modo *Debug*.
4. Explora variables en tiempo real (ej. `type(var)`, `var.keys()`, etc.)

---

## 📌 Consideraciones técnicas

- El modelo `Facenet` es más preciso pero más pesado que otros (puedes cambiar a `VGG-Face` si lo deseas)
- El sistema detecta cada rostro **por frame**, no hay tracking entre frames aún
- No se usa multithreading, pero el rendimiento es adecuado en una 4070 Ti

---

## 📈 Posibles mejoras futuras

- Agregar seguimiento por ID (tracking entre frames)
- Persistencia de embeddings ya calculados (para cargar más rápido)
- Interfaz gráfica (GUI)
- Notificaciones por correo/Telegram cuando se detecte un desconocido
- Entrenamiento personalizado

---

## 🔗 Recursos útiles

- [Documentación oficial de OpenCV](https://docs.opencv.org/)
- [Repositorio de DeepFace](https://github.com/serengil/deepface)
- [Facenet paper (2015)](https://arxiv.org/abs/1503.03832)

---

## 🧑‍💻 Autor

Proyecto desarrollado por Armando Ruz, 2025.  
Contacto: armandoruz.lyon@gmail.com

---