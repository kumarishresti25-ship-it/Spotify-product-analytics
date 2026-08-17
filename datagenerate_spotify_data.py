import pandas as pd
import numpy as np

def generate_spotify_events(n_users=10000, seed=42):
    np.random.seed(seed)
    users = [f"U_{i:05d}" for i in range(n_users)]
    
    event_logs = []
    for uid in users:
        # 15% of users are Premium subscribers
        is_premium = np.random.choice([0, 1], p=[0.85, 0.15])
        sessions = np.random.randint(1, 6)
        
        for session_id in range(sessions):
            # 45% interaction rate with personalized discovery features (Discover Weekly / AI DJ)
            used_personalized_feature = np.random.choice([0, 1], p=[0.55, 0.45])
            
            # Funnel progression probabilities
            app_open = 1
            search_or_browse = np.random.choice([0, 1], p=[0.20, 0.80])
            track_play = np.random.choice([0, 1], p=[0.35, 0.65]) if search_or_browse else 0
            save_or_lyrics = np.random.choice([0, 1], p=[0.50, 0.50]) if track_play else 0
            completed_session = np.random.choice([0, 1], p=[0.25, 0.75]) if track_play else 0
            
            event_logs.append({
                'user_id': uid,
                'session_id': f"{uid}_S{session_id}",
                'is_premium': is_premium,
                'used_personalized_feature': used_personalized_feature,
                'app_open': app_open,
                'search_or_browse': search_or_browse,
                'track_play': track_play,
                'save_or_lyrics': save_or_lyrics,
                'completed_session': completed_session
            })
            
    df = pd.DataFrame(event_logs)
    
    # Save the file directly in the current folder
    df.to_csv('spotify_user_events.csv', index=False)
    print(f"Generated {len(df)} Spotify session logs successfully and saved to 'spotify_user_events.csv'.")

if __name__ == "__main__":
    generate_spotify_events()