# Guía rápida de demostración

## 1. Secret Scanning

Abre la alerta asociada a `src/demo_config.py`.

Preguntas:

- ¿Eliminar el valor del último commit elimina todo el riesgo?
- ¿Qué haríamos si fuera una credencial real?

Puntos clave:

- El valor es ficticio.
- Para una credencial real: revocar o rotar, investigar uso, eliminar exposición y sustituir por un mecanismo seguro.
- Explica la diferencia entre detección y Push Protection.

## 2. Dependabot

Abre una alerta de dependencia y muestra:

- paquete y versión afectados;
- severidad y advisory;
- versión corregida, si GitHub la indica;
- manifiesto donde se declaró la dependencia.

Pregunta:

- ¿Quién es responsable de una dependencia transitiva?

Punto clave:

- Una actualización debe ir acompañada de pruebas de compatibilidad y verificación de remediación.

## 3. CodeQL

Abre la alerta de SQL Injection y sigue el flujo:

```text
request.args.get("id") -> user_id -> query -> cursor.execute(query)
```

Explica:

- **Source:** entrada HTTP controlada por el usuario.
- **Sink:** ejecución de la consulta SQL.
- **Corrección:** consulta parametrizada, validación y prueba de regresión.

## Cierre

```text
Detectar -> Entender -> Corregir -> Prevenir
```

Frase final:

> La mejor vulnerabilidad es la que se detecta y corrige antes de llegar a producción.
