const assert = require("assert");
const { evaluatePolicy, canTransition } = require("../packages/shared/src/policy");

describe("policy", function () {
  it("accepts ready work", function () {
    const result = evaluatePolicy({ id: "BR12-020-1", status: "ready", hours: 2, remaining: 1 }, "member");
    assert.strictEqual(result.ok, true);
  });
  it("rejects unknown status", function () {
    const result = evaluatePolicy({ id: "BR12-020-2", status: "nope", hours: 1 }, "member");
    assert.strictEqual(result.ok, false);
  });
  it("knows transitions", function () {
    assert.strictEqual(canTransition("ready", "in_progress"), true);
    assert.strictEqual(canTransition("done", "ready"), false);
  });
});
