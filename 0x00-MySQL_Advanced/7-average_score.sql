-- Change the delimiter to $$ to handle the procedure definition
DELIMITER $$;

-- Create a stored procedure named ComputeAverageScoreForUser, taking user_id as input
CREATE PROCEDURE ComputeAverageScoreForUser(IN user_id INT)
BEGIN 
    -- Update the users table, setting the average_score column to the result of the subquery
    UPDATE users
    SET 
    average_score = (SELECT AVG(score) FROM corrections WHERE corrections.user_id = user_id);
    -- Filter the rows to update to match the user_id provided
    WHERE id = user_id;
END $$;

-- Reset the delimiter back to the default semicolon
DELIMITER ;
