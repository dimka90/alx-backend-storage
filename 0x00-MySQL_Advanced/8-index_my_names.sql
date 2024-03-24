 -- Creating an index on the first letter on a name
CREATE index idx_name_first on names(LEFT(name,1));