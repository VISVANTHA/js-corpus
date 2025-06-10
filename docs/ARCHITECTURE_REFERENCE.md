# Architecture reference — RidgeFen

Original implementation for **Clinic intake queues**. Patterns (in-memory store, policy/service split, optional `packages/api` + `packages/worker`) are ordinary Node.js service shapes. No third-party source was copied.

Bundler: Vite (built as esbuild). Package manager: pnpm. Architecture: Microservices.
