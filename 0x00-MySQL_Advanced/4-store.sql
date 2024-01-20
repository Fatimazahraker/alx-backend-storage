-- Buy buy buy

CREATE TRIGGER decrease_quatity
AFTER INSERT
ON orders
FOR EACH ROW
UPDATE items SET quantity = quantity - NEW.number
WHERE name = NEW.item_name;
