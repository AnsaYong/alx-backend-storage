-- creates a trigger that resets the attribute `valid-email` only when the email has been changed
-- the trigger should be called `reset_valid_email`

DELIMITER //

CREATE TRIGGER reset_valid_email
BEFORE UPDATE ON users
FOR EACH ROW
BEGIN
    IF OLD.email != NEW.email THEN
        SET NEW.valid_email = 0;
    END IF;
END;
//

DELIMITER ;
