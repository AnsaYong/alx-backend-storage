-- creates an index `idx_name_first` on the table `names` and the first letter of the `name` column
-- only the first letter of `name` is indexed
CREATE INDEX idx_name_first ON names (LEFT(name, 1));