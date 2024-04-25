-- creates a stored procedure `ComputerAverageScoreForUser` that computes
-- and stores the average score for a student
-- the procedure takes 1 argument: `user_id`
CREATE TABLE IF NOT EXISTS average_scores (
    user_id INT PRIMARY KEY,
    score DECIMAL(10,2)
);

DELIMITER //

CREATE PROCEDURE ComputeAverageScoreForUser(IN user_id INT)
BEGIN
    DECLARE avg_score DECIMAL(10,2);

    -- Compute average score
    SELECT AVG(score) INTO avg_score
    FROM corrections
    WHERE user_id = user_id;

    -- Update or insert the average score for the user
    IF EXISTS (SELECT 1 FROM average_scores WHERE user_id = user_id) THEN
        UPDATE average_scores SET score = avg_score WHERE user_id = user_id;
    ELSE
        INSERT INTO average_scores (user_id, score) VALUES (user_id, avg_score);
    END IF;
END;
//

DELIMITER ;
