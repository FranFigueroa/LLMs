# Generador de Contenido para Twitter

Este proyecto es un generador automático de tweets creativos y personalizados, diseñado para publicar contenido relevante y atractivo en Twitter de manera autónoma. Utiliza modelos de lenguaje, plantillas de prompts, post-procesamiento inteligente y un sistema de memoria para evitar repeticiones.

---

## Características

- Generación automática de tweets a partir de prompts temáticos.
- Post-procesamiento para agregar hashtags, limpiar y acortar tweets.
- Memoria para evitar publicar contenido repetido o muy similar.
- Integración con la API de Twitter para publicación directa.
- Modularidad y facilidad de extensión.

---

## Estructura del Proyecto

```
twitter_content_generator/
│
├── requirements.txt
├── .env
├── README.md
│
├── config/
│   └── config.yaml
├── data/
│   └── prompts/
│       ├── saludo.txt
│       ├── noticia.txt
│       ├── motivacional.txt
│       └── humor.txt
│   └── tweet_memory.json
│
├── src/
│   ├── main.py
│   ├── generator.py
│   ├── postprocessing.py
│   ├── memory.py
│   └── twitter_api.py
│
└── tests/
    ├── test_generator.py
    ├── test_postprocessing.py
    └── test_memory.py
```

---

## Configuración

1. **Clona el repositorio y entra en la carpeta:**
   ```bash
   git clone https://github.com/tu_usuario/twitter_content_generator.git
   cd twitter_content_generator
   ```

2. **Instala las dependencias:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Configura tus claves de API en un archivo `.env`:**
   ```
   OPENAI_API_KEY=sk-...
   TWITTER_API_KEY=...
   TWITTER_API_SECRET=...
   TWITTER_ACCESS_TOKEN=...
   TWITTER_ACCESS_TOKEN_SECRET=...
   ```

4. **Edita o agrega tus propios prompts en `data/prompts/`.**

---

## Uso

Para generar y publicar un tweet:

```bash
python src/main.py
```

Puedes modificar el tipo de tweet, hashtags y otros parámetros editando `main.py` o pasándolos como argumentos.

---

## Pruebas

Para ejecutar las pruebas unitarias:

```bash
pytest
```

---

## Personalización

- Agrega nuevos tipos de prompts en `data/prompts/`.
- Ajusta el post-procesamiento en `src/postprocessing.py`.
- Modifica la lógica de memoria en `src/memory.py`.

---

## Licencia

MIT

---

## Mejoras Futuras

- Se planea agregar una funcionalidad para que el usuario pueda seleccionar fácilmente el tipo de tweets que desea publicar (motivacional, noticia, humor, etc.) sin modificar el código.
- Se implementará una interfaz más amigable para la configuración y el uso del generador.
- Otras mejoras para facilitar la personalización y la experiencia de usuario. 

---

¡Por supuesto! Aquí tienes un prompt optimizado para generar tweets de saludo, siguiendo los principios de prompt engineering para obtener mensajes originales, cálidos y adecuados para Twitter:

---

**saludo.txt**

```
Eres un generador de tweets de saludo para una cuenta de Twitter sobre inteligencia artificial, tecnología y aprendizaje. Tu objetivo es crear un tweet original y amistoso para dar los buenos días a los seguidores, transmitiendo energía positiva y entusiasmo por aprender o innovar.

Requisitos:
- El tweet debe ser breve y cálido (máximo 180 caracteres).
- Incluye un solo emoji relevante al final del tweet.
- No repitas frases típicas como “buenos días mundo” ni uses clichés.
- No incluyas hashtags, menciones ni enlaces.
- El tono debe ser cercano, motivador y optimista.
- No hagas referencia a que eres una IA ni a instrucciones de prompt.

Ejemplo de tweet:
¡Despierta tu curiosidad y deja que la tecnología te sorprenda hoy! ☀️

Ahora, genera un tweet siguiendo estas instrucciones.
```

---

**¿Por qué es un prompt de calidad?**
- Define el rol, el contexto y la intención del mensaje.
- Especifica longitud, tono, formato y restricciones.
- Fomenta la originalidad y evita clichés.
- Da un ejemplo concreto y relevante.
- Evita referencias meta, hashtags y enlaces para mantener el tweet limpio y profesional.

¿Te gustaría mejorar algún otro prompt o necesitas ayuda con otro tipo de mensaje? 