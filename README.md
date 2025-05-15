# 🧠 Context Initial Orchestrator (Langchain + Gemini)

## 🧩 Objetivo General

Permitir que un workflow definido en YAML inicialice un contexto de ejecución que podrá ser utilizado por los siguientes nodos del pipeline de LangChain con Gemini.

---

## 🔧 Componentes Clave

### 1. Parser de YAML del Workflow
- Lee la definición del workflow y valida su estructura.
- Reconoce el nodo `"Context Initial"` con clave `context`.

### 2. Validador de Nodo "Context Initial"
- Valida existencia y estructura del campo `context`.
- Acepta:
  - Diccionarios simples
  - Estructuras anidadas
  - Valor vacío/ausente → `{}`

### 3. Context Manager
- Almacena el contexto global durante la ejecución del workflow.
- Métodos: `get_context()`, `update_context()`, `reset_context()`

### 4. Runtime Engine
- Ejecuta nodos secuencialmente.
- Cada nodo accede al contexto y puede modificarlo.

---

## ✅ Escenarios de Prueba

| Escenario | Descripción |
|----------|-------------|
| 1 | Inicialización exitosa con contexto simple |
| 2 | Inicialización exitosa con contexto complejo |
| 3 | Inicialización sin contexto explícito (vacío) |
| 4 | Contexto accesible por nodo siguiente |
| 5 | Configuración inválida lanza error |

---

## 📦 Estructura YAML esperada

```yaml
workflow:
  - type: context_initial
    context:
      user_id: 123
      session_data:
        language: "es"
        level: "advanced"
  - type: agent_node
    action: generate_response
