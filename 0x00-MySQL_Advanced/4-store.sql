-- Create trigger to decrease item quantity in stock after adding a new order
CREATE TRIGGER decrease_item_quantity_in_stock AFTER INSERT ON orders
-- Looping through each row
FOR EACH ROW
-- Update the quantity of the corresponding item in the items table
UPDATE items
-- Subtract the quantity of the new order from the current item quantity
SET quantity = quantity - NEW.number
-- Match the item name of the new order with the item name in the items table
WHERE name = NEW.item_name;

