-- creates a function `SafeDiv` that divides (and returns) the first by the second number
-- if the second number is zero, it returns 0
DELIMITER //

CREATE FUNCTION SafeDiv(a INT, b INT)
RETURNS INT
DETERMINISTIC
BEGIN
    IF b = 0 THEN
        RETURN 0;
    ELSE
        RETURN a / b;
    END IF;
END;
//

DELIMITER ;
