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
