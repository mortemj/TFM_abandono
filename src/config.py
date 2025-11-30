# =============================================================================
# TFM Abandono Universitario - Configuración de Rutas
# =============================================================================
# Este módulo detecta automáticamente el entorno y configura las rutas
# Funciona en: Local, Google Colab, Kaggle, GitHub Actions
# =============================================================================

from pathlib import Path
import os

def detectar_entorno():
    """Detecta en qué entorno se está ejecutando"""
    if os.environ.get('COLAB_GPU') or os.path.exists('/content'):
        return 'colab'
    elif os.path.exists('/kaggle'):
        return 'kaggle'
    elif os.environ.get('GITHUB_ACTIONS'):
        return 'github'
    else:
        return 'local'

def encontrar_raiz_proyecto():
    """Encuentra la raíz del proyecto buscando README.md"""
    entorno = detectar_entorno()
    
    if entorno == 'colab':
        # En Colab, asumimos que se clona en /content/TFM_abandono
        posibles = [
            Path('/content/TFM_abandono'),
            Path('/content/drive/MyDrive/TFM_abandono'),
        ]
        for p in posibles:
            if p.exists():
                return p
        return Path('/content/TFM_abandono')
    
    elif entorno == 'kaggle':
        return Path('/kaggle/working/TFM_abandono')
    
    elif entorno == 'github':
        return Path(os.environ.get('GITHUB_WORKSPACE', '.'))
    
    else:  # local
        # Buscar hacia arriba desde el directorio actual
        current = Path.cwd()
        for parent in [current] + list(current.parents):
            if (parent / 'README.md').exists() and (parent / 'data').exists():
                return parent
        # Si no encuentra, asumir estructura típica desde notebooks/
        if 'notebooks' in str(current):
            return current.parent
        return current

# =============================================================================
# RUTAS PRINCIPALES
# =============================================================================

ENTORNO = detectar_entorno()
ROOT = encontrar_raiz_proyecto()
DATA_RAW = ROOT / 'data' / '01_raw'
DATA_INTERIM = ROOT / 'data' / '02_interim'
DATA_PROCESSED = ROOT / 'data' / '03_processed'
DOCS = ROOT / 'docs'
NOTEBOOKS = ROOT / 'notebooks'

# =============================================================================
# FUNCIONES AUXILIARES
# =============================================================================

def crear_estructura():
    """Crea las carpetas necesarias si no existen"""
    for carpeta in [DATA_RAW, DATA_INTERIM, DATA_PROCESSED, DOCS, NOTEBOOKS]:
        carpeta.mkdir(parents=True, exist_ok=True)
    print(f"✅ Estructura creada en: {ROOT}")

def validar_estructura():
    """Valida que la estructura existe"""
    carpetas = [DATA_RAW, DATA_INTERIM, DATA_PROCESSED, DOCS, NOTEBOOKS]
    todas_existen = all(c.exists() for c in carpetas)
    if todas_existen:
        print("✅ Estructura de carpetas OK")
    else:
        print("❌ Faltan carpetas. Ejecuta crear_estructura()")
    return todas_existen

def validar_ficheros_raw():
    """Valida que los ficheros Excel están en data/01_raw"""
    ficheros = [
        DATA_RAW / 'preinscripcion_si.xlsx',
        DATA_RAW / 'datos_proyecto_sin_preinscrip.xlsx'
    ]
    for f in ficheros:
        if f.exists():
            print(f"✅ {f.name}")
        else:
            print(f"❌ Falta: {f.name}")
    return all(f.exists() for f in ficheros)

def info_entorno():
    """Muestra información del entorno actual"""
    print("="*50)
    print("INFORMACIÓN DEL ENTORNO")
    print("="*50)
    print(f"Entorno: {ENTORNO}")
    print(f"Raíz proyecto: {ROOT}")
    print(f"Data RAW: {DATA_RAW}")
    print(f"Data INTERIM: {DATA_INTERIM}")
    print(f"Data PROCESSED: {DATA_PROCESSED}")
    print(f"Docs: {DOCS}")
    print("="*50)

# Mostrar info al importar
if __name__ == '__main__':
    info_entorno()
