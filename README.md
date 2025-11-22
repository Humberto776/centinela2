
# Proyecto Centinela

Plataforma contenerizada para análisis de desinformación y OSINT con pipeline **DevSecOps** completo.

## 📌 Introducción
Este proyecto implementa una arquitectura de microservicios y un pipeline CI/CD/CS sobre **GitHub Actions**, integrando seguridad en cada fase del ciclo de vida (Shift-Left Security).

## ✅ Objetivos
- Desarrollar una aplicación contenerizada (Gateway, Backend, Scraper, Analyzer, Publisher).
- Automatizar CI/CD con pruebas y escaneos de seguridad (SAST, DAST, IaC, contenedores).
- Desplegar en Kubernetes (k3s) con IaC y monitoreo.

---

## 🏗 Arquitectura
docs/arquitectura.png

**Componentes:**
- **Gateway (FastAPI)**: API principal.
- **Backend (FastAPI)**: lógica interna.
- **Scraper**: extracción de contenido.
- **Analyzer**: análisis de sentimiento.
- **Publisher**: publicación en redes.
- **PostgreSQL**: base de datos.
- **RabbitMQ**: mensajería asíncrona.

---

## 🔐 Pipeline DevSecOps
docs/pipeline.png

**Fases y herramientas:**
- **SAST**: Bandit, Semgrep.
- **Secret scanning**: Gitleaks.
- **Container scan**: Trivy.
- **IaC scan**: Checkov, tfsec.
- **DAST**: OWASP ZAP.
- **Runtime Security**: Falco.
- **Monitoreo**: PLG (Promtail, Loki, Grafana).

Workflow: `.github/workflows/devsecops.yml`.

---

## ▶️ Ejecución local
```bash
docker compose up -d --build
curl http://localhost:8000/health
