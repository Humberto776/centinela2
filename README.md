
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
----

name: DevSecOps CI/CD/CS

on:
  push:
    branches: ["main", "master"]
  pull_request:
  workflow_dispatch:

permissions:
  contents: read
  actions: read
  security-events: write   # necesario para subir SARIF al panel "Security"

jobs:

  # -----------------------------
  # Build + Unit tests + SAST
  # -----------------------------
  build_test_sast:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout repo
        uses: actions/checkout@v4

      - name: Setup Python
        uses: actions/setup-python@v5
        with:
          python-version: "3.11"

      - name: Install test deps
        run: |
          pip install fastapi uvicorn pytest bandit
          # Ajusta dependencias según tu proyecto
      - name: Unit tests (pytest)
        run: |
          if [ -d "backend" ]; then
            pip install -r backend/requirements.txt || true
            pytest -q backend || true
          else
            echo "No backend/ folder. Skipping unit tests."
          fi

      - name: SAST - Bandit (Python)
        run: bandit -r . || true

      - name: SAST - Semgrep (p/default)
        uses: returntocorp/semgrep-action@v1
        with:
          config: p/default   # reglas por defecto
        # Docs: https://semgrep.dev/docs/semgrep-ci/sample-ci-configs

  # -----------------------------
  # Secret Scanning (Gitleaks)
  # -----------------------------
  secrets_gitleaks:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout repo (full history)
        uses: actions/checkout@v4
        with:
          fetch-depth: 0
      - name: Gitleaks scan
        uses: gitleaks/gitleaks-action@v2
        env:
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
        # README acción: https://github.com/gitleaks/gitleaks-action
      - name: Upload Gitleaks report (artifact)
        if: always()
        run: |
          # La acción de Gitleaks genera logs/outputs en el job.
          # Si quieres report JSON local, puedes añadir:
          gitleaks detect --source . --report-format json --report-path gitleaks_report.json || true
