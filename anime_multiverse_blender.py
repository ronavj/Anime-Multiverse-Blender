import streamlit as st
import random
import time
from datetime import datetime

# --- App State Management ---
if 'history' not in st.session_state:
    st.session_state.history = []
if 'favorites' not in st.session_state:
    st.session_state.favorites = []
if 'custom_anime' not in st.session_state:
    st.session_state.custom_anime = {}
if 'current_plot' not in st.session_state:
    st.session_state.current_plot = ""

# --- Expanded Anime Database ---
default_anime = {
    "Naruto": {
        "plot": "A young ninja seeks recognition and dreams of becoming the Hokage, the village leader.",
        "characters": ["Naruto Uzumaki", "Sasuke Uchiha", "Sakura Haruno", "Kakashi Hatake"],
        "genre": ["Action", "Adventure", "Fantasy"],
        "year": 2002
    },
    "Attack on Titan": {
        "plot": "Humanity fights for survival against giant humanoid creatures known as Titans.",
        "characters": ["Eren Yeager", "Mikasa Ackerman", "Armin Arlert", "Levi Ackerman"],
        "genre": ["Action", "Dark Fantasy", "Post-Apocalyptic"],
        "year": 2013
    },
    "Death Note": {
        "plot": "A high school student discovers a notebook that allows him to kill anyone by writing their name.",
        "characters": ["Light Yagami", "L Lawliet", "Ryuk", "Misa Amane"],
        "genre": ["Mystery", "Psychological Thriller", "Supernatural"],
        "year": 2006
    },
    # (shortened here to save space; you'd include your previous anime entries here)
    "Astro Boy": {
        "plot": "A robot boy with incredible powers fights for justice in a futuristic world.",
        "characters": ["Atom", "Dr. Tenma", "Uran", "Dr. Ochanomizu"],
        "genre": ["Science Fiction", "Adventure"],
        "year": 1963
    },
    "Princess Mononoke": {
        "plot": "A young prince becomes involved in the struggle between the gods of a forest and the humans who consume its resources.",
        "characters": ["Ashitaka", "San", "Lady Eboshi", "Jigo"],
        "genre": ["Fantasy", "Historical", "Drama"],
        "year": 1997
    },
    "Perfect Blue": {
        "plot": "A pop singer turned actress begins to lose her grip on reality when she is stalked by an obsessed fan.",
        "characters": ["Mima Kirigoe", "Rumi", "Me-Mania"],
        "genre": ["Psychological Thriller", "Drama"],
        "year": 1997
    },
    # ... Add remaining new anime (Tomorrow’s Joe, Akira, Evangelion, etc.) ...
}

if 'anime_database' not in st.session_state:
    st.session_state.anime_database = default_anime.copy()
    st.session_state.anime_database.update(st.session_state.custom_anime)

# --- Crossover Types ---
crossover_types = {
    "World Collision": "The physical worlds of both anime merge, forcing characters to adapt to new environments and threats.",
    "Character Swap": "Main characters from each series swap places, bringing their unique abilities and perspectives to a new world.",
    "Tournament Arc": "Characters from both series participate in a grand tournament to determine the strongest fighter across dimensions.",
    "Villain Team-up": "The main antagonists from both series join forces, creating a threat greater than either world has faced before.",
    "Academy/School": "Characters from both worlds attend the same school or academy, leading to friendships, rivalries, and adventures.",
    "Time Travel": "A time distortion connects both worlds across different time periods, creating paradoxes that must be resolved."
}

# --- Helper Functions ---
def get_all_anime_options():
    return [anime for anime in st.session_state.anime_database if not anime.startswith("Post-war")]

def save_to_favorites():
    if st.session_state.current_plot and st.session_state.current_plot not in st.session_state.favorites:
        st.session_state.favorites.append(st.session_state.current_plot)
        return True
    return False

def generate_episode_titles(anime1, anime2):
    return [
        f"Echoes of {anime1}",
        f"Shadows in {anime2}",
        f"Crossroads: {anime1} × {anime2}"
    ]

def generate_crossover_plot(anime1, anime2, crossover_type, tone):
    a1 = st.session_state.anime_database[anime1]
    a2 = st.session_state.anime_database[anime2]
    char1 = random.choice(a1['characters'])
    char2 = random.choice(a2['characters'])

    intro = f"## {anime1} × {anime2}: A Multiversal Encounter\n\n"

    # --- STORYLINE ---
    storyline = (
        f"### 📖 Storyline\n"
        f"When {char1} from *{anime1}* is suddenly pulled into the chaotic world of *{anime2}*, reality bends. "
        f"At the same time, {char2} finds themselves trapped in {anime1}'s universe, trying to make sense of its rules. "
        f"As the two worlds blur due to a {random.choice(['dimensional rift', 'failed experiment', 'celestial alignment'])}, unexpected friendships and rivalries form. "
        f"{char1} and {char2} slowly realize that the key to restoring balance lies in embracing each other's pasts and powers. "
        f"Allies and enemies from both sides must unite against a looming threat that neither world could face alone."
    )

    # --- THEME ---
    theme = (
        f"\n\n### 🎨 Theme\n"
        f"The crossover is styled with the hand-drawn depth of *{anime1}*, overlaid with the sleek digital edge of *{anime2}*. "
        f"The soundtrack is a fusion of {random.choice(['orchestral swells', 'synth-heavy beats', 'traditional Japanese instruments'])} and emotional piano interludes, capturing both tension and beauty."
    )

    # --- EPISODES ---
    episodes = generate_episode_titles(anime1, anime2)
    episodes_text = "\n\n### 🎬 Potential Episode Titles\n" + "\n".join([f"- {title}" for title in episodes])

    # --- Timestamp + Combine ---
    timestamp = f"\n\n*Generated on {datetime.now().strftime('%Y-%m-%d at %H:%M:%S')}*"
    full_plot = intro + storyline + theme + episodes_text + timestamp

    st.session_state.history.append({
        "plot": full_plot,
        "anime1": anime1,
        "anime2": anime2,
        "type": crossover_type,
        "tone": tone,
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    })

    st.session_state.current_plot = full_plot
    return full_plot


# --- Streamlit UI ---
st.set_page_config(page_title="Anime Crossover Generator", page_icon="🎭", layout="wide")

# Custom CSS for better styling
st.markdown("""
<style>
    .main-header {
        text-align: center;
        color: #FF4B4B;
        margin-bottom: 0;
    }
    .sub-header {
        text-align: center;
        color: #4B4BFF;
        margin-top: 0;
        margin-bottom: 2rem;
    }
    .stButton button {
        width: 100%;
    }
    .plot-container {
        background-color: #f0f2f6;
        border-radius: 10px;
        padding: 20px;
        margin-top: 20px;
    }
    .footer {
        text-align: center;
        margin-top: 3rem;
        color: gray;
        font-size: 0.8rem;
    }
</style>
""", unsafe_allow_html=True)

# Header
st.markdown("<h1 class='main-header'>🎭 Anime Multiverse Blender</h1>", unsafe_allow_html=True)
st.markdown("<h3 class='sub-header'>Create epic crossovers between your favorite anime worlds!</h3>", unsafe_allow_html=True)
st.markdown("<h3 class='sub-header'>Final Project for course 82-279 @Carnegie Mellon</h3>", unsafe_allow_html=True)

# Sidebar for additional features
with st.sidebar:
    st.header("🛠 Options & Tools")
    
    # Navigation tabs
    tab_selection = st.radio("Navigate:", ["Create Crossover", "Add Custom Anime", "View History", "Favorites"])
    
    st.markdown("---")
    
    # App info
    st.markdown("### 📊 Database Stats")
    st.markdown(f"*Total Anime Series:* {len(st.session_state.anime_database)}")
    st.markdown(f"*Custom Anime Added:* {len(st.session_state.custom_anime)}")
    st.markdown(f"*Crossovers Generated:* {len(st.session_state.history)}")
    st.markdown(f"*Favorites Saved:* {len(st.session_state.favorites)}")
    
    st.markdown("---")
    
    # Clear data options
    if st.button("Clear All History"):
        st.session_state.history = []
        st.success("History cleared!")
    
    if st.button("Clear All Favorites"):
        st.session_state.favorites = []
        st.success("Favorites cleared!")
    
    if st.button("Reset Custom Anime"):
        st.session_state.custom_anime = {}
        st.session_state.anime_database = default_anime.copy()
        st.success("Custom anime reset!")

# Main content based on sidebar selection
if tab_selection == "Create Crossover":
    
    st.header("💥 Create Your Crossover")
    
    # Create columns for selection
    col1, col2 = st.columns(2)
    
    with col1:
        anime1 = st.selectbox("First Anime Series", get_all_anime_options(), index=0)
        
        # Display info about selected anime
        if anime1:
            anime1_data = st.session_state.anime_database[anime1]
            st.markdown(f"*Plot:* {anime1_data['plot']}")
            st.markdown(f"*Year:* {anime1_data['year']}")
            st.markdown(f"*Genres:* {', '.join(anime1_data['genre'])}")
            st.markdown("*Main Characters:*")
            st.markdown(", ".join(anime1_data['characters']))
    
    with col2:
        # Filter out the first selection
        remaining_options = [a for a in get_all_anime_options() if a != anime1]
        anime2 = st.selectbox("Second Anime Series", remaining_options, index=0)
        
        # Display info about selected anime
        if anime2:
            anime2_data = st.session_state.anime_database[anime2]
            st.markdown(f"*Plot:* {anime2_data['plot']}")
            st.markdown(f"*Year:* {anime2_data['year']}")
            st.markdown(f"*Genres:* {', '.join(anime2_data['genre'])}")
            st.markdown("*Main Characters:*")
            st.markdown(", ".join(anime2_data['characters']))
    
    # Additional options
    st.markdown("### 🔄 Crossover Options")
    crossover_type = st.selectbox("Crossover Type", list(crossover_types.keys()))
    
    st.markdown(f"{crossover_types[crossover_type]}")
    
    tone = st.selectbox("Tone", ["Action-Packed", "Dramatic", "Comedic", "Mystery"])
    
    # Generation
    if st.button("🚀 Generate Epic Crossover!"):
        with st.spinner("Creating your anime crossover... Please wait!"):
            # Add a small delay for dramatic effect
            time.sleep(1)
            plot = generate_crossover_plot(anime1, anime2, crossover_type, tone)
        
        # Display plot
        st.markdown(plot)
        
        # Action buttons
        col1, col2 = st.columns(2)
        
        with col1:
            if st.button("❤ Add to Favorites"):
                if save_to_favorites():
                    st.success("Added to favorites!")
                else:
                    st.info("Already in favorites!")
        
        with col2:
            if st.button("🔄 Generate New Version"):
                with st.spinner("Creating a new version..."):
                    time.sleep(0.5)
                    new_plot = generate_crossover_plot(anime1, anime2, crossover_type, tone)
                st.markdown(new_plot)

elif tab_selection == "Add Custom Anime":
    st.header("✏ Add Your Own Anime")
    
    st.markdown("""
    Add your favorite anime that isn't in our database! Fill in the details below to create a custom entry
    that you can use in crossover generation.
    """)
    
    col1, col2 = st.columns(2)
    
    with col1:
        custom_name = st.text_input("Anime Title")
        custom_plot = st.text_area("Plot Summary")
    
    with col2:
        custom_characters = st.text_input("Main Characters (comma separated)")
        custom_genres = st.text_input("Genres (comma separated)")
        custom_year = st.number_input("Release Year", min_value=1960, max_value=2025, value=2000)
    
    if st.button("Add to Database"):
        if add_custom_anime(custom_name, custom_plot, custom_characters, custom_genres, custom_year):
            st.success(f"'{custom_name}' successfully added to the database!")
            st.info("You can now use this anime in crossover generation.")
        else:
            st.error("Please provide at least a title and plot summary.")
    
    # Display current custom anime
    if st.session_state.custom_anime:
        st.markdown("### Your Custom Anime")
        for name, data in st.session_state.custom_anime.items():
            with st.expander(name):
                st.markdown(f"*Plot:* {data['plot']}")
                st.markdown(f"*Year:* {data['year']}")
                st.markdown(f"*Genres:* {', '.join(data['genre'])}")
                st.markdown(f"*Characters:* {', '.join(data['characters'])}")

elif tab_selection == "View History":
    st.header("📜 Crossover History")
    
    if not st.session_state.history:
        st.info("You haven't generated any crossovers yet. Create one to see it here!")
    else:
        # Sort by most recent first
        sorted_history = sorted(st.session_state.history, key=lambda x: x["timestamp"], reverse=True)
        
        for i, entry in enumerate(sorted_history):
            with st.expander(f"{entry['anime1']} × {entry['anime2']} ({entry['type']}) - {entry['timestamp']}"):
                st.markdown(entry["plot"])
                
                # Add option to save to favorites
                if st.button(f"Add to Favorites", key=f"fav_hist_{i}"):
                    if entry["plot"] not in st.session_state.favorites:
                        st.session_state.favorites.append(entry["plot"])
                        st.success("Added to favorites!")
                    else:
                        st.info("Already in favorites!")

elif tab_selection == "Favorites":
    st.header("❤ Your Favorite Crossovers")
    
    if not st.session_state.favorites:
        st.info("You haven't saved any favorites yet. Add some from your generated crossovers!")
    else:
        for i, plot in enumerate(st.session_state.favorites):
            with st.expander(f"Favorite #{i+1}"):
                st.markdown(plot)
                
                # Option to remove from favorites
                if st.button("Remove from Favorites", key=f"rem_fav_{i}"):
                    st.session_state.favorites.pop(i)
                    st.success("Removed from favorites!")
                    st.rerun()

# Footer
st.markdown("""
<div class="footer">
    Ultimate Anime Crossover Generator 🎭<br>
    Created by Ronav Jaiswal
</div>
""", unsafe_allow_html=True)
