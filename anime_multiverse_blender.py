import streamlit as st
import random
import time
from datetime import datetime

if 'history' not in st.session_state:
    st.session_state.history = []
if 'favorites' not in st.session_state:
    st.session_state.favorites = []
if 'custom_anime' not in st.session_state:
    st.session_state.custom_anime = {}
if 'current_plot' not in st.session_state:
    st.session_state.current_plot = ""

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
    "My Hero Academia": {
        "plot": "In a world where most people have superpowers, a powerless boy dreams of becoming a hero.",
        "characters": ["Izuku Midoriya", "Katsuki Bakugo", "All Might", "Ochaco Uraraka"],
        "genre": ["Action", "Superhero", "School"],
        "year": 2016
    },
    "One Piece": {
        "plot": "A boy with a rubber body sails the seas with his crew in search of the ultimate treasure, the One Piece.",
        "characters": ["Monkey D. Luffy", "Roronoa Zoro", "Nami", "Usopp"],
        "genre": ["Adventure", "Fantasy", "Comedy"],
        "year": 1999
    },
    "Demon Slayer": {
        "plot": "A young man becomes a demon slayer after his family is slaughtered and his sister is turned into a demon.",
        "characters": ["Tanjiro Kamado", "Nezuko Kamado", "Zenitsu Agatsuma", "Inosuke Hashibira"],
        "genre": ["Action", "Dark Fantasy", "Martial Arts"],
        "year": 2019
    },
    "Fullmetal Alchemist": {
        "plot": "Two brothers search for the Philosopher's Stone to restore their bodies after a failed alchemical ritual.",
        "characters": ["Edward Elric", "Alphonse Elric", "Roy Mustang", "Winry Rockbell"],
        "genre": ["Adventure", "Dark Fantasy", "Steampunk"],
        "year": 2003
    },
    "Hunter x Hunter": {
        "plot": "A young boy takes a dangerous test to become a Hunter like his father, whom he never met.",
        "characters": ["Gon Freecss", "Killua Zoldyck", "Kurapika", "Leorio Paradinight"],
        "genre": ["Adventure", "Fantasy", "Martial Arts"],
        "year": 2011
    }
}

if 'anime_database' not in st.session_state:
    st.session_state.anime_database = default_anime.copy()
    st.session_state.anime_database.update(st.session_state.custom_anime)

crossover_types = {
    "World Collision": "The physical worlds of both anime merge, forcing characters to adapt to new environments and threats.",
    "Character Swap": "Main characters from each series swap places, bringing their unique abilities and perspectives to a new world.",
    "Tournament Arc": "Characters from both series participate in a grand tournament to determine the strongest fighter across dimensions.",
    "Villain Team-up": "The main antagonists from both series join forces, creating a threat greater than either world has faced before.",
    "Academy/School": "Characters from both worlds attend the same school or academy, leading to friendships, rivalries, and adventures.",
    "Time Travel": "A time distortion connects both worlds across different time periods, creating paradoxes that must be resolved."
}

def get_all_anime_options():
    """Return list of all available anime names"""
    return list(st.session_state.anime_database.keys())

def save_to_favorites():
    """Save current plot to favorites"""
    if st.session_state.current_plot and st.session_state.current_plot not in st.session_state.favorites:
        st.session_state.favorites.append(st.session_state.current_plot)
        return True
    return False

def add_custom_anime(name, plot, characters, genres, year):
    """Add custom anime to database"""
    if name and plot:
        char_list = [c.strip() for c in characters.split(',') if c.strip()]
        genre_list = [g.strip() for g in genres.split(',') if g.strip()]
        
        st.session_state.custom_anime[name] = {
            "plot": plot,
            "characters": char_list,
            "genre": genre_list,
            "year": year
        }
        

        st.session_state.anime_database = default_anime.copy()
        st.session_state.anime_database.update(st.session_state.custom_anime)
        return True
    return False

def generate_episode_titles(anime1, anime2, count=3):
    """Generate creative episode titles for the crossover"""
    anime1_data = st.session_state.anime_database[anime1]
    anime2_data = st.session_state.anime_database[anime2]
    

    all_characters = anime1_data["characters"] + anime2_data["characters"]
    all_genres = list(set(anime1_data["genre"] + anime2_data["genre"]))
    
    title_templates = [
        f"When {random.choice(anime1_data['characters'])} Meets {random.choice(anime2_data['characters'])}",
        f"The {random.choice(all_genres)} of Two Worlds",
        f"{anime1} × {anime2}: New Beginnings",
        f"The {random.choice(['Secret', 'Mystery', 'Power', 'Challenge'])} of {random.choice(all_characters)}",
        f"{random.choice(anime1_data['characters'])} vs {random.choice(anime2_data['characters'])}: {random.choice(['Showdown', 'Alliance', 'Rivalry'])}",
        f"Journey to the {random.choice(['Heart', 'Edge', 'Depths'])} of {random.choice([anime1, anime2])}",
        f"The {random.choice(['Lost', 'Hidden', 'Forbidden'])} {random.choice(['Technique', 'Artifact', 'Power'])}",
        f"{random.choice(['Dawn', 'Dusk', 'Rise', 'Fall'])} of a New {random.choice(['Hero', 'Legend', 'Era', 'Adventure'])}"
    ]
    
    return random.sample(title_templates, min(count, len(title_templates)))

def generate_crossover_plot(anime1, anime2, crossover_type, tone):
    """Generate a crossover plot based on selected parameters"""
    anime1_data = st.session_state.anime_database[anime1]
    anime2_data = st.session_state.anime_database[anime2]
    

    char1 = random.choice(anime1_data["characters"])
    char2 = random.choice(anime2_data["characters"])
    

    intro = (
        f"## {anime1} × {anime2}: {random.choice(['Worlds Collide', 'New Dimensions', 'Fated Encounter', 'Ultimate Crossover'])}\n\n"
        f"*Anime 1:* {anime1} ({anime1_data['year']}) - {', '.join(anime1_data['genre'])}\n"
        f"*Anime 2:* {anime2} ({anime2_data['year']}) - {', '.join(anime2_data['genre'])}\n\n"
    )
    

    type_desc = f"*Crossover Type:* {crossover_type}\n{crossover_types[crossover_type]}\n\n"
    

    tone_modifiers = {
        "Action-Packed": {
            "adjectives": ["epic", "intense", "explosive", "adrenaline-fueled", "high-octane"],
            "themes": ["battle", "conflict", "challenge", "conquest", "competition"]
        },
        "Dramatic": {
            "adjectives": ["emotional", "heart-wrenching", "profound", "moving", "psychological"],
            "themes": ["sacrifice", "loss", "betrayal", "redemption", "inner struggle"]
        },
        "Comedic": {
            "adjectives": ["hilarious", "absurd", "lighthearted", "zany", "ridiculous"],
            "themes": ["misunderstanding", "culture clash", "fish out of water", "unexpected friendship", "wacky adventure"]
        },
        "Mystery": {
            "adjectives": ["mysterious", "enigmatic", "puzzling", "suspenseful", "cryptic"],
            "themes": ["investigation", "conspiracy", "hidden truth", "ancient secret", "unexpected revelation"]
        }
    }
    

    adj = random.choice(tone_modifiers[tone]["adjectives"])
    theme = random.choice(tone_modifiers[tone]["themes"])
    

    if crossover_type == "World Collision":
        main_plot = (
            f"In this {adj} tale of {theme}, the worlds of {anime1} and {anime2} suddenly merge due to "
            f"{random.choice(['a cosmic anomaly', 'ancient forbidden magic', 'a villain\'s ultimate plan', 'a technological experiment gone wrong'])}. "
            f"{char1} from {anime1} and {char2} from {anime2} must form an unlikely alliance to prevent both their realities from collapsing. "
            f"As they journey across this merged landscape, they discover that "
            f"{random.choice(['their powers work differently in this combined world', 'ancient prophecies foretold their meeting', 'they share a mysterious connection', 'a greater threat looms behind the merging of worlds'])}."
        )
    
    elif crossover_type == "Character Swap":
        main_plot = (
            f"In this {adj} story centered on {theme}, {char1} from {anime1} and {char2} from {anime2} mysteriously swap places. "
            f"Now {char1} must navigate the unfamiliar challenges of {anime2}'s world, while {char2} struggles to adapt to the rules of {anime1}. "
            f"As both characters learn to use their unique abilities in new environments, "
            f"{random.choice(['they gain new perspectives on their own lives', 'they discover secrets about their own worlds', 'they realize the swap was orchestrated for a specific purpose', 'they begin to change the fate of both worlds'])}, "
            f"all while seeking a way to return home."
        )
    
    elif crossover_type == "Tournament Arc":
        main_plot = (
            f"In this {adj} tournament focusing on {theme}, fighters from the worlds of {anime1} and {anime2} are summoned to compete "
            f"by {random.choice(['a godlike entity testing the strongest across dimensions', 'mysterious organizers with hidden motives', 'ancient guardians seeking worthy successors', 'a being threatening to destroy the losing world'])}. "
            f"{char1} and {char2} find themselves as {random.choice(['rivals on opposite sides', 'reluctant teammates', 'finalists facing each other', 'pawns in a greater game'])}. "
            f"As the tournament progresses, fighters discover that the true purpose of the competition is "
            f"{random.choice(['to find champions to face a greater threat', 'to harvest the energy of powerful battles', 'to test the worthiness of both worlds to continue existing', 'to forge an alliance between dimensions'])}."
        )
    
    elif crossover_type == "Villain Team-up":

        villain1 = random.choice(anime1_data["characters"])
        villain2 = random.choice(anime2_data["characters"])
        
        main_plot = (
            f"In this {adj} confrontation centered on {theme}, the infamous {villain1} from {anime1} forms an alliance with {villain2} from {anime2}, "
            f"creating a threat that transcends dimensional boundaries. Their combined plan involves "
            f"{random.choice(['stealing powers from both worlds', 'rewriting the rules of reality', 'summoning an ancient evil', 'creating a new world under their control'])}. "
            f"Faced with this unprecedented danger, {char1} and {char2} must overcome their differences and "
            f"{random.choice(['learn to combine their unique abilities', 'gather allies from both worlds', 'rediscover forgotten powers', 'embark on a quest for a legendary weapon'])}, "
            f"before both their worlds fall to darkness."
        )
    
    elif crossover_type == "Academy/School":
        main_plot = (
            f"In this {adj} school life story exploring {theme}, characters from {anime1} and {anime2} find themselves attending the same "
            f"{random.choice(['prestigious academy', 'special training program', 'interdimensional school', 'magical institution'])}. "
            f"{char1} and {char2} are assigned as {random.choice(['roommates', 'project partners', 'rivals in the same class', 'members of competing clubs'])}. "
            f"What begins as {random.choice(['mutual animosity', 'cultural misunderstandings', 'a heated rivalry', 'reluctant cooperation'])} "
            f"gradually transforms as they face shared challenges including "
            f"{random.choice(['mysterious disappearances on campus', 'a corrupt faculty with hidden agendas', 'school tournaments with dangerous stakes', 'an ancient secret hidden beneath the school grounds'])}."
        )
    
    elif crossover_type == "Time Travel":
        main_plot = (
            f"In this {adj} time-bending adventure centered on {theme}, a disruption in the temporal continuum connects the worlds of {anime1} and {anime2} across different eras. "
            f"{char1} finds {random.choice(['ancient records', 'future technology', 'prophetic visions', 'mysterious messages'])} that reveal "
            f"connections to {char2}'s world. As they unravel the mystery, they discover that "
            f"{random.choice(['their worlds share a common ancestry', 'current events are echoing a past catastrophe', 'future threats have roots in both their timelines', 'a time traveler is manipulating both histories'])}. "
            f"Together, they must navigate the complex web of cause and effect to "
            f"{random.choice(['restore the proper timeline', 'prevent a disaster that threatens both worlds', 'stop an entity feeding on temporal anomalies', 'create a new future for both realities'])}."
        )
    

    episodes = generate_episode_titles(anime1, anime2)
    episodes_section = "## Potential Episode Titles\n" + "\n".join([f"- {i+1}. {title}" for i, title in enumerate(episodes)])
    

    dynamics = (
        f"## Key Character Dynamics\n"
        f"- *{char1} & {char2}:* {random.choice(['Reluctant allies who gradually develop mutual respect', 'Instant rivals with contrasting philosophies', 'Kindred spirits who recognize similarities in their journeys', 'Master and student relationship as one helps the other grow'])}\n"
        f"- *Powers & Abilities:* {random.choice(['Their abilities complement each other in unexpected ways', 'They must learn to combine their techniques to create new powers', 'What works in one world follows different rules in another', 'The limitations of their abilities are removed in this crossover'])}\n"
        f"- *Growth & Development:* {random.choice(['Both characters confront their personal weaknesses through this encounter', 'Their beliefs and values are challenged by exposure to a different world', 'They discover new applications for their abilities', 'Meeting counterparts from another world forces them to reconsider their paths'])}"
    )
    

    timestamp = f"\n\n*Generated on {datetime.now().strftime('%Y-%m-%d at %H:%M:%S')}*"
    

    full_plot = intro + type_desc + main_plot + "\n\n" + episodes_section + "\n\n" + dynamics + timestamp
    

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


st.set_page_config(page_title="Anime Crossover Generator", page_icon="🎭", layout="wide")


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


st.markdown("<h1 class='main-header'>🎭 Ultimate Anime Crossover Generator</h1>", unsafe_allow_html=True)
st.markdown("<h3 class='sub-header'>Create epic crossovers between your favorite anime worlds!</h3>", unsafe_allow_html=True)


with st.sidebar:
    st.header("🛠 Options & Tools")
    

    tab_selection = st.radio("Navigate:", ["Create Crossover", "Add Custom Anime", "View History", "Favorites"])
    
    st.markdown("---")
    
    st.markdown("### 📊 Database Stats")
    st.markdown(f"*Total Anime Series:* {len(st.session_state.anime_database)}")
    st.markdown(f"*Custom Anime Added:* {len(st.session_state.custom_anime)}")
    st.markdown(f"*Crossovers Generated:* {len(st.session_state.history)}")
    st.markdown(f"*Favorites Saved:* {len(st.session_state.favorites)}")
    
    st.markdown("---")
    
    
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


if tab_selection == "Create Crossover":
    
    st.header("💥 Create Your Crossover")
    

    col1, col2 = st.columns(2)
    
    with col1:
        anime1 = st.selectbox("First Anime Series", get_all_anime_options(), index=0)
        

        if anime1:
            anime1_data = st.session_state.anime_database[anime1]
            st.markdown(f"*Plot:* {anime1_data['plot']}")
            st.markdown(f"*Year:* {anime1_data['year']}")
            st.markdown(f"*Genres:* {', '.join(anime1_data['genre'])}")
            st.markdown("*Main Characters:*")
            st.markdown(", ".join(anime1_data['characters']))
    
    with col2:
        remaining_options = [a for a in get_all_anime_options() if a != anime1]
        anime2 = st.selectbox("Second Anime Series", remaining_options, index=0)
        

        if anime2:
            anime2_data = st.session_state.anime_database[anime2]
            st.markdown(f"*Plot:* {anime2_data['plot']}")
            st.markdown(f"*Year:* {anime2_data['year']}")
            st.markdown(f"*Genres:* {', '.join(anime2_data['genre'])}")
            st.markdown("*Main Characters:*")
            st.markdown(", ".join(anime2_data['characters']))
    

    st.markdown("### 🔄 Crossover Options")
    crossover_type = st.selectbox("Crossover Type", list(crossover_types.keys()))
    
    st.markdown(f"{crossover_types[crossover_type]}")
    
    tone = st.selectbox("Tone", ["Action-Packed", "Dramatic", "Comedic", "Mystery"])
    

    if st.button("🚀 Generate Epic Crossover!"):
        with st.spinner("Creating your anime crossover... Please wait!"):

            time.sleep(1)
            plot = generate_crossover_plot(anime1, anime2, crossover_type, tone)
        
        st.markdown(plot)
        
  
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
  
        sorted_history = sorted(st.session_state.history, key=lambda x: x["timestamp"], reverse=True)
        
        for i, entry in enumerate(sorted_history):
            with st.expander(f"{entry['anime1']} × {entry['anime2']} ({entry['type']}) - {entry['timestamp']}"):
                st.markdown(entry["plot"])
                
  
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
                
  
                if st.button("Remove from Favorites", key=f"rem_fav_{i}"):
                    st.session_state.favorites.pop(i)
                    st.success("Removed from favorites!")
                    st.rerun()


st.markdown("""
<div class="footer">
    Ultimate Anime Crossover Generator 🎭<br>
    Created by Ronav Jaiswal
</div>
""", unsafe_allow_html=True)
