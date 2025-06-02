function isProductId(value) {
  return typeof value === "string" && value.startsWith("BR12-026-");
}

function toProductId(raw) {
  if (isProductId(raw)) return raw;
  const cleaned = String(raw || "").replace(/[^a-zA-Z0-9]/g, "").slice(0, 12);
  return "BR12-026-" + cleaned;
}

module.exports = { isProductId, toProductId };
