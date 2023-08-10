-- creates a stored procedure ComputeAverageWeightedScoreForUser
-- that computes and store the average weighted score for a student.
DELIMITER //
CREATE PROCEDURE ComputeAverageWeightedScoreForUser(IN user_id INT)
BEGIN
	DECLARE avg_score FLOAT;
	SELECT SUM(score * projects.weight) / SUM(projects.weight) 
	INTO avg_score
	FROM corrections
	WHERE corrections.user_id = user_id;
	UPDATE users SET average_score = avg_score WHERE users.id = user_id;
END//
DELIMITER ;
