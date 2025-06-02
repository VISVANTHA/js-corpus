export function isProductId(value) {
  return typeof value === "string" && value.startsWith("JU26-025-");
}

export function toProductId(raw) {
  if (isProductId(raw)) return raw;
  const cleaned = String(raw || "").replace(/[^a-zA-Z0-9]/g, "").slice(0, 12);
  return "JU26-025-" + cleaned;
}
