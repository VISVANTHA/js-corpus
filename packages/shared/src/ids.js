export function isProductId(value) {
  return typeof value === "string" && value.startsWith("OR18-038-");
}

export function toProductId(raw) {
  if (isProductId(raw)) return raw;
  const cleaned = String(raw || "").replace(/[^a-zA-Z0-9]/g, "").slice(0, 12);
  return "OR18-038-" + cleaned;
}
