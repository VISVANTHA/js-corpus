const idPrefix = require("./eslint-rules/id-prefix");
module.exports = {
  env: { es2020: true, node: true, mocha: true },
  parserOptions: { ecmaVersion: 2020, sourceType: "module" },
  plugins: ["security", "sonarjs"],
  rules: {"no-eval": "error", "security/detect-object-injection": "warn", "security/detect-non-literal-regexp": "warn", "sonarjs/cognitive-complexity": ["warn", 15]},
};
module.exports.rulesCustom = { "id-prefix": idPrefix };
