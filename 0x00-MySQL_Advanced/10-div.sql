CREATE FUNCTION SafeDiv(a INT, b INT)  -- Create a new function named SafeDiv that takes two integer arguments, a and b
RETURNS INT  -- Specify that the function returns an integer value
BEGIN  -- Begin the body of the function
    IF b = 0 THEN  -- Check if the value of b is equal to 0
        RETURN 0;  -- If b is 0, return 0
    ELSE  -- Otherwise
        RETURN a / b;  -- Return the result of dividing a by b
    END IF;  -- End the conditional statement
END;  -- End the body of the function
