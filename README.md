# Despliegue de Modelo
Este proyecto despliega un modelo de clasificación de riesgos como una API utilizando **FastAPI** y **Vercel**. La API permite predecir si un cliente es de "alto riesgo" (`bad risk`) o "bajo riesgo" (`good risk`) basado en una descripción y otros datos numéricos.

## Estructura del Proyecto

```
project-folder/
├── api/
│   ├── predict.py    
├── models/
│   ├── optimized_risk_classifier_model.pkl  
│   ├── optimized_tfidf_vectorizer.pkl    
├── requirements.txt 
├── vercel.json  
```

### Archivos Principales

1. **`api/predict.py`**: Contiene la implementación de la API utilizando FastAPI.
2. **`models/`**: Carpeta que almacena el modelo entrenado y el vectorizador TF-IDF.
3. **`requirements.txt`**: Lista de dependencias necesarias para ejecutar la API.
4. **`vercel.json`**: Configuración para desplegar el proyecto en Vercel.

---

## Configuración del Entorno

1. **Instalar dependencias:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Iniciar servidor localmente:**
   Usa `uvicorn` para probar la API localmente:
   ```bash
   uvicorn api.predict:app --reload
   ```
   La API estará disponible en `http://127.0.0.1:8000`.

3. **Prueba de la API:**
   Envíe una solicitud POST al endpoint `/predict`:
   ```bash
   curl -X POST http://127.0.0.1:8000/predict \
   -H "Content-Type: application/json" \
   -d '{
     "description": "Descripción del cliente",
     "age": 30,
     "credit_amount": 5000,
     "duration": 12,
     "job": 2,
     "saving_account": "little",
     "checking_account": "moderate",
     "purpose": "car"
   }'
   ```

---

## Despliegue en Vercel

1. **Instalar Vercel CLI:**
   ```bash
   npm install -g vercel
   ```

2. **Iniciar sesión en Vercel:**
   ```bash
   vercel login
   ```

3. **Desplegar el proyecto:**
   ```bash
   vercel
   ```

4. **Prueba en Producción:**
   Envía una solicitud POST al endpoint desplegado:
   ```bash
   curl -X POST https://<tu-api-vercel>.vercel.app/api/predict \
   -H "Content-Type: application/json" \
   -d '{
     "description": "Descripción del cliente",
     "age": 30,
     "credit_amount": 5000,
     "duration": 12,
     "job": 2,
     "saving_account": "little",
     "checking_account": "moderate",
     "purpose": "car"
   }'
   ```
---

## Licencia
Este proyecto es de uso libre y abierto para fines educativos y de desarrollo.
