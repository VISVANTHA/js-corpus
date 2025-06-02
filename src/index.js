const { DATASET_CLOCK } = require("./clock");
const { MemoryStore } = require("./store");
const { createService } = require("./service");
function createApp() {
  const store = new MemoryStore(DATASET_CLOCK);
  const service = createService(store);
  return { product: "BrambleQuarry", store, service, clock: DATASET_CLOCK };
}

module.exports = { createApp };
