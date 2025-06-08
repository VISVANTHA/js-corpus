const { sanitizeText, allowRole } = require("./sanitize");

function authorize(actor, action) {
  const role = sanitizeText(actor && actor.role);
  if (!allowRole(role)) return { ok: false, reason: "unknown-role" };
  if (action === "write" && role === "viewer") return { ok: false, reason: "read-only" };
  return { ok: true, role };
}
module.exports = { authorize };
