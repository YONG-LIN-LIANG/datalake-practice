-- Create Table: customers
CREATE TABLE customers (
    customer_id SERIAL PRIMARY KEY,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    email VARCHAR(100),
    phone VARCHAR(20),
    created_at TIMESTAMP DEFAULT NOW(),
    updated_at TIMESTAMP DEFAULT NOW()
);

-- Create Table: orders
CREATE TABLE orders (
    order_id SERIAL PRIMARY KEY,
    customer_id INT REFERENCES customers(customer_id),
    order_date DATE,
    total_amount DECIMAL(10, 2),
    created_at TIMESTAMP DEFAULT NOW(),
    updated_at TIMESTAMP DEFAULT NOW()
);

-- Create Table: products
CREATE TABLE products (
    product_id SERIAL PRIMARY KEY,
    product_name VARCHAR(100),
    price DECIMAL(10, 2),
    created_at TIMESTAMP DEFAULT NOW(),
    updated_at TIMESTAMP DEFAULT NOW()
);

-- Create Table: order_items
CREATE TABLE order_items (
    order_item_id SERIAL PRIMARY KEY,
    order_id INT REFERENCES orders(order_id),
    product_id INT REFERENCES products(product_id),
    quantity INT,
    price DECIMAL(10, 2),
    created_at TIMESTAMP DEFAULT NOW(),
    updated_at TIMESTAMP DEFAULT NOW()
);



-- Insert into customers
INSERT INTO customers (customer_id, first_name, last_name, email, phone, created_at, updated_at) VALUES
(1, 'John', 'Doe', 'john.doe@email.com', '555-1235', '2024-01-01 10:00:00', '2024-01-05 12:00:00'),
(2, 'Jane', 'Smith', 'jane.smith@email.com', '555-5678', '2024-02-01 11:00:00', '2024-02-10 13:00:00'),
(3, 'Bob', 'Johnson', 'bob.johnson@email.com', '555-9012', '2024-03-01 12:00:00', '2024-03-11 14:00:00'),
(4, 'Alice', 'Williams', 'alice.williams@email.com', '555-3456', '2024-04-01 13:00:00', '2024-04-12 15:00:00'),
(5, 'Charlie', 'Brown', 'charlie.brown@email.com', '555-7890', '2024-05-01 14:00:00', '2024-05-15 16:00:00'),
(6, 'Emily', 'Taylor', 'emily.taylor@email.com', '555-6789', '2024-11-10 09:00:00', '2024-11-11 10:00:00'),
(7, 'Michael', 'Clark', 'michael.clark@email.com', '555-4321', '2024-11-11 11:00:00', '2024-11-12 12:00:00'),
(8, 'Sarah', 'Davis', 'sarah.davis@email.com', '555-8765', '2024-11-12 13:00:00', '2024-11-13 14:00:00');

-- Insert into orders
INSERT INTO orders (order_id, customer_id, order_date, total_amount, created_at, updated_at) VALUES
(1, 1, '2024-01-15', 150.00, '2024-01-15 09:30:00', '2024-01-15 11:00:00'),
(2, 2, '2024-02-20', 200.50, '2024-02-20 10:00:00', '2024-02-21 11:30:00'),
(3, 3, '2024-03-10', 75.25, '2024-03-10 14:30:00', '2024-03-10 16:00:00'),
(4, 1, '2024-04-05', 300.00, '2024-04-05 17:00:00', '2024-04-06 18:30:00'),
(5, 4, '2024-05-12', 125.75, '2024-05-12 19:00:00', '2024-05-12 20:30:00'),
(6, 6, '2024-11-13', 180.25, '2024-11-13 15:00:00', '2024-11-13 16:30:00'),
(7, 7, '2024-11-14', 220.75, '2024-11-14 14:00:00', '2024-11-14 15:00:00'),
(8, 8, '2024-11-15', 95.00, '2024-11-15 12:00:00', '2024-11-15 13:00:00');

-- Insert into products
INSERT INTO products (product_id, product_name, price, created_at, updated_at) VALUES
(1, 'Widget A', 19.99, '2024-01-01 08:00:00', '2024-01-02 09:00:00'),
(2, 'Gadget B', 29.99, '2024-02-01 10:00:00', '2024-02-02 11:00:00'),
(3, 'Gizmo C', 39.99, '2024-03-01 12:00:00', '2024-03-02 13:00:00'),
(4, 'Doohickey D', 49.99, '2024-04-01 14:00:00', '2024-04-02 15:00:00'),
(5, 'Thingamajig E', 59.99, '2024-05-01 16:00:00', '2024-05-02 17:00:00'),
(6, 'Doodad F', 24.99, '2024-11-10 08:00:00', '2024-11-10 09:00:00'),
(7, 'Widget G', 34.99, '2024-11-11 08:30:00', '2024-11-11 09:30:00');

-- Insert into order_items
INSERT INTO order_items (order_item_id, order_id, product_id, quantity, price, created_at, updated_at) VALUES
(1, 1, 1, 2, 19.99, '2024-01-15 08:30:00', '2024-01-15 09:00:00'),
(2, 1, 3, 1, 39.99, '2024-01-15 09:00:00', '2024-01-15 10:00:00'),
(3, 2, 2, 3, 29.99, '2024-02-20 10:30:00', '2024-02-20 11:00:00'),
(4, 3, 4, 1, 49.99, '2024-03-10 11:30:00', '2024-03-10 12:00:00'),
(5, 4, 5, 2, 59.99, '2024-04-05 13:30:00', '2024-04-05 14:00:00'),
(6, 5, 1, 3, 19.99, '2024-05-12 15:30:00', '2024-05-12 16:00:00'),
(7, 5, 2, 1, 29.99, '2024-05-12 16:30:00', '2024-05-12 17:00:00'),
(8, 6, 2, 2, 29.99, '2024-11-13 15:30:00', '2024-11-13 16:00:00'),
(9, 6, 4, 1, 49.99, '2024-11-13 16:00:00', '2024-11-13 16:30:00'),
(10, 7, 3, 3, 39.99, '2024-11-14 14:30:00', '2024-11-14 15:00:00'),
(11, 8, 1, 1, 19.99, '2024-11-15 12:30:00', '2024-11-15 13:00:00'),
(12, 8, 5, 1, 59.99, '2024-11-15 13:00:00', '2024-11-15 13:30:00');
