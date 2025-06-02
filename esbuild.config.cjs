const esbuild = require("esbuild");
esbuild.build({
  entryPoints: ["src/index.js"],
  bundle: true,
  platform: "node",
  outfile: "dist/index.js",
  logLevel: "info",
}).catch(() => process.exit(1));
