UPDATE person_entities
SET research_status = CASE
        WHEN EXISTS (
            SELECT 1
            FROM research_attempts
            WHERE research_attempts.person_id = person_entities.person_id
              AND research_attempts.outcome NOT IN ('planned', 'skipped_budget')
        ) THEN 'in_progress'
        ELSE 'not_started'
    END,
    next_action = CASE
        WHEN EXISTS (
            SELECT 1
            FROM research_attempts
            WHERE research_attempts.person_id = person_entities.person_id
              AND research_attempts.outcome NOT IN ('planned', 'skipped_budget')
        ) THEN 'Continue the minimum research protocol with the next source family.'
        ELSE NULL
    END,
    updated_at = strftime('%Y-%m-%dT%H:%M:%SZ', 'now')
WHERE research_status = 'candidate_found'
  AND NOT EXISTS (
      SELECT 1
      FROM candidate_matches
      WHERE candidate_matches.person_id = person_entities.person_id
        AND candidate_matches.candidate_type <> 'duplicate_person'
        AND candidate_matches.match_assessment = 'unreviewed'
  );

UPDATE research_queue
SET research_status = CASE
        WHEN EXISTS (
            SELECT 1
            FROM research_attempts
            WHERE research_attempts.person_id = research_queue.person_id
              AND research_attempts.outcome NOT IN ('planned', 'skipped_budget')
        ) THEN 'in_progress'
        ELSE 'not_started'
    END,
    next_action = CASE
        WHEN EXISTS (
            SELECT 1
            FROM research_attempts
            WHERE research_attempts.person_id = research_queue.person_id
              AND research_attempts.outcome NOT IN ('planned', 'skipped_budget')
        ) THEN 'Continue staged research.'
        ELSE NULL
    END,
    updated_at = strftime('%Y-%m-%dT%H:%M:%SZ', 'now')
WHERE research_status = 'candidate_found'
  AND NOT EXISTS (
      SELECT 1
      FROM candidate_matches
      WHERE candidate_matches.person_id = research_queue.person_id
        AND candidate_matches.candidate_type <> 'duplicate_person'
        AND candidate_matches.match_assessment = 'unreviewed'
  );

UPDATE person_entities
SET research_status = 'candidate_found',
    next_action = 'Review discovery candidates for identity and temporal relevance.',
    updated_at = strftime('%Y-%m-%dT%H:%M:%SZ', 'now')
WHERE EXISTS (
    SELECT 1
    FROM candidate_matches
    WHERE candidate_matches.person_id = person_entities.person_id
      AND candidate_matches.candidate_type <> 'duplicate_person'
      AND candidate_matches.match_assessment = 'unreviewed'
);

UPDATE research_queue
SET research_status = 'candidate_found',
    next_action = 'Review source candidates.',
    updated_at = strftime('%Y-%m-%dT%H:%M:%SZ', 'now')
WHERE EXISTS (
    SELECT 1
    FROM candidate_matches
    WHERE candidate_matches.person_id = research_queue.person_id
      AND candidate_matches.candidate_type <> 'duplicate_person'
      AND candidate_matches.match_assessment = 'unreviewed'
);
