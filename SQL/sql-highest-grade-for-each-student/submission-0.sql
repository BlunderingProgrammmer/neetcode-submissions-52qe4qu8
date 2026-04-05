-- Write your query below
SELECT DISTINCT ON (student_id) -- DISTINCT KEY WORD IS CRUTIAL HER AND USES ORDER BY AS A BASIS TO  SORT AND TIE BRAKER AS EXAM ID
    student_id,
    exam_id,
    score
FROM exam_results 
ORDER BY student_id ASC,score DESC,exam_id ASC;