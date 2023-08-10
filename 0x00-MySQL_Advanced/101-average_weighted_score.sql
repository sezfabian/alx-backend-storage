-- creates a stored procedure ComputeAverageWeightedScoreForUsers that
-- computes and store the average weighted score for all students.
DELIMITER //
CREATE PROCEDURE ComputeAverageWeightedScoreForUsers()
BEGIN
	DECLARE @avg_score FLOAT;
	SELECT SUM(score * projects.weight) / SUM(projects.weight) INTO @avg_score FROM corrections
	INNER JOIN projects ON projects.id = corrections.project_id
	WHERE corrections.user_id = users.id;
	UPDATE users SET average_score = @avg_score;
END//
DELIMITER ;
