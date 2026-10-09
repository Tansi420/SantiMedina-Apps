import streamlit as st
from PIL import Image

# Configuración de la página
st.set_page_config(
    page_title="Portafolio de Aplicaciones Creativas | Santiago Medina",
    page_icon="🎨",
    layout="wide"
)

# Estilos CSS personalizados para una interfaz moderna y llamativa
st.markdown("""
    <style>
    /* Fondo general y tipografía */
    .main {
        background-color: #0f1117;
        color: #e2e8f0;
    }
    
    /* Encabezado principal */
    .hero-container {
        background: linear-gradient(135deg, #1e1b4b 0%, #312e81 100%);
        padding: 2.5rem;
        border-radius: 16px;
        margin-bottom: 2rem;
        border: 1px solid rgba(255, 255, 255, 0.1);
        box-shadow: 0 10px 25px -5px rgba(0, 0, 0, 0.3);
    }
    .hero-title {
        font-size: 2.5rem;
        font-weight: 800;
        color: #ffffff;
        margin-bottom: 0.5rem;
    }
    .hero-subtitle {
        font-size: 1.2rem;
        color: #a5b4fc;
        margin-bottom: 1rem;
    }
    .hero-description {
        font-size: 1rem;
        color: #cbd5e1;
        line-height: 1.6;
    }

    /* Tarjetas de aplicaciones */
    .app-card {
        background-color: #1e293b;
        border: 1px solid #334155;
        padding: 1.5rem;
        border-radius: 12px;
        margin-bottom: 1.5rem;
        transition: transform 0.2s ease, box-shadow 0.2s ease;
        height: 100%;
        display: flex;
        flex-direction: column;
        justify-content: space-between;
    }
    .app-card:hover {
        transform: translateY(-4px);
        box-shadow: 0 12px 20px -10px rgba(99, 102, 241, 0.3);
        border-color: #6366f1;
    }
    .app-title {
        font-size: 1.15rem;
        font-weight: 700;
        color: #f8fafc;
        margin-bottom: 0.75rem;
    }
    .app-desc {
        font-size: 0.9rem;
        color: #94a3b8;
        margin-bottom: 1rem;
    }
    
    /* Botones y Enlaces personalizados */
    .stLinkButton > a {
        background-color: #4f46e5 !important;
        color: white !important;
        border-radius: 8px !important;
        padding: 0.5rem 1rem !important;
        font-weight: 600 !important;
        text-align: center !important;
        width: 100% !important;
        border: none !important;
    }
    .stLinkButton > a:hover {
        background-color: #4338ca !important;
    }
    
    /* Sidebar */
    [data-testid="stSidebar"] {
        background-color: #0b0f19;
        border-right: 1px solid #1e293b;
    }
    </style>
""", unsafe_allow_html=True)

# --- SECCIÓN HERO / PRESENTACIÓN PERSONAL ---
st.markdown("""
    <div class="hero-container">
        <div class="hero-title">Portafolio de Herramientas Digitales e IA</div>
        <div class="hero-subtitle">Santiago Medina López | Estudiante de Diseño Interactivo (6to Semestre)</div>
        <div class="hero-description">
            Esta plataforma interactiva reúne una serie de aplicaciones creativas impulsadas por Inteligencia Artificial, 
            integrando tecnologías avanzadas como OCR, motores de traducción en tiempo real, análisis avanzados de texto, 
            procesamiento multimodal y sistemas ciberfísicos. Explora cada módulo desplegado a continuación.
        </div>
    </div>
""", unsafe_allow_html=True)

# --- SIDEBAR ---
with st.sidebar:
    st.subheader("💡 Sobre el Portafolio")
    st.write(
        "La inteligencia artificial permite mejorar la toma de decisiones con el uso de datos, "
        "automatizar tareas rutinarias y proporcionar análisis avanzados en tiempo real, lo que "
        "resulta en una mayor eficiencia y precisión en diversos campos creativos y técnicos."
    )
    st.markdown("---")
    st.subheader("🔗 Enlaces Externos")
    url_ia = "https://sites.google.com/view/aplicacionesdeia/inicio"
    st.write(f"Encuentra más páginas y ejercicios prácticos en el [sitio web oficial]({url_ia}).")

# --- CONTENEDORES DE LAS 10 HERRAMIENTAS EN 3 COLUMNAS ---
col1, col2, col3 = st.columns(3)

# Definimos las herramientas con sus respectivos títulos, descripciones y URLs (conservando las originales)
herramientas = [
    {
        "titulo": "Creador de Ondas Binaurales",
        "desc": "Generación de frecuencias y audio inmersivo enfocado en la estimulación creativa y la concentración.",
        "img": "txt_to_audio2.png",
        "url": "https://imultimod.streamlit.app/",
        "col": col1
    },
    {
        "titulo": "Traductor de Emergencias para Turistas",
        "desc": "Sistema ágil de traducción asistida por IA diseñado para solventar barreras lingüísticas críticas en ruta.",
        "img": "OIG8.jpg",
        "url": "https://traductorw.streamlit.app/",
        "col": col2
    },
    {
        "titulo": "Lector de Etiquetas de Supermercado",
        "desc": "Aplicación basada en OCR para extraer, procesar y evaluar componentes e información nutricional de productos.",
        "img": "Chat_pdf.png",
        "url": "https://chatpdf-cc.streamlit.app/",
        "col": col3
    },
    {
        "titulo": "Radar de Reseñas",
        "desc": "Clasificación y análisis automatizado de opiniones públicas para la extracción de métricas de satisfacción.",
        "img": "txt_to_audio.png",
        "url": "https://yolov5cmc.streamlit.app/",
        "col": col1
    },
    {
        "titulo": "Análisis Emocional de Textos",
        "desc": "Procesamiento de lenguaje natural (PLN) para detectar tonos, sentimientos y matices psicológicos en escritos.",
        "img": "data_analisis.png",
        "url": "https://dataagente.streamlit.app/",
        "col": col2
    },
    {
        "titulo": "Inventario de Mudanzas",
        "desc": "Organización y catalogación inteligente de objetos mediante visión computacional y conteo automatizado.",
        "img": "OIG4.jpg",
        "url": "https://vision2-gpt4o.streamlit.app/",
        "col": col3
    },
    {
        "titulo": "TF-IDF",
        "desc": "Algoritmo estadístico para evaluar la importancia y relevancia de términos dentro de un corpus documental.",
        "img": "OIG5.jpg",
        "url": "https://xn3pg24ztuv6fdiqon8qn3.streamlit.app/",
        "col": col1
    },
    {
        "titulo": "Analizador de PDFs Lexiscan",
        "desc": "Extracción inteligente de conocimiento y consultas conversacionales directas sobre documentos legales o extensos.",
        "img": "OIG3.jpg",
        "url": "https://transcript-whisper.streamlit.app/",
        "col": col2
    },
    {
        "titulo": "Crítico de Arte por Imágenes",
        "desc": "Evaluación estética y conceptual de piezas gráficas mediante análisis visual avanzado de alta precisión.",
        "img": "OIG6.jpg",
        "url": "https://vision2-gpt4o.streamlit.app/",
        "col": col3
    },
    {
        "titulo": "Aplicación Intro",
        "desc": "Módulo introductorio y de visión general sobre el ecosistema de experiencias y herramientas interactivas.",
        "img": "txt_to_audio2.png",
        "url": "https://imultimod.streamlit.app/",
        "col": col1
    }
]

# Renderizado dinámico de las tarjetas asegurando el diseño en columnas
for h in herramientas:
    with h["col"]:
        with st.container():
            st.markdown(f"""
                <div class="app-card">
                    <div>
                        <div class="app-title">{h["titulo"]}</div>
                        <div class="app-desc">{h["desc"]}</div>
                    </div>
            """, unsafe_allow_html=True)
            
            # Intentar cargar la imagen de manera segura
            try:
                image = Image.open(h["img"])
                st.image(image, use_container_width=True)
            except Exception:
                st.info("🖼️ [Vista previa de herramienta]")
                
            st.link_button("🚀 Abrir Aplicación", h["url"])
            st.markdown("</div>", unsafe_allow_html=True)
