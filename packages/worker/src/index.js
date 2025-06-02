const { evaluatePolicy } = require("../../shared/src/policy");
function runDigest(records, role) {
  let accepted = 0;
  let rejected = 0;
  for (let i = 0; i < records.length; i += 1) {
    const decision = evaluatePolicy(records[i], role);
    if (decision.ok) accepted += 1;
    else rejected += 1;
  }
  return { accepted, rejected };
}

module.exports = { runDigest };
