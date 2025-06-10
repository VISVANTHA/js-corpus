# Architecture reference — CopperDelta

Original implementation for **Orchard harvest lots**. Patterns (in-memory store, policy/service split, optional `packages/api` + `packages/worker`) are ordinary Node.js service shapes. No third-party source was copied.

Bundler: Vite (built as esbuild). Package manager: pnpm. Architecture: Monolith.
