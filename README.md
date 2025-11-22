
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

**Componentes:**
- **Frontend:** SPA en Vue.js o React.
- **Gateway:** API principal (FastAPI).
- **Scraper:** Worker para extracción de contenido.
- **Analyzer:** Microservicio NLP (NLTK).
- **Publisher:** Publicación en APIs sociales.
- **Base de Datos:** PostgreSQL.
- **Broker:** RabbitMQ para comunicación asíncrona.

---

## 🔐 Pipeline DevSecOps
![Pipeline](docs/pipeline.pngherramientas:**
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
curl [http://localhost:8000/docs]
curl [http://localhost:8000]
