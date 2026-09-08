# GHAS Demo Vulnerable

> [!WARNING]
> Proyecto **deliberadamente vulnerable** para una clase de GitHub Advanced Security.
> No desplegar, no reutilizar en producción y no sustituir los valores ficticios por credenciales reales.

## Objetivo

Generar demostraciones controladas de tres capacidades:

1. **Secret Scanning** mediante un patrón personalizado y un secreto ficticio.
2. **Dependabot Alerts / SCA** mediante dependencias antiguas fijadas en `requirements.txt`.
3. **Code Scanning con CodeQL** mediante un flujo de datos vulnerable a SQL Injection.

## Estructura

```text
.
├── .github/
│   ├── dependabot.yml
│   └── workflows/codeql.yml
├── docs/DEMO-GUIDE.md
├── src/
│   ├── app.py
│   └── demo_config.py
├── requirements.txt
└── SECURITY.md
```

## Preparación del repositorio

1. Crea un repositorio de GitHub dedicado exclusivamente a formación.
2. Sube este contenido a la rama `main`.
3. Habilita las funciones de seguridad disponibles en `Settings > Advanced Security`.
4. Para Secret Scanning, crea un patrón personalizado:

```regex
DEMO_SECRET_GHAS_[A-Z0-9]{32}
```

5. Ejecuta primero **Save and dry run** y después publica el patrón.
6. Para CodeQL, permite GitHub Actions y ejecuta el workflow `CodeQL Demo`.
7. Revisa los resultados en la pestaña `Security`.

## Resultado esperado

- Un match del patrón ficticio en `src/demo_config.py`.
- Alertas de dependencias si GitHub Advisory Database contiene avisos aplicables a las versiones fijadas.
- Una alerta de CodeQL asociada a la construcción y ejecución de una consulta SQL con datos provenientes de una solicitud HTTP.

> La aparición exacta de alertas puede depender de la configuración de GHAS, licencias, visibilidad del repositorio, versión del analizador y avisos vigentes.

## Flujo recomendado para la clase

Para cada hallazgo explica:

```text
Qué detectó -> Por qué importa -> Cómo corregir -> Cómo prevenir
```

Consulta `docs/DEMO-GUIDE.md` para el guion operativo.
