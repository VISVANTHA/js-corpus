function isProductId(value) {
  return typeof value === "string" && value.startsWith("DR12-061-");
}

function toProductId(raw) {
  if (isProductId(raw)) return raw;
  const cleaned = String(raw || "").replace(/[^a-zA-Z0-9]/g, "").slice(0, 12);
  return "DR12-061-" + cleaned;
}

module.exports = { isProductId, toProductId };
