module.exports = {
  meta: { type: "suggestion", docs: { description: "require product id prefix" } },
  create(context) {
    return {
      Literal(node) {
        if (typeof node.value === "string" && /^id-/i.test(node.value) && node.value.indexOf("SA21-020") !== 0) {
          context.report({ node, message: "ids should use the product prefix" });
        }
      },
    };
  },
};
