-- Best band ever!
-- ranks country origins of bands

SELECT origin, SUM(fans) as nb_fans
FROM metal_bands
GROUP By origin
ORDER By nb_fans DESC;
