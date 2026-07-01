-- data/products.sql
-- Seed schema + data for the product catalog (Postgres source for PostgresLoader).

DROP TABLE IF EXISTS products;

-- Create products table
CREATE TABLE products (
    id          SERIAL PRIMARY KEY,
    name        TEXT NOT NULL,
    tier        TEXT NOT NULL,
    description TEXT,
    specs       JSONB
);

-- Index tier since we filter/facet on it in Azure AI Search
CREATE INDEX idx_products_tier ON products (tier);

-- Insert Pro tier products
INSERT INTO products (name, tier, description, specs)
VALUES
('Pro Laptop 15', 'Pro', 'High-performance laptop with 15-inch display.',
 '{"CPU":"Intel i7","RAM":"16GB","Storage":"512GB SSD"}'::jsonb),
('Pro Smartphone X', 'Pro', 'Flagship smartphone with advanced camera system.',
 '{"Display":"6.5-inch OLED","Camera":"108MP Triple Lens","Battery":"4000mAh"}'::jsonb);

-- Insert Standard tier products
INSERT INTO products (name, tier, description, specs)
VALUES
('Standard Tablet 10', 'Standard', 'Affordable tablet with 10-inch screen.',
 '{
