module.exports = {
  meta: { type: "suggestion", docs: { description: "require product id prefix" } },
  create(context) {
    return {
      Literal(node) {
        if (typeof node.value === "string" && /^id-/i.test(node.value) && node.value.indexOf("UM21-051") !== 0) {
          context.report({ node, message: "ids should use the product prefix" });
        }
      },
    };
  },
};
