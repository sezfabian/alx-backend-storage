-- creates a function SafeDiv that divides the first by the second number
-- returns 0 if the second number is equal to 0.
DELIMITER //
CREATE FUNCTION SafeDiv (a INT, b INT) RETURNS FLOAT
BEGIN
	RETURN IF(b = 0, 0, a / b);
END//
DELIMITER ;
