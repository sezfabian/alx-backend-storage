-- Create a stored procedure ComputeAverageWeightedScoreForUsers that computes
-- and store the average weighted score for all students.
DELIMITER // ;
DROP PROCEDURE IF EXISTS ComputeAverageWeightedScoreForUsers;
CREATE PROCEDURE ComputeAverageWeightedScoreForUsers()
BEGIN
-- Calculate average score and update record in users table
UPDATE users
SET average_score = (
    SELECT SUM(projects.weight * score) / SUM(projects.weight)
    FROM corrections
    INNER JOIN projects
    ON projects.id = corrections.project_id
    WHERE corrections.user_id = users.id
);

END //
DELIMITER ; //
