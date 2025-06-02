function ok(value) {
  return { ok: true, value };
}

function err(error) {
  return { ok: false, error };
}

function mapResult(result, map) {
  return result.ok ? ok(map(result.value)) : result;
}

module.exports = { ok, err, mapResult };
