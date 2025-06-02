const path = require("path");
module.exports = {
  entry: "./packages/api/src/index.js",
  target: "node",
  output: { path: path.resolve(__dirname, "dist"), filename: "index.js" },
};
