export function isProductId(value) {
  return typeof value === "string" && value.startsWith("TH21-034-");
}

export function toProductId(raw) {
  if (isProductId(raw)) return raw;
  const cleaned = String(raw || "").replace(/[^a-zA-Z0-9]/g, "").slice(0, 12);
  return "TH21-034-" + cleaned;
}
