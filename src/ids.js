function isProductId(value) {
  return typeof value === "string" && value.startsWith("CA12-037-");
}

function toProductId(raw) {
  if (isProductId(raw)) return raw;
  const cleaned = String(raw || "").replace(/[^a-zA-Z0-9]/g, "").slice(0, 12);
  return "CA12-037-" + cleaned;
}

module.exports = { isProductId, toProductId };
