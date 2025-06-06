import assert from "assert";
import { DATASET_CLOCK } from "../packages/shared/src/clock.js";
import { MemoryStore } from "../packages/api/src/store.js";
import { createService } from "../packages/api/src/service.js";

describe("service", function () {
  it("stores a valid record", function () {
    const service = createService(new MemoryStore(DATASET_CLOCK));
    const saved = service.upsert({ id: "raw1", status: "ready", hours: 2, remaining: 1 }, "member");
    assert.strictEqual(saved.ok, true);
    assert.ok(saved.value.id.indexOf("IN16-010") === 0);
  });
  it("rejects illegal move", function () {
    const service = createService(new MemoryStore(DATASET_CLOCK));
    service.upsert({ id: "raw2", status: "ready", hours: 2, remaining: 1 }, "member");
    const moved = service.move("IN16-010-raw2", "done", "member");
    assert.strictEqual(moved.ok, false);
  });
});
