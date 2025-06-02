const { DATASET_CLOCK } = require("../../shared/src/clock");
const { MemoryStore } = require("./store");
const { createService } = require("./service");

function createApp() {
  const store = new MemoryStore(DATASET_CLOCK);
  const service = createService(store);
  return { product: "BrambleMarina", store, service, clock: DATASET_CLOCK };
}

module.exports = { createApp };
