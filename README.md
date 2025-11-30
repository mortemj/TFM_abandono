# 🎓 TFM: Predicción de Abandono Universitario

## Descripción

Proyecto de Trabajo Fin de Máster para predecir el abandono universitario utilizando técnicas de Machine Learning y Explicabilidad (XAI).

**Autora:** María José Morte (morte@uji.es)  
**GitHub:** mortemj

---

## 🚀 Inicio Rápido

### 1. Copiar los datos
Copia tus ficheros Excel a la carpeta `data/01_raw/`:
- `preinscripcion_si.xlsx`
- `datos_proyecto_sin_preinscrip.xlsx`

### 2. Instalar dependencias
```bash
pip install -r requirements.txt
```

### 3. Ejecutar notebooks en orden
```
1️⃣ notebooks/01_limpieza_datos.ipynb
2️⃣ notebooks/02_genera_reportes_sweetviz_dinamico.ipynb
3️⃣ notebooks/03_union_dataset_dinamico.ipynb
```

### 4. Ver resultados
Abre `docs/transformaciones_dinamico.html` en tu navegador.

---

## 📁 Estructura del Proyecto

```
TFM_abandono/
├── data/
│   ├── 01_raw/           ← Excel originales (copiar aquí)
│   ├── 02_interim/       ← Tablas limpias (.parquet)
│   └── 03_processed/     ← Dataset final (df_alumno)
├── docs/                 ← HTML interactivos (se generan automáticamente)
├── notebooks/            ← Jupyter notebooks
├── src/                  ← Código Python auxiliar
├── README.md
└── requirements.txt
```

---

## 🔄 Flujo de Ejecución

```
Excel originales
      ↓
01_limpieza_datos.ipynb
      ↓ Genera: 9 tablas .parquet
      ↓
02_genera_reportes_sweetviz_dinamico.ipynb
      ↓ Genera: reportes HTML + transformaciones_dinamico.html
      ↓
03_union_dataset_dinamico.ipynb
      ↓ Genera: df_alumno.parquet + reporte_df_alumno.html
      ↓
Dataset listo para EDA y modelado
```

---

## 🌐 Compatibilidad

| Entorno | Estado |
|---------|--------|
| Local (Jupyter/Anaconda) | ✅ |
| Google Colab | ✅ |
| Kaggle | ✅ |
| GitHub Actions | ✅ |

---

## 📊 Fases del Proyecto

| Fase | Descripción | Estado |
|------|-------------|--------|
| 1 | Limpieza de datos | ✅ |
| 2 | EDA (Análisis Exploratorio) | ⏳ |
| 3 | Feature Engineering | ⏳ |
| 4 | Modelado (ML) | ⏳ |
| 5 | Explicabilidad (XAI) | ⏳ |
| 6 | Dashboard | ⏳ |

---

## 📝 Licencia

Proyecto académico - UJI 2024
