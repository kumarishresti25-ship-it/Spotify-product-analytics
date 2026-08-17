import pandas as pd

def analyze_spotify_funnel():
    df = pd.read_csv('spotify_user_events.csv')
    
    total_sessions = len(df)
    funnel_stages = ['app_open', 'search_or_browse', 'track_play', 'save_or_lyrics', 'completed_session']
    
    print("=== SPOTIFY LISTENING FUNNEL REPORT ===")
    counts = df[funnel_stages].sum()
    for i, stage in enumerate(funnel_stages):
        count = counts[stage]
        conversion_rate = (count / total_sessions) * 100
        print(f"Stage {i+1}: {stage.replace('_', ' ').capitalize()} -> {count} sessions ({conversion_rate:.2f}%)")
        
    print("\n=== FEATURE ADOPTION (PERSONALIZED DISCOVERY) ===")
    feature_users = df[df['used_personalized_feature'] == 1]
    standard_users = df[df['used_personalized_feature'] == 0]
    
    feature_completion = (feature_users['completed_session'].sum() / len(feature_users)) * 100
    standard_completion = (standard_users['completed_session'].sum() / len(standard_users)) * 100
    
    print(f"Session Completion Rate with Personalization (AI DJ/Playlists): {feature_completion:.2f}%")
    print(f"Session Completion Rate without Personalization: {standard_completion:.2f}%")

if __name__ == "__main__":
    analyze_spotify_funnel()