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
(1, 'John', 'Doe', 'john.doe@email.com', '555-1235', '2023-01-01 10:00:00', '2023-01-05 12:00:00'),
(2, 'Jane', 'Smith', 'jane.smith@email.com', '555-5678', '2023-02-01 11:00:00', '2023-02-10 13:00:00'),
(3, 'Bob', 'Johnson', 'bob.johnson@email.com', '555-9012', '2023-03-01 12:00:00', '2023-03-11 14:00:00'),
(4, 'Alice', 'Williams', 'alice.williams@email.com', '555-3456', '2023-04-01 13:00:00', '2023-04-12 15:00:00'),
(5, 'Charlie', 'Brown', 'charlie.brown@email.com', '555-7890', '2023-05-01 14:00:00', '2023-05-15 16:00:00');

-- Insert into orders
INSERT INTO orders (order_id, customer_id, order_date, total_amount, created_at, updated_at) VALUES
(1, 1, '2023-01-15', 150.00, '2023-01-15 09:30:00', '2023-01-15 11:00:00'),
(2, 2, '2023-02-20', 200.50, '2023-02-20 10:00:00', '2023-02-21 11:30:00'),
(3, 3, '2023-03-10', 75.25, '2023-03-10 14:30:00', '2023-03-10 16:00:00'),
(4, 1, '2023-04-05', 300.00, '2023-04-05 17:00:00', '2023-04-06 18:30:00'),
(5, 4, '2023-05-12', 125.75, '2023-05-12 19:00:00', '2023-05-12 20:30:00');

-- Insert into products
INSERT INTO products (product_id, product_name, price, created_at, updated_at) VALUES
(1, 'Widget A', 19.99, '2023-01-01 08:00:00', '2023-01-02 09:00:00'),
(2, 'Gadget B', 29.99, '2023-02-01 10:00:00', '2023-02-02 11:00:00'),
(3, 'Gizmo C', 39.99, '2023-03-01 12:00:00', '2023-03-02 13:00:00'),
(4, 'Doohickey D', 49.99, '2023-04-01 14:00:00', '2023-04-02 15:00:00'),
(5, 'Thingamajig E', 59.99, '2023-05-01 16:00:00', '2023-05-02 17:00:00');

-- Insert into order_items
INSERT INTO order_items (order_item_id, order_id, product_id, quantity, price, created_at, updated_at) VALUES
(1, 1, 1, 2, 19.99, '2023-01-15 08:30:00', '2023-01-15 09:00:00'),
(2, 1, 3, 1, 39.99, '2023-01-15 09:00:00', '2023-01-15 10:00:00'),
(3, 2, 2, 3, 29.99, '2023-02-20 10:30:00', '2023-02-20 11:00:00'),
(4, 3, 4, 1, 49.99, '2023-03-10 11:30:00', '2023-03-10 12:00:00'),
(5, 4, 5, 2, 59.99, '2023-04-05 13:30:00', '2023-04-05 14:00:00'),
(6, 5, 1, 3, 19.99, '2023-05-12 15:30:00', '2023-05-12 16:00:00'),
(7, 5, 2, 1, 29.99, '2023-05-12 16:30:00', '2023-05-12 17:00:00');
