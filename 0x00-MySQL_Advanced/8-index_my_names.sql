 -- Creating an index on the first letter on a name
 -- Only first letter of name must be indexed
CREATE INDEX idx_name_first on names(LEFT(name,1));