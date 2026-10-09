import streamlit as st
from PIL import Image

# Configuración de la página
st.set_page_config(
    page_title="Portafolio Creativo | Santiago Medina",
    page_icon="✨",
    layout="wide"
)

# Estilos CSS avanzados (Glassmorphism y diseño futurista)
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800&display=swap');

    /* Aplicar fuente global */
    html, body, [class*="css"] {
        font-family: 'Plus Jakarta Sans', sans-serif;
    }

    .main {
        background: radial-gradient(circle at 10% 20%, #090d16 0%, #030712 90%);
        color: #f1f5f9;
    }
    
    /* Banner Principal (Hero) */
    .hero-box {
        background: linear-gradient(135deg, rgba(79, 70, 229, 0.15) 0%, rgba(147, 51, 234, 0.15) 100%);
        backdrop-filter: blur(12px);
        -webkit-backdrop-filter: blur(12px);
        border: 1px solid rgba(255, 255, 255, 0.12);
        padding: 3rem 2.5rem;
        border-radius: 24px;
        margin-bottom: 2.5rem;
        box-shadow: 0 20px 40px -15px rgba(0, 0, 0, 0.5);
        position: relative;
        overflow: hidden;
    }
    .hero-box::before {
        content: '';
        position: absolute;
        top: -50px;
        right: -50px;
        width: 200px;
        height: 200px;
        background: rgba(99, 102, 241, 0.2);
        border-radius: 50%;
        filter: blur(60px);
    }
    .hero-tag {
        display: inline-block;
        background: linear-gradient(90deg, #6366f1, #a855f7);
        color: white;
        padding: 0.35rem 1rem;
        border-radius: 50px;
        font-size: 0.8rem;
        font-weight: 700;
        text-transform: uppercase;
        letter-spacing: 1px;
        margin-bottom: 1rem;
    }
    .hero-title {
        font-size: 2.8rem;
        font-weight: 800;
        color: #ffffff;
        margin-bottom: 0.5rem;
        letter-spacing: -0.5px;
    }
    .hero-subtitle {
        font-size: 1.25rem;
        color: #c084fc;
        font-weight: 600;
        margin-bottom: 1rem;
    }
    .hero-text {
        font-size: 1.05rem;
        color: #94a3b8;
        line-height: 1.7;
        max-width: 900px;
    }

    /* Tarjetas de herramientas (Glass Cards) */
    .tool-card {
        background: rgba(30, 41, 59, 0.6);
        backdrop-filter: blur(8px);
        border: 1px solid rgba(255, 255, 255, 0.08);
        padding: 1.8rem;
        border-radius: 18px;
        margin-bottom: 1.8rem;
        transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
        height: 100%;
        display: flex;
        flex-direction: column;
        justify-content: space-between;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
    }
    .tool-card:hover {
        transform: translateY(-6px);
        border-color: rgba(168, 85, 247, 0.4);
        box-shadow: 0 20px 30px -10px rgba(147, 51, 234, 0.2);
        background: rgba(30, 41, 59, 0.8);
    }
    .tool-title {
        font-size: 1.25rem;
        font-weight: 700;
        color: #f8fafc;
        margin-bottom: 0.6rem;
    }
    .tool-desc {
        font-size: 0.92rem;
        color: #94a3b8;
        margin-bottom: 1.2rem;
        line-height: 1.5;
    }

    /* Botón personalizado Streamlit */
    .stLinkButton > a {
        background: linear-gradient(135deg, #4f46e5 0%, #7c3aed 100%) !important;
        color: white !important;
        border-radius: 10px !important;
        padding: 0.6rem 1.2rem !important;
        font-weight: 600 !important;
        text-align: center !important;
        width: 100% !important;
        border: none !important;
        box-shadow: 0 4px 12px rgba(79, 70, 229, 0.3) !important;
        transition: all 0.2s ease !important;
    }
    .stLinkButton > a:hover {
        opacity: 0.9 !important;
        box-shadow: 0 6px 16px rgba(124, 58, 237, 0.5) !important;
        transform: scale(1.02);
    }

    /* Sidebar Estilizado */
    [data-testid="stSidebar"] {
        background-color: #050811;
        border-right: 1px solid rgba(255, 255, 255, 0.05);
    }
    </style>
""", unsafe_allow_html=True)

# --- BANNER / PRESENTACIÓN PERSONAL ---
st.markdown("""
    <div class="hero-box">
        <div class="hero-tag">Portafolio Interactivo</div>
        <div class="hero-title">Laboratorio de Inteligencia Artificial & Apps Creativas</div>
        <div class="hero-subtitle">Santiago Medina López &bull; Estudiante de Diseño Interactivo (6to Semestre)</div>
        <div class="hero-text">
            Bienvenido a este espacio experimental donde convergen la tecnología y el diseño. Esta serie de aplicaciones 
            creativas integra herramientas avanzadas como reconocimiento óptico de caracteres (OCR), motores de traducción multilingüe, 
            sistemas de análisis semántico de textos con IA y experiencias interactivas diseñadas para potenciar procesos creativos y técnicos.
        </div>
    </div>
""", unsafe_allow_html=True)

# --- SIDEBAR CON TEXTOS NUEVOS ---
with st.sidebar:
    st.markdown("### ⚡ Panel de Navegación")
    st.write(
        "Este portafolio recopila prototipos funcionales desarrollados para explorar el potencial "
        "de los modelos de lenguaje, la visión computacional y los sistemas cognitivos aplicados a la resolución de problemas."
    )
    st.markdown("---")
    st.markdown("### 🎯 Recursos y Enlaces")
    url_ia = "https://sites.google.com/view/aplicacionesdeia/inicio"
    st.write(f"Explora documentación complementaria, guías conceptuales y ejercicios prácticos en el [Sitio Oficial de Prácticas]({url_ia}).")
    st.markdown("---")
    st.caption("© 2026 • Diseñado y programado por Santiago Medina.")

# --- DISTRIBUCIÓN DE LAS 10 HERRAMIENTAS EN 3 COLUMNAS ---
col1, col2, col3 = st.columns(3)

herramientas = [
    {
        "titulo": "Creador de Ondas Binaurales",
        "desc": "Generación de frecuencias sonoras y audio inmersivo enfocado en la estimulación creativa y la concentración profunda.",
        "img": "1.jpg",
        "url": "https://imultimod.streamlit.app/",
        "col": col1
    },
    {
        "titulo": "Traductor de Emergencias para Turistas",
        "desc": "Sistema ágil de traducción asistida por IA diseñado para solventar barreras lingüísticas críticas en entornos dinámicos.",
        "img": "2.jpg",
        "url": "https://traductorw.streamlit.app/",
        "col": col2
    },
    {
        "titulo": "Lector de Etiquetas de Supermercado",
        "desc": "Aplicación basada en OCR para extraer, interpretar y evaluar componentes, textos e información nutricional de productos.",
        "img": "3.jpeg",
        "url": "https://chatpdf-cc.streamlit.app/",
        "col": col3
    },
    {
        "titulo": "Radar de Reseñas",
        "desc": "Clasificación inteligente y análisis automatizado de opiniones públicas para la extracción de métricas de satisfacción.",
        "img": "4.jpeg",
        "url": "https://yolov5cmc.streamlit.app/",
        "col": col1
    },
    {
        "titulo": "Análisis Emocional de Textos",
        "desc": "Procesamiento de Lenguaje Natural (PLN) para detectar matices psicológicos, tonos y sentimientos profundos en escritos.",
        "img": "5.jpeg",
        "url": "https://dataagente.streamlit.app/",
        "col": col2
    },
    {
        "titulo": "Inventario de Mudanzas",
        "desc": "Organización y catalogación inteligente de objetos mediante visión computacional y conteo automatizado por IA.",
        "img": "6.jpeg",
        "url": "https://vision2-gpt4o.streamlit.app/",
        "col": col3
    },
    {
        "titulo": "TF-IDF",
        "desc": "Algoritmo estadístico avanzado para evaluar el peso, la importancia y la relevancia de términos dentro de un corpus documental.",
        "img": "7.jpg",
        "url": "https://xn3pg24ztuv6fdiqon8qn3.streamlit.app/",
        "col": col1
    },
    {
        "titulo": "Analizador de PDFs Lexiscan",
        "desc": "Extracción inteligente de conocimiento y consultas conversacionales directas orientadas a documentos legales y extensos.",
        "img": "8.jpeg",
        "url": "https://transcript-whisper.streamlit.app/",
        "col": col2
    },
    {
        "titulo": "Crítico de Arte por Imágenes",
        "desc": "Evaluación estética, compositiva y conceptual de piezas gráficas mediante modelos visuales de alta precisión.",
        "img": "9.jpeg",
        "url": "https://vision2-gpt4o.streamlit.app/",
        "col": col3
    },
    {
        "titulo": "Aplicación Intro",
        "desc": "Mi primera app, donde comenzó todo...",
        "img": "10.jpeg",
        "url": "https://imultimod.streamlit.app/",
        "col": col1
    }
]

# Renderizado dinámico de las tarjetas manteniendo la estructura visual
for h in herramientas:
    with h["col"]:
        with st.container():
            st.markdown(f"""
                <div class="tool-card">
                    <div>
                        <div class="tool-title">{h["titulo"]}</div>
                        <div class="tool-desc">{h["desc"]}</div>
                    </div>
            """, unsafe_allow_html=True)
            
            try:
                image = Image.open(h["img"])
                st.image(image, use_container_width=True)
            except Exception:
                st.info("🖼️ [Vista previa no disponible]")
                
            st.link_button("🚀 Abrir Aplicación", h["url"])
            st.markdown("</div>", unsafe_allow_html=True)
