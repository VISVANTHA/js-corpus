# Architecture reference — YarrowMeadow

Original implementation for **Harbor slip bookings**. Patterns (in-memory store, policy/service split, optional `packages/api` + `packages/worker`) are ordinary Node.js service shapes. No third-party source was copied.

Bundler: Rspack. Package manager: yarn (Berry). Architecture: Monolith.
