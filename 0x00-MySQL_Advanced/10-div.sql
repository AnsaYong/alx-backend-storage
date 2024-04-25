-- creates a function `SafeDiv` that divides (and returns) the first by the second number
-- if the second number is zero, it returns 0
DELIMITER //

CREATE FUNCTION SafeDiv(numerator INT, denominator INT) RETURNS INT
BEGIN
  IF denominator = 0 THEN
    RETURN 0;
  ELSE
    RETURN numerator / denominator;
  END IF;
END;
//

DELIMITER ;
