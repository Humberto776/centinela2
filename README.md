
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

---

## ▶️ Ejecución local
```bash
docker compose up -d --build
curl http://localhost:8000/health
curl http://localhost:8000/docs
curl http://localhost:8000


---

🔹 Fase 1: Plan
        🔹Modelado de amenazas:** OWASP Threat Dragon, STRIDE

🔹 Fase 2: Code (Seguridad Estática)

        🔹 Pre-commit Hooks:**
        🔹gitleaks` → Detecta secretos y claves API
       🔹black` → Formato Python consistente
       🔹fix-end-of-files` / `trailing-whitespace` → Limpieza de código

    🔹SAST (Análisis Estático):

        🔹flake8` → Errores y estilo
        🔹bandit` → Vulnerabilidades comunes en Python
        🔹semgrep` → Patrones de código complejos
        🔹SCA (Dependencias):** `trivy fs` → Detecta CVEs
        🔹IaC Scan:** `checkov` → Escaneo de Terraform

🔹 Fase 3: Build (Seguridad de Imágenes)

    🔹Escaneo:** `trivy image` detecta HIGH/CRITICAL y bloquea el pipelineConstrucción:** Docker de los 3 microservicios
    🔹Escaneo:** `trivy image` detecta HIGH/CRITICAL y bloquea el pipeline
    🔹Registro Temporal:** GHCR (GitHub Container Registry) con la `run_id`

🔹 Fase 4: Test (Seguridad Dinámica)

  🔹Unit & Smoke Tests:** `pytest` para API y frontend
  🔹DAST:** OWASP ZAP analiza frontend (`http://frontend:80`)
  🔹Quality Gates:** Falla el pipeline si:
     🔹pytest` falla
      🔹trivy` detecta CVEs críticos
      🔹ZAP detecta vulnerabilidades críticas

🔹 Fase 5 & 6: Release, Deploy & Monitor}

  🔹Publicación:** Las imágenes validadas se publican en:
  🔹 GitHub Container Registry (GHCR) con tag `:latest`
  🔹 Docker Hub con tag `:latest`
  🔹Deploy (Simulado):** Job `deploy-to-production` simula la conexión SSH a un VPS y la actualización con `docker compose pull` y `docker compose up -d`.
  🔹Monitoreo:** Opcional, Falco (seguridad runtime) + stack PLG (Promtail, Loki, Grafana) para logs.

---



