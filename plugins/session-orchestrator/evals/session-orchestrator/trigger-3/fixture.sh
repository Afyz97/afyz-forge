#!/usr/bin/env bash
# Small Node project used as the eval workspace. Files and git state only.
set -euo pipefail
mkdir -p src test
cat > package.json <<'J'
{
  "name": "orders-api",
  "version": "1.0.0",
  "type": "module",
  "scripts": { "test": "node --test" }
}
J
cat > src/orders.js <<'J'
// TODO: paginate instead of returning everything
export function listOrders(db) {
  return db.orders.slice();
}

export function findOrder(db, id) {
  return db.orders.find((o) => o.id === id) ?? null;
}

// Unused since the v2 checkout; kept "just in case".
export function legacyTotal(order) {
  return order.items.reduce((sum, i) => sum + i.price, 0);
}
J
cat > src/server.js <<'J'
import http from "node:http";
import { listOrders, findOrder } from "./orders.js";

const db = { orders: [{ id: "a1", customer: "Siti", items: [{ sku: "X", price: 12.5 }] }] };

// TODO: add auth before this goes public
export const server = http.createServer((req, res) => {
  if (req.url === "/orders") {
    res.setHeader("content-type", "application/json");
    return res.end(JSON.stringify(listOrders(db)));
  }
  const m = req.url.match(/^\/orders\/(\w+)$/);
  if (m) {
    const order = findOrder(db, m[1]);
    res.statusCode = order ? 200 : 404;
    return res.end(JSON.stringify(order));
  }
  res.statusCode = 404;
  res.end();
});
J
cat > test/orders.test.js <<'J'
import test from "node:test";
import assert from "node:assert/strict";
import { findOrder } from "../src/orders.js";

test("findOrder returns null for unknown id", () => {
  assert.equal(findOrder({ orders: [] }, "zz"), null);
});
J
cat > README.md <<'J'
# orders-api

Tiny HTTP API that lists orders. Run tests with `npm test`.
J
git init -q
git add -A
git -c user.name=eval -c user.email=eval@example.com commit -q -m "initial"
