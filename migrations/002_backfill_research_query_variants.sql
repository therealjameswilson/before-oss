UPDATE research_attempts
SET query_variant_type = CASE
    WHEN source_adapter = 'nara' THEN 'official'
    WHEN source_adapter = 'cia' THEN 'exact_oss'
    WHEN source_adapter = 'loc'
         AND (
             query_text LIKE '% employer 1940'
             OR query_text LIKE '% occupation 1940'
         ) THEN 'employment'
    WHEN source_adapter = 'loc'
         AND (
             query_text LIKE '% obituary'
             OR query_text LIKE '% biography'
         ) THEN 'institutional'
    WHEN source_adapter = 'loc' THEN 'exact_oss'
    WHEN source_adapter = 'web'
         AND (
             query_text LIKE '% employer 1940'
             OR query_text LIKE '% occupation 1940'
         ) THEN 'employment'
    WHEN source_adapter = 'web'
         AND (
             query_text LIKE '% obituary'
             OR query_text LIKE '% biography'
         ) THEN 'institutional'
    WHEN source_adapter = 'web' THEN 'exact_oss'
    ELSE 'unknown'
END
WHERE query_variant_type IS NULL OR query_variant_type = '';
