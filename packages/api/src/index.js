import { DATASET_CLOCK } from "../../shared/src/clock.js";
import { MemoryStore } from "./store.js";
import { createService } from "./service.js";

function createApp() {
  const store = new MemoryStore(DATASET_CLOCK);
  const service = createService(store);
  return { product: "GlacierTerrace", store, service, clock: DATASET_CLOCK };
}

export { createApp };
