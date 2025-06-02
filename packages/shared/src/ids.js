function isProductId(value) {
  return typeof value === "string" && value.startsWith("AL12-006-");
}

function toProductId(raw) {
  if (isProductId(raw)) return raw;
  const cleaned = String(raw || "").replace(/[^a-zA-Z0-9]/g, "").slice(0, 12);
  return "AL12-006-" + cleaned;
}

module.exports = { isProductId, toProductId };
