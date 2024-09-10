CREATE TABLE customers (
    customer_id SERIAL PRIMARY KEY,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    email VARCHAR(100),
    phone VARCHAR(20)
);

CREATE TABLE orders (
    order_id SERIAL PRIMARY KEY,
    customer_id INT REFERENCES customers(customer_id),
    order_date DATE,
    total_amount DECIMAL(10, 2)
);

CREATE TABLE products (
    product_id SERIAL PRIMARY KEY,
    product_name VARCHAR(100),
    price DECIMAL(10, 2)
);

CREATE TABLE order_items (
    order_item_id SERIAL PRIMARY KEY,
    order_id INT REFERENCES orders(order_id),
    product_id INT REFERENCES products(product_id),
    quantity INT,
    price DECIMAL(10, 2)
);


INSERT INTO customers (customer_id, first_name, last_name, email, phone) VALUES
(1, 'John', 'Doe', 'john.doe@email.com', '555-1234'),
(2, 'Jane', 'Smith', 'jane.smith@email.com', '555-5678'),
(3, 'Bob', 'Johnson', 'bob.johnson@email.com', '555-9012'),
(4, 'Alice', 'Williams', 'alice.williams@email.com', '555-3456'),
(5, 'Charlie', 'Brown', 'charlie.brown@email.com', '555-7890');

INSERT INTO orders (order_id, customer_id, order_date, total_amount) VALUES
(1, 1, '2023-01-15', 150.00),
(2, 2, '2023-02-20', 200.50),
(3, 3, '2023-03-10', 75.25),
(4, 1, '2023-04-05', 300.00),
(5, 4, '2023-05-12', 125.75);

INSERT INTO products (product_id, product_name, price) VALUES
(1, 'Widget A', 19.99),
(2, 'Gadget B', 29.99),
(3, 'Gizmo C', 39.99),
(4, 'Doohickey D', 49.99),
(5, 'Thingamajig E', 59.99);

INSERT INTO order_items (order_item_id, order_id, product_id, quantity, price) VALUES
(1, 1, 1, 2, 19.99),
(2, 1, 3, 1, 39.99),
(3, 2, 2, 3, 29.99),
(4, 3, 4, 1, 49.99),
(5, 4, 5, 2, 59.99),
(6, 5, 1, 3, 19.99),
(7, 5, 2, 1, 29.99);