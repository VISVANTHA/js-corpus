export function isProductId(value) {
  return typeof value === "string" && value.startsWith("ZE22-053-");
}

export function toProductId(raw) {
  if (isProductId(raw)) return raw;
  const cleaned = String(raw || "").replace(/[^a-zA-Z0-9]/g, "").slice(0, 12);
  return "ZE22-053-" + cleaned;
}
