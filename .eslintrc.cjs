const idPrefix = require("./eslint-rules/id-prefix");
module.exports = {
  env: { es2020: true, node: true, mocha: true },
  parserOptions: { ecmaVersion: 2020, sourceType: "module" },
  plugins: ["sonarjs"],
  rules: {"no-eval": "error", "sonarjs/cognitive-complexity": ["warn", 15]},
};
module.exports.rulesCustom = { "id-prefix": idPrefix };
