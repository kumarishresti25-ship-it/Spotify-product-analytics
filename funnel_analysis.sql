WITH listening_funnel AS (
    SELECT
        session_id,
        MAX(app_open) AS opened,
        MAX(search_or_browse) AS searched,
        MAX(track_play) AS played_track,
        MAX(save_or_lyrics) AS interacted_extra,
        MAX(completed_session) AS finished_session
    FROM spotify_user_events
    GROUP BY session_id
)
SELECT
    COUNT(session_id) AS total_app_launches,
    SUM(searched) AS search_count,
    SUM(played_track) AS track_play_count,
    SUM(interacted_extra) AS engagement_count,
    SUM(finished_session) AS completed_sessions,
    ROUND(100.0 * SUM(finished_session) / COUNT(session_id), 2) AS overall_funnel_efficiency
FROM listening_funnel;