SELECT
    used_personalized_feature,
    COUNT(DISTINCT session_id) AS total_sessions,
    SUM(completed_session) AS total_completed_sessions,
    ROUND(100.0 * SUM(completed_session) / COUNT(DISTINCT session_id), 2) as completion_rate
FROM spotify_user_events
GROUP BY used_personalized_feature;