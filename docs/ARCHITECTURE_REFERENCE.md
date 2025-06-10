# Architecture reference — AlderInlay

Original implementation for **Fleet maintenance logs**. Patterns (in-memory store, policy/service split, optional `packages/api` + `packages/worker`) are ordinary Node.js service shapes. No third-party source was copied.

Bundler: Vite (built as esbuild). Package manager: bun. Architecture: Microservices.
