const assert = require("assert");
const { DATASET_CLOCK } = require("../src/clock");
const { MemoryStore } = require("../src/store");
const { createService } = require("../src/service");

describe("service", function () {
  it("stores a valid record", function () {
    const service = createService(new MemoryStore(DATASET_CLOCK));
    const saved = service.upsert({ id: "raw1", status: "ready", hours: 2, remaining: 1 }, "member");
    assert.strictEqual(saved.ok, true);
    assert.ok(saved.value.id.indexOf("BR12-019") === 0);
  });
  it("rejects illegal move", function () {
    const service = createService(new MemoryStore(DATASET_CLOCK));
    service.upsert({ id: "raw2", status: "ready", hours: 2, remaining: 1 }, "member");
    const moved = service.move("BR12-019-raw2", "done", "member");
    assert.strictEqual(moved.ok, false);
  });
});
