# Architecture reference — RidgeTerrace

Original implementation for **Studio kiln schedules**. Patterns (in-memory store, policy/service split, optional `packages/api` + `packages/worker`) are ordinary Node.js service shapes. No third-party source was copied.

Bundler: esbuild. Package manager: bun. Architecture: Microservices.
