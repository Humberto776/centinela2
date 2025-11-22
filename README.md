Introducción


Este documento describe la implementación del Proyecto Centinela con enfoque DevSecOps, integrando seguridad en cada fase del ciclo de vida mediante herramientas FOSS y despliegue contenerizado

Arquitectura


Arquitectura basada en microservicios: Gateway, Backend, Scraper, Analyzer, Publisher, DB y RabbitMQ. Todos contenerizados con Docker y orquestados con Kubernetes (k3s).
 
 
 Pipeline DevSecOps
 
Pipeline CI/CD/CS con fases Code → Build → Test → Deploy → Monitor, integrando SAST, secret scanning, análisis de contenedores, IaC y DAST.
 
Modelado de Amenazas

Se utilizó OWASP Threat Dragon para generar DFDs y aplicar STRIDE. Amenazas: Spoofing, Tampering, Information Disclosure, DoS y Elevation of Privilege. Mitigaciones: autenticación segura, escaneo continuo, Falco en runtime.

 Implementación
 
Herramientas utilizadas: Bandit, Semgrep, Gitleaks, Trivy, Checkov, tfsec, OWASP ZAP, Falco y stack PLG. Todas integradas en GitHub Actions.

Resultados de Seguridad

Ejemplos: Gitleaks detectó claves expuestas; Trivy reportó CVEs; ZAP identificó cabeceras faltantes; Checkov/tfsec hallaron configuraciones inseguras; Falco alertó sobre shells en contenedores.

