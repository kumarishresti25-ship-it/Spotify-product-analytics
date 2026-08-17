CREATE TABLE spotify_user_events (
    user_id VARCHAR(50),
    session_id VARCHAR(50),
    is_premium INT,
    used_personalized_feature INT,
    app_open INT,
    search_or_browse INT,
    track_play INT,
    save_or_lyrics INT,
    completed_session INT
);