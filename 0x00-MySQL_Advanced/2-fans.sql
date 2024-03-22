-- Create a sql script that 

-- A select statement for selecting origin
SELECT origin, SUM(fans) AS nb_fans
-- Using a metal band
FROM metal_bands
-- Orign 
GROUP BY origin
-- Arranging from bottom to top
ORDER BY nb_fans DESC;