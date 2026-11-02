## Agent Design

OpsInsight uses a **single-agent architecture with iterative native LLM tool calling and bounded autonomy**.

The agent dynamically selects tools, observes their results and decides whether additional investigation is required before generating its final answer.

### Agent Execution Flow

1. **Understand:** Receive the user's question and prepare relevant dataset context.
2. **Discover:** Select `list_datasets` when dataset discovery is required.
3. **Inspect:** Select `inspect_schema` when table or column information is needed.
4. **Execute:** Select an appropriate analytical tool, such as `execute_readonly_sql`.
5. **Validate:** The backend validates tool arguments and SQL before execution.
6. **Observe:** Return database results or controlled errors to the LLM.
7. **Decide:** The LLM evaluates the observations and decides whether another tool call is necessary.
8. **Respond:** Generate an evidence-backed answer when sufficient information is available.

### Decision Handling

| Situation | Agent behaviour |
|---|---|
| Results found | Evaluate results and investigate further or answer |
| No results | Consider query refinement or report unavailable data |
| Missing schema | Inspect schema before querying |
| Invalid SQL | Reject execution and return validation feedback |
| Tool execution error | Handle safely within execution limits |
| Ambiguous question | Request clarification |
| Sufficient evidence | Generate final answer |

### Initial Agent Tools

| Tool | Responsibility |
|---|---|
| `list_datasets` | Discover available datasets |
| `inspect_schema` | Inspect tables and columns |
| `execute_readonly_sql` | Execute validated analytical SQL |
| `compare_metrics` | Compare business metrics |
| `analyze_trend` | Analyze trends over time |

### Implementation Strategy

**Stage 1 — Native Tool Calling**

Build the complete agent orchestration ourselves using the OpenAI-compatible SDK, without LangChain.

Implement tool definitions, registry, Pydantic argument validation, iterative execution loop, result handling, timeouts and execution limits.

**Stage 2 — LangChain**

Implement an equivalent agent using LangChain, reusing the same tools, connectors, LLM providers and security validation.

Compare both implementations for reliability, complexity, execution behaviour and observability.

The selected implementation will be configurable through `AGENT_FRAMEWORK`.

### Execution Constraints

- Maximum agent execution steps.
- Overall execution timeout.
- SQL validation before execution.
- Read-only database access.
- Query row limits and timeouts.
- Controlled tool error handling.
- No unsupported analytical claims.
- No exposure of hidden chain-of-thought.

The LLM decides what to investigate; Python controls execution; MySQL provides the evidence.