---
# Scan vulneravilidades
alwaysApply: true
always_on: true
trigger: always_on
applyTo: "**"
description: Snyk Security At Inception
---

# Project security best practices

- Always run snyk_code_scan tool for new first party code that is generated in a Snyk-supported language.
- If any security issues are found based on newly introduced or modified code or dependencies, attempt to fix the issues using the results context from Snyk.
- Rescan the code after fixing the issues to ensure that the issues were fixed and that there are no newly introduced issues.
- Repeat this process until no new issues are found.
# PROYECTO CENTINELA
# Autor: Hummberto Ramirez Pinzon

## 📌 Introducción
En el panorama digital actual, la desinformación y la manipulación en redes sociales representan amenazas significativas. Este proyecto propone la creación de una plataforma funcional llamada **Proyecto Centinela**, diseñada para:
- Combatir noticias falsas mediante web scraping y contrastación de fuentes.
- Evaluar el impacto de campañas de información/desinformación.
- Gestionar la publicación de contenido verificado en múltiples plataformas.



---

## ✅ Objetivos
- Diseñar e implementar un pipeline CI/CD/CS que integre seguridad en cada fase.
- Desarrollar la aplicación Centinela con scraping, análisis y publicación.
- Contenerizar todos los componentes (Frontend, Backend, DB, Workers).
- Integrar herramientas de seguridad en cada etapa (Shift-Left Security).
- Desplegar en Kubernetes (k3s) con IaC.
- Establecer monitoreo y seguridad en tiempo real.

---

## 🏗 Arquitectura

# PROYECTO CENTINELA

## 📌 Introducción
En el panorama digital actual, la desinformación y la manipulación en redes sociales representan amenazas significativas. Este proyecto propone la creación de una plataforma funcional llamada **Proyecto Centinela**, diseñada para:
- Combatir noticias falsas mediante web scraping y contrastación de fuentes.
- Evaluar el impacto de campañas de información/desinformación.
- Gestionar la publicación de contenido verificado en múltiples plataformas.

El verdadero desafío es **construir, asegurar y automatizar el ciclo de vida completo de la aplicación** utilizando herramientas FOSS y un enfoque 100% contenerizado, aplicando principios DevSecOps.

---

## ✅ Objetivos
- Diseñar e implementar un pipeline CI/CD/CS que integre seguridad en cada fase.
- Desarrollar la aplicación Centinela con scraping, análisis y publicación.
- Contenerizar todos los componentes (Frontend, Backend, DB, Workers).
- Integrar herramientas de seguridad en cada etapa (Shift-Left Security).
- Desplegar en Kubernetes (k3s) con IaC.
- Establecer monitoreo y seguridad en tiempo real.

---

## 🏗 Arquitectura

docs/arquitectura.png

### Tabla de Componentes
| Componente    | Tecnología       | Función                                      |
|---------------|-----------------|---------------------------------------------|
| **Frontend**  | Vue.js / React | Interfaz de usuario (SPA)                  |
| **Gateway**   | FastAPI        | API principal y orquestación               |
| **Backend**   | FastAPI        | Lógica interna y procesamiento             |
| **Scraper**   | Python + BS4   | Extracción de contenido web                |
| **Analyzer**  | Python + NLTK  | Análisis de sentimiento y texto            |
| **Publisher** | Python         | Publicación en redes sociales              |
| **DB**        | PostgreSQL     | Almacenamiento de datos                    |
| **Broker**    | RabbitMQ       | Comunicación asíncrona entre servicios     |

---


**Componentes:**
- **Frontend:** SPA en Vue.js o React.
- **Gateway:** API principal (FastAPI).
- **Scraper:** Worker para extracción de contenido.
- **Analyzer:** Microservicio NLP (NLTK).
- **Publisher:** Publicación en APIs sociales.
- **Base de Datos:** PostgreSQL.
- **Broker:** RabbitMQ para comunicación asíncrona.


## 🔐 Pipeline DevSecOps
docs/pipeline.png

**Fases y herramientas:**
- **Planificación:** OWASP Threat Dragon (modelado de amenazas).
- **Code:** Semgrep, Bandit, Gitleaks.
- **Build:** Docker + Trivy.
- **Test:** Pytest + OWASP ZAP (DAST).
- **Release/Deploy:** Terraform + Checkov/tfsec + k3s.
- **Operate/Monitor:** Grafana, Loki, Promtail, Falco.

Workflow: `.github/workflows/devsecops.yml`.

**Archivo principal:** `.github/workflows/ci-cd.yml`  
Integra seguridad en cada fase del ciclo de vida del software.

docs/arquitectura.png  
docs/pipeline.png  
![Reporte ZAP](docs/vulnerabilidad.png) <!-- Usa la imagen que subiste Fases del Pipeline

### 🔹 Fase 1: **Plan**
- **Modelado de amenazas:** OWASP Threat Dragon, STRIDE

### 🔹 Fase 2: **Code (Seguridad Estática)**
- **Pre-commit Hooks:**
  - `gitleaks` → Detecta secretos y claves API
  - `black` → Formato Python consistente
  - `fix-end-of-files` / `trailing-whitespace` → Limpieza de código
- **SAST (Análisis Estático):**
  - `flake8` → Errores y estilo
  - `bandit` → Vulnerabilidades comunes en Python
  - `semgrep` → Patrones de código complejos
- **SCA (Dependencias):** `trivy fs` → Detecta CVEs
- **IaC Scan:** `checkov` → Escaneo de Terraform

### 🔹 Fase 3: **Build (Seguridad de Imágenes)**
- **Construcción:** Docker de los microservicios
- **Escaneo:** `trivy image` detecta HIGH/CRITICAL y bloquea el pipeline
- **Registro Temporal:** GHCR (GitHub Container Registry) con la `run_id`

### 🔹 Fase 4: **Test (Seguridad Dinámica)**
- **Unit & Smoke Tests:** `pytest` para API y frontend
- **DAST:** OWASP ZAP analiza frontend (`http://frontend:80`)
- **Quality Gates:** Falla el pipeline si:
  - `pytest` falla
  - `trivy` detecta CVEs críticos
  - ZAP detecta vulnerabilidades críticas

### 🔹 Fase 5 y 6: **Release, Deploy y Monitor**
- **Publicación:** Imágenes validadas en:
  - GitHub Container Registry (GHCR) con tag `:latest`
  - Docker Hub con tag `:latest`
- **Deploy (Simulado):** Job `deploy-to-production` simula conexión SSH a VPS y actualización con:
  ```bash
  docker compose pull
  docker compose up -d


---

## ▶️ Ejecución local
```bash
docker compose up -d --build
curl http://localhost:8000/health
curl http://localhost:8000/docs
curl http://localhost:8000







