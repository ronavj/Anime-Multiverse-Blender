import streamlit as st
import random
from datetime import datetime

if 'history' not in st.session_state:
    st.session_state.history = []
if 'favorites' not in st.session_state:
    st.session_state.favorites = []
if 'current_plot' not in st.session_state:
    st.session_state.current_plot = ""

anime_list = [
    "Astro Boy (1963)",
    "Tomorrow’s Joe (1970-1971)",
    "Princess Mononoke (1997)",
    "Akira (1988)",
    "Neon Genesis Evangelion (1995)",
    "Attack on Titan: Crimson Bow and Arrow (2014)",
    "Summer Wars (2009)",
    "Perfect Blue (1997)"
]

crossover_database = {

    ('Astro Boy (1963)', 'Attack on Titan: Crimson Bow and Arrow (2014)'): """# Astro Boy x Attack on Titan

**Blended Theme:**  
Hope and humanity in the face of extinction—can a robot's compassion save a collapsing world?

**Storyline:**  
When a transdimensional anomaly appears in the skies over Paradis Island, Astro Boy is pulled through the rift during a rescue mission in his own world. He crash-lands outside Wall Rose, where he is immediately seen as a threat by the Survey Corps. Mikasa and Armin are skeptical of the boy-shaped machine, but Eren is drawn to Astro’s power and innocence. As they navigate mistrust and discovery, Astro’s advanced sensors detect traces of artificial genetic engineering in Titan biology—prompting horrifying questions about the origins of the Titans.

The team sets out to investigate a long-buried laboratory beneath Shiganshina District, where Astro uncovers blueprints suspiciously similar to his own construction. The truth emerges: the Titans may have been a failed experiment to mass-produce sentient beings like Astro. But unlike Astro, these creations lacked a conscience.

**Visual and Audio Theme:**  
Combines the grainy, steampunk horror of AoT with Astro’s clean, monochrome sci-fi aesthetic. The music mixes melancholic strings from AoT with retro-futuristic beeps and synth from Astro’s world.

**Episode Ideas:**
1. **"Steel Among the Flesh"** – Astro rescues Jean from a Titan, earning the Scouts’ uneasy trust.
2. **"The Ghost of Shiganshina"** – The team explores the hidden lab and uncovers shocking connections.
3. **"The Last Light"** – Astro sacrifices his core to power the final defense against a new Titan breed.
""",

    ('Astro Boy (1963)', 'Akira (1988)'): """# Astro Boy x Akira

**Blended Theme:**  
The innocence of artificial life meets the chaos of unchecked evolution.

**Storyline:**  
Tokyo, 2019. Tetsuo’s psychic powers are spiraling out of control, and in desperation, Kei and Kaneda search for help beyond their world. Through a mysterious communication device left behind by the Espers, they summon Astro Boy from another dimension. At first, Astro is overwhelmed by the dystopia—Neo-Tokyo's neon lights are dimmed by its darkness.

Astro tries to reason with Tetsuo, recognizing in him the same loneliness he once felt as a robot abandoned by his creator. But Tetsuo, consumed by power and paranoia, sees Astro as a threat. Kaneda, torn between jealousy and hope, must work with Astro to reach the human inside the monster.

In a climactic battle near the Olympic Stadium, Astro and Tetsuo clash—not as enemies, but as opposing visions of humanity’s future: one built on compassion, the other on dominance.

**Visual and Audio Theme:**  
Neon-soaked urban decay meets crisp black-and-white robotics. The score merges Akira’s taiko drums and chanting with Astro’s hopeful orchestral melodies.

**Episode Ideas:**
1. **"Synthetic Messiah"** – Astro arrives and witnesses the chaos of Tetsuo’s rampage.
2. **"Three Ghosts"** – The Espers guide Astro through their history and warn of Tetsuo’s potential.
3. **"Neo-Genesis"** – Astro must decide whether to destroy Tetsuo—or save him.
""",

    ('Astro Boy (1963)', 'Princess Mononoke (1997)'): """# Astro Boy x Princess Mononoke

**Blended Theme:**  
Nature and machine in conflict—and in search of harmony.

**Storyline:**  
Astro Boy is pulled back through time and space into the forests of Muromachi Japan, landing between a boar god’s rampage and San’s ambush on a gun caravan. At first mistaken as a tool of the humans, Astro is wounded by a demon-tainted arrow and rescued by Ashitaka. As Astro learns of the deep-rooted hatred between the forest and Iron Town, he questions the role of technology in a world defined by balance.

Lady Eboshi sees Astro as a gift from the gods—an indestructible guardian who could defend her town. San sees him as a monster in disguise. Torn between the two, Astro must choose whether his advanced nature will serve conquest or coexistence.

**Visual and Audio Theme:**  
Mononoke’s painterly, naturalistic backgrounds juxtaposed with Astro’s clean, rounded lines. The soundtrack pairs traditional Japanese flute and drums with eerie synthetic undertones.

**Episode Ideas:**
1. **"Iron Spirit"** – Lady Eboshi attempts to reprogram Astro as her new protector.
2. **"Of Roots and Circuits"** – Astro explores the Deer God's realm and experiences a vision of the world's past and future.
3. **"Peace Without a Core"** – Astro disables his reactor to stop a forest fire caused by human weapons.
""",

    ('Astro Boy (1963)', 'Tomorrow’s Joe (1970-1971)'): """# Astro Boy x Tomorrow’s Joe

**Blended Theme:**  
The relentless pursuit of identity—through steel or scar.

**Storyline:**  
When Astro Boy stumbles into a rift that deposits him in 1970s Tokyo, he encounters Joe Yabuki, a boxer on the edge of self-destruction. Astro, seeking to understand human suffering, becomes fascinated by Joe’s fighting spirit, his pain, and his refusal to surrender to the cruel world.

Joe initially mocks Astro as a "tin kid," but after watching Astro save a street gang child with compassion—not strength—he begins to respect him. When Astro is forced to fight in an underground robo-boxing league to survive, Joe trains him, shaping him into a symbol of human dignity.

But as the two rise in fame, the world begins to ask: is Astro Boy still human enough to fight among men?

**Visual and Audio Theme:**  
Grainy, grayscale boxing gyms meet gleaming metal and high-tech overlays. The music is jazz-tinged soul from Joe’s era, layered with chiptune refrains.

**Episode Ideas:**
1. **"One Round Heart"** – Joe and Astro face off in the ring for the first time.
2. **"The Tin Champion"** – A corrupt promoter forces Astro into a brutal match against a war-bot.
3. **"Throw In the Soul"** – Joe risks his career to defend Astro’s right to fight.
""",

    ('Astro Boy (1963)', 'Neon Genesis Evangelion (1995)'): """# Astro Boy x Evangelion

**Blended Theme:**  
The line between pilot and weapon, soul and circuitry.

**Storyline:**  
Astro is summoned to Tokyo-3 by NERV as a last-ditch weapon when the Evas are damaged beyond repair. Gendo sees him as a controllable tool—an AI that won’t hesitate like Shinji. But Astro’s emotional depth, and his questions about right and wrong, unsettle the staff. Rei is intrigued by him. Shinji, threatened.

When a new Angel attacks with an EMP that disables all mechas, Astro’s internal reactor becomes the key to saving the city. But to do so, he must fuse with EVA-01’s core, risking both his mind and Shinji’s in a shared consciousness. In that space, they confront their traumas, learn of each other’s losses, and ultimately redefine what it means to be human.

**Visual and Audio Theme:**  
Bleak, psychosexual symbolism of Evangelion offset by Astro’s hopeful glow. Choral hymns layered with synth pulses create a tension between awe and dread.

**Episode Ideas:**
1. **"Adam and Atom"** – Astro replaces Shinji in a mission, outperforming expectations but unnerving everyone.
2. **"Soul Sync Ratio"** – Rei and Astro bond in eerie quiet while an Angel approaches.
3. **"The Electric Sea"** – A shared mental dive reveals Astro and Shinji’s deepest fears—and hopes.
""",
    
    ('Astro Boy (1963)', 'Perfect Blue (1997)'): """# Astro Boy x Perfect Blue

**Blended Theme:**  
The collapse of identity in an age of artificial performance.

**Storyline:**  
When a rogue experimental AI breaches into Astro Boy’s timeline, it brings with it the psychological residue of another world—one where a former idol named Mima is struggling with reality. Astro investigates the anomaly and finds himself pulled into a surreal version of late-90s Tokyo, where data and memory blend with dreamlike hallucinations.

Mima, plagued by voices and stalking threats, begins to see Astro as both savior and spy—an avatar of the people controlling her. Astro, programmed to empathize, tries to unravel the mystery while resisting the corrupting data that distorts even his own memory circuits. As they navigate a collapsing sense of self and surveillance, both begin to ask: what is truly real?

**Visual and Audio Theme:**  
The slick, modern anime realism of Perfect Blue warps Astro’s clean-cut designs into surreal echoes. The soundtrack is eerie synth over silence, with Astro’s classic themes rendered as haunting piano motifs.

**Episode Ideas:**
1. **"Digital Phantom"** – Astro arrives in Mima’s fragmented world, confused by time glitches and recursive scenes.
2. **"Who’s Watching Me?"** – Mima confronts a holographic Astro duplicate, unsure if he’s real.
3. **"Hardwired Illusion"** – Astro rewires his own memory to trap the AI infecting both minds.
""",

    ("Astro Boy (1963)", "Summer Wars (2009)"): """
# Astro Boy x Summer Wars

**Blended Theme:**  
Digital utopia and the ethics of artificial guardianship in a hyperconnected age.

**Storyline:**  
When OZ, the global digital infrastructure of Summer Wars, is hacked again—this time not by a rogue AI, but by a quantum rift—Astro Boy is accidentally uploaded into its core system. Simultaneously, the Jinnouchi family is once again drawn into crisis mode when their smart devices begin behaving erratically, displaying images of a strange, kind-looking boy flying through virtual cities.

Kenji, Natsuki, and Kazuma try to locate the source, only to discover that Astro isn’t the threat—he’s the last firewall protecting OZ from total collapse. An invasive virus, evolved from the remnants of Love Machine, is targeting Astro specifically, seeking to overwrite his conscience and use his advanced AI to take control of real-world infrastructures.

Astro must team up with Kazuma's avatar King Kazma in a breathtaking digital duel that spans OZ’s chaotic landscape. In the end, it’s not brute strength, but empathy—Astro’s ability to truly understand both machine and human—that turns the tide.

**Visual and Audio Theme:**  
A dazzling fusion of OZ’s surreal, vivid digital spaces with Astro’s sleek retro-futuristic silhouette. The audio layers chiptune motifs and glitched Astro Boy theme music over Summer Wars’ orchestral score.

**Episode Ideas:**
1. **"Firewalls and Family Bonds"** – The Jinnouchis trace the digital disturbance to Astro's arrival.
2. **"Code of the Brave"** – King Kazma and Astro Boy duel, then unite to defend OZ’s core.
3. **"Heart.exe"** – Astro restores empathy to the viral AI by uploading his own emotional logs.
""",

    ('Tomorrow’s Joe (1970-1971)', 'Akira (1988)'): """# Tomorrow’s Joe x Akira

**Blended Theme:**  
Fists of rebellion in a world on the brink of psychic collapse.

**Storyline:**  
Joe Yabuki wakes up in a chaotic Neo-Tokyo after being pulled through a rift mid-fight. Confused but undeterred, he wanders the city until he's swept into an underground fight ring where his raw boxing style captivates Kaneda’s gang. Meanwhile, Tetsuo, newly empowered and increasingly unhinged, takes notice of Joe as a new “champion of the people.”

As Tetsuo’s power spirals out of control, Joe becomes a symbol of physical grit in contrast to the psychic apocalypse looming. Kaneda and Joe work together to stop Tetsuo—not through explosions or machines, but through reminding him of what it meant to be just a boy with something to prove.

**Visual and Audio Theme:**  
Akira’s dystopian neon visuals meet Joe’s grainy, hand-drawn realism. Gritty jazz drums pulse beneath deep synth and city ambiance.

**Episode Ideas:**
1. **"One Punch Utopia"** – Joe wins the hearts of underground fighters in Neo-Tokyo.
2. **"Blood and Breath"** – Joe is kidnapped by Tetsuo and forced to witness psychic decay.
3. **"Ten-Count Collapse"** – Joe confronts Tetsuo, not to win—but to save what's left of him.
""",

    ('Tomorrow’s Joe (1970-1971)', 'Princess Mononoke (1997)'): """# Tomorrow’s Joe x Princess Mononoke

**Blended Theme:**  
Raw human struggle clashes with nature’s divine vengeance.

**Storyline:**  
After a near-fatal fight, Joe Yabuki awakens not in Tokyo, but in the lush, war-torn forests of Princess Mononoke. Taken in by Ashitaka, Joe learns that the rage within him mirrors the curses afflicting the land. Lady Eboshi sees in Joe the perfect soldier—fueled by anger, unyielding in combat. But San sees only another broken tool of mankind.

As battles between Iron Town and the spirits escalate, Joe is forced to confront his own nature. Is he a weapon, or a human seeking redemption?

**Visual and Audio Theme:**  
Hand-painted forestscapes, muddy and rain-soaked, envelop Joe’s stark silhouette. Traditional Japanese strings meet urban jazz percussion.

**Episode Ideas:**
1. **"Boar’s Heart, Boxer’s Soul"** – Joe trains under Ashitaka to channel his violence.
2. **"Smoke Over Iron Town"** – Joe spars with Eboshi’s guards and questions his allegiance.
3. **"The Bell Tolls Twice"** – Joe fights a cursed samurai to protect San and the forest.
""",

    ('Tomorrow’s Joe (1970-1971)', 'Attack on Titan: Crimson Bow and Arrow (2014)'): """# Tomorrow’s Joe x Attack on Titan

**Blended Theme:**  
The indomitable human spirit against monsters both inside and out.

**Storyline:**  
Joe Yabuki wakes up beyond Wall Rose after a dimensional rift tosses him into the Titan-infested world. He’s mistaken for a new warrior candidate and captured by the Survey Corps. Once tested, his raw physical ability earns him a spot among the Scouts—though he refuses to use ODM gear, preferring hand-to-hand combat.

Eren sees Joe’s reckless passion as both inspiring and dangerous. Mikasa, however, sees a broken man hiding behind bravado. Joe joins an expedition where a new breed of Titan mimics human martial arts—a twisted mirror of himself. When faced with this abomination, Joe must reclaim the meaning of human strength.

**Visual and Audio Theme:**  
A blend of muddy alleys and towering city walls with Joe’s rough 70s aesthetic. The score merges military drums with blues harmonica and distant roars.

**Episode Ideas:**
1. **"Fists and Fangs"** – Joe decks a Titan, shocking the Scouts.
2. **"Beyond the Rope"** – Joe spars with Eren, revealing deep trauma.
3. **"No Round Left"** – Joe sacrifices everything to defeat the martial Titan.
""",

    ('Tomorrow’s Joe (1970-1971)', 'Neon Genesis Evangelion (1995)'): """# Tomorrow’s Joe x Evangelion

**Blended Theme:**  
Two broken boys trying to outrun fate.

**Storyline:**  
Joe arrives in Tokyo-3 after NERV recruits him as a backup pilot for EVA-02. He scoffs at the “sync tests” and ignores orders, clashing hard with Asuka. Shinji watches from afar, intrigued and resentful of Joe’s boldness. But when an Angel attack disables the Evas, Joe saves a trapped group of civilians using nothing but grit and fists.

Gendo sees in Joe a model of raw human resolve—but one he can’t control. Joe, meanwhile, is drawn into Rei’s calm existentialism and finds purpose in the chaos NERV thrives in. As old scars resurface, Joe must decide whether to keep fighting or finally heal.

**Visual and Audio Theme:**  
Evangelion’s psychological noir meets gritty gym locker rooms and alley brawls. Haunting cello duets with the clinking of chains and boxing bells.

**Episode Ideas:**
1. **"Blue Gloves, Red Tape"** – Joe knocks out an EVA simulator in a failed sync test.
2. **"Second Impact, First Punch"** – Joe protects Shinji during an Angel breach.
3. **"Break the Core"** – Joe infiltrates the Angel to land one final punch.
""",

    ('Tomorrow’s Joe (1970-1971)', 'Perfect Blue (1997)'): """# Tomorrow’s Joe x Perfect Blue

**Blended Theme:**  
Fame, identity, and the ghosts that haunt our reflection.

**Storyline:**  
Joe is retired, older, and working as a security consultant for a studio when he’s assigned to protect Mima, a former idol slipping into madness. At first dismissive of her as “just another celebrity,” Joe comes to see in Mima the same pressures he once faced in the ring: public adoration, loneliness, and an identity that never felt truly his.

When strange hallucinations begin to affect Joe as well, he questions whether his fighting days are truly behind him—or if he’s fighting a new kind of battle altogether.

**Visual and Audio Theme:**  
Flickering CRT screens and noir cityscapes wrap around Joe’s stoic frame. Echoing footsteps and distant arena chants fade into eerie silence.

**Episode Ideas:**
1. **"Past the Bell"** – Joe shadows Mima through a chilling fan encounter.
2. **"Phantom Round"** – Joe relives past matches in his dreams, unsure of what’s real.
3. **"You Were Never Just a Boxer"** – Joe and Mima confront the masked stalker—and themselves.
""",

    ('Tomorrow’s Joe (1970-1971)', 'Summer Wars (2009)'): """# Tomorrow’s Joe x Summer Wars

**Blended Theme:**  
Old-school grit meets new-age digital war.

**Storyline:**  
Joe is accidentally uploaded into OZ when a scan of an old sports magazine he appears in is digitized into a museum archive. Now, his AI recreation begins learning and adapting. As a rogue virus resembling Love Machine reawakens, the Jinnouchi family finds themselves allied with a digital ghost of 1970s toughness.

Kazuma’s avatar, King Kazma, trains with Joe’s AI, forming an unlikely tag-team. But as Joe’s code begins to mutate into something sentient, the family faces a choice: shut him down, or let him fight for real in the new digital coliseum.

**Visual and Audio Theme:**  
Color-saturated OZ graphics contrast with grainy anime-style Joe footage brought to life. 8-bit bell rings echo alongside orchestral remixes of Joe’s classic themes.

**Episode Ideas:**
1. **"Ghost in the Ropes"** – Joe's avatar stuns OZ with a brutal knockout.
2. **"Digital Jab"** – King Kazma and Joe spar before facing the new virus boss.
3. **"Data Doesn’t Quit"** – Joe’s code burns itself out to destroy the core from within.
""",

    ('Princess Mononoke (1997)', 'Akira (1988)'): """# Princess Mononoke x Akira

**Blended Theme:**  
Nature’s gods meet science’s ghosts in a tale of rebellion and reclamation.

**Storyline:**  
After a massive temporal quake, the corrupted energy from Akira’s psychic explosion reaches the ancient forests of Mononoke’s world. The Deer God, disturbed by the unnatural force, sends San and Ashitaka to investigate the rift—leading them to a Neo-Tokyo rebuilt upon psychic experimentation.

Kaneda and San instantly clash—she sees him as a reckless emblem of industrial destruction, while he finds her feral devotion unsettling. But when a decayed spirit of Tetsuo emerges, twisted by unnatural technology, they must unite to seal the anomaly.

As Ashitaka and Kaneda form an uneasy alliance, the group must face a world where neither gods nor machines rule—but something monstrous in between.

**Visual and Audio Theme:**  
Gritty post-apocalyptic cityscapes filled with spirit haze; glitchy shakuhachi flutes meet Akira’s iconic drums in an industrial-folk fusion.

**Episode Ideas:**
1. **"The Last Spirit Reactor"** – The Deer God arrives in Tokyo, silent and menacing.
2. **"Flesh and Forest"** – San enters a lab housing experiments on nature’s DNA.
3. **"Akira’s Curse"** – Ashitaka and Kaneda fight a resurrected psychic-beast hybrid.
""",

    ('Princess Mononoke (1997)', 'Attack on Titan: Crimson Bow and Arrow (2014)'): """# Princess Mononoke x Attack on Titan

**Blended Theme:**  
Walls can’t keep out nature’s wrath.

**Storyline:**  
When the Titans breach Wall Maria, they awaken something far older beneath the earth—an ancient forest spirit buried under the city. San and Ashitaka are pulled into this world and find themselves in a decaying urban jungle choked with stone and steel. San despises the humans’ inability to coexist with nature, while Eren is drawn to her anger and defiance.

Meanwhile, the Titans begin mutating—absorbing traits of ancient beasts from San’s world. A battle looms not only for humanity’s survival, but for nature’s last stand.

**Visual and Audio Theme:**  
Dark forests spliced with abandoned wall districts. Wailing vocals over tribal percussion, layered with AoT’s brass.

**Episode Ideas:**
1. **"Roots Beneath the Walls"** – A sacred tree erupts from the ground near Trost.
2. **"Feral Pact"** – Mikasa and San clash, testing their strength and ideology.
3. **"Spirit of the Colossus"** – A new Titan appears with godlike forest powers.
""",

    ('Princess Mononoke (1997)', 'Neon Genesis Evangelion (1995)'): """# Princess Mononoke x Evangelion

**Blended Theme:**  
The Earth’s gods vs. humanity’s final gods—Evas.

**Storyline:**  
The world teeters after a failed Angel invasion destabilizes reality, merging Tokyo-3 with the sacred forest of the Deer God. San views the Evas as monstrous avatars of human arrogance. Gendo sees the forest spirits as ancient A.T. Field emitters—potential tools.

As Rei and Ashitaka bond over their quiet reflection and burdened roles, Shinji is plagued with visions of nature’s wrath and his own helplessness. With the Earth itself rising in judgment, the Evas must battle creatures born not from Angels—but from Gaia.

**Visual and Audio Theme:**  
Overgrown bio-mechanical landscapes. Organic cello harmonizes with primal drums and forest wind.

**Episode Ideas:**
1. **"Unit Roots"** – EVA-01 is swallowed by a sacred tree and reemerges with moss and antlers.
2. **"The Curse of Progress"** – Gendo tries to harness a boar spirit for weaponry.
3. **"Rain of Red Leaves"** – San and Shinji face the apocalypse on nature’s terms.
""",

    ('Princess Mononoke (1997)', 'Perfect Blue (1997)'): """# Princess Mononoke x Perfect Blue

**Blended Theme:**  
Spiritual loss and identity breakdown in an alienated world.

**Storyline:**  
Mima, escaping the traumas of celebrity life, is drawn by visions into a dreamscape forest where she meets San—who sees Mima as a specter, a lost soul drifting too far from purpose. Meanwhile, Lady Eboshi appears, reimagined as a corporate CEO spearheading an AI-driven nature reclamation project.

As Mima is torn between hallucinations of her idol self and the raw honesty of San’s life, she must navigate a surreal world where nature and mind are indistinguishable. Can she find peace in a world she doesn’t understand?

**Visual and Audio Theme:**  
Hyperreal city lights fade into forest hues; minimalist strings meet ambient rustling and breath.

**Episode Ideas:**
1. **"Dreaming in Fur and Silk"** – Mima awakens in the forest with no memory.
2. **"The Mirror Spirit"** – San and Mima face a doppelgänger idol singing in the trees.
3. **"One Step Beyond"** – Mima chooses to stay in the spirit world—reborn.
""",

    ('Princess Mononoke (1997)', 'Summer Wars (2009)'): """# Princess Mononoke x Summer Wars

**Blended Theme:**  
The ancient forest meets the digital frontier.

**Storyline:**  
When OZ begins scanning Earth’s deepest natural signatures to build a new eco-server, it accidentally taps into a spirit dimension—causing the Deer God and Kodama to digitize into the platform. Chaos spreads as forest spirits now haunt digital spaces, and modern life is disrupted by ancient codes.

San is summoned through the link, believing OZ is the Iron Town of the new age. Kenji must win her trust, and with the Jinnouchi family, protect both worlds from a viral corruption that infects the very idea of nature.

**Visual and Audio Theme:**  
Shimmering digital forests, OZ avatars gain organic flair. Music combines folk chants and chimes with digital choir layers.

**Episode Ideas:**
1. **"Avatar of the Forest"** – King Kazma fights a spirit-infused rogue user.
2. **"Glitch in the Grove"** – San explores the neural pathways of OZ.
3. **"Divine Patch"** – A ritual is held in both real and virtual worlds to seal the breach.
""",

    ('Princess Mononoke (1997)', 'Tomorrow’s Joe (1970-1971)'): """# Princess Mononoke x Tomorrow’s Joe

**Blended Theme:**  
Feral willpower meets disciplined pain.

**Storyline:**  
After an earthquake in the city, Joe finds himself in a mysterious valley where wolves roam and humans wage war with gods. Injured and disoriented, he meets San, who sees in Joe a spirit torn between man and beast.

Lady Eboshi recruits Joe for an underground arena, promising a way home if he wins. But with each fight, the spirit of the forest reaches deeper into him, awakening something primal. San sees him succumbing to bloodlust—and only she can stop him.

**Visual and Audio Theme:**  
Traditional brushwork forest fight scenes with anime boxing grit. Drums, grunts, howls, and silence in sync.

**Episode Ideas:**
1. **"The Beast Boxer"** – Joe fights a boar god in a sacred circle.
2. **"Of Smoke and Sinew"** – Eboshi tempts Joe to turn against San.
3. **"Ash and Fur"** – Joe breaks the cycle, refusing the final match.
""",

    ('Akira (1988)', 'Attack on Titan: Crimson Bow and Arrow (2014)'): """# Akira x Attack on Titan

**Blended Theme:**  
Genetic destiny and the rebellion against monstrous power.

**Storyline:**  
In the ruins of post-war Neo-Tokyo, a massive explosion cracks reality itself, linking it with the world behind the walls. Titans flood the streets of Neo-Tokyo. Kaneda’s gang fights to protect the last remnants of the city, while Eren and the Scouts arrive through the breach, stunned by a world of motorbikes and psychic fallout.

Tetsuo, already near his breaking point, becomes fascinated with the Titans—power without limits. He begins fusing Titan DNA with his own psychic abilities. The Scouts reluctantly team up with Kaneda to stop him before the fusion becomes irreversible.

As both sides realize their battles are reflections of one another, Armin and Kei devise a plan to collapse the rift—but not before one final, city-levelling confrontation.

**Visual and Audio Theme:**  
Neo-Tokyo’s nightmarish glow collides with AoT’s bleak military landscapes. Choral Titan chants and synth-rumble soundscapes meld.

**Episode Ideas:**
1. **"Through the Rift"** – Titans invade Neo-Tokyo; Kaneda meets Levi in the chaos.
2. **"Singularity Core"** – Tetsuo absorbs a Titan shifter’s power.
3. **"No Future"** – Eren and Kaneda confront Tetsuo in the crater where Akira once stood.
""",

    ('Akira (1988)', 'Neon Genesis Evangelion (1995)'): """# Akira x Evangelion

**Blended Theme:**  
The apocalypse inside the mind—told through flesh, steel, and spirit.

**Storyline:**  
In the aftermath of Tetsuo’s explosion, a dying world pulls in another—Tokyo-3. SEELE believes Akira was the first failed Instrumentality experiment and wishes to retrieve his essence to complete their plan.

Rei and Tetsuo are drawn toward each other, linked by their unstable identities and potential for destruction. Shinji, overwhelmed by Tetsuo’s unfiltered trauma, must face his own fears anew. Meanwhile, Kaneda, displaced from time, is taken in by Misato and becomes a volatile yet dependable ally.

The final confrontation isn’t physical, but metaphysical—within a shared mental landscape where choices reshape existence.

**Visual and Audio Theme:**  
Blood-red suns and concrete mechas. Evangelion's still frames erupt into Akira’s kinetic body horror. Choral whispers, static, and deep drums.

**Episode Ideas:**
1. **"First Impact, Second Explosion"** – A new energy event links Neo-Tokyo with NERV HQ.
2. **"Children of Collapse"** – Rei and Tetsuo share a psychic vision of nothingness.
3. **"Beyond Zero"** – The core of Akira and EVA-01 meet in a rebirth sequence.
""",

    ('Akira (1988)', 'Perfect Blue (1997)'): """# Akira x Perfect Blue

**Blended Theme:**  
The breakdown of self—through psychic power and psychological distortion.

**Storyline:**  
Mima is haunted not just by her idol past but by visions of a crumbling city and a boy whose power tore it apart. Her therapist believes it’s a trauma response—but these visions are real. Tetsuo’s energy has broken through dimensions, infecting minds sensitive to media and identity.

As Mima’s grasp on reality shatters, she becomes a beacon for Tetsuo’s fragmented consciousness. Kaneda enters this warped dreamscape to find what remains of his friend—and help Mima reclaim herself before the psychic residue burns her mind out completely.

**Visual and Audio Theme:**  
Mirror distortions of Tokyo streets and craters. Whispered versions of Mima’s pop songs clash with booming Akira drums.

**Episode Ideas:**
1. **"The Idol and the Aberration"** – Mima dreams of Tetsuo’s destruction, then wakes up bruised.
2. **"Broadcast Memory"** – A televised event is hijacked by Tetsuo’s voice.
3. **"Rewind Akira"** – Mima and Kaneda descend into a dream-chasm to rescue what’s left of both.
""",

    ('Akira (1988)', 'Summer Wars (2009)'): """# Akira x Summer Wars

**Blended Theme:**  
Digital utopias clash with psychic anarchy.

**Storyline:**  
OZ detects a hostile presence—energy, not code. Tetsuo’s fractured essence has found its way into the global digital ecosystem, infecting AI protocols and warping avatars into grotesque forms. The Jinnouchi family teams up with Kaneda and Kei, brought forward in time, to confront this hybrid threat.

Kazuma must evolve King Kazma into a new form capable of psychic shielding, while Kaneda once again races through a neon battlefield—only now it’s virtual. Together, they confront a digital god born from pain, ego, and unresolved power.

**Visual and Audio Theme:**  
OZ’s crystalline networks cracked with red energy pulses. The music pulses with remixed taiko drums and choral distortion.

**Episode Ideas:**
1. **"Input Overflow"** – OZ users begin mutating into energy beings.
2. **"Photon Circuit"** – Kaneda and Kazma chase Tetsuo through a collapsing server field.
3. **"Final Ping"** – A data-triggered Big Bang threatens to reboot the planet.
""",

    ('Akira (1988)', 'Tomorrow’s Joe (1970-1971)'): """# Akira x Tomorrow’s Joe

**Blended Theme:**  
Inner rage in a world where fists aren’t enough.

**Storyline:**  
Joe wakes up in Neo-Tokyo, where boxing is now illegal due to post-war trauma. He quickly finds himself brawling in the streets—and catching the attention of Kaneda. Intrigued by Joe’s intensity, Kaneda invites him into the resistance.

Tetsuo, however, sees Joe as an anomaly—human, flawed, but unyielding. He offers Joe a taste of psychic power, tempting him with a shortcut to glory. But Joe resists, choosing fists over mind tricks.

When the city threatens to crumble under Tetsuo’s rage again, it’s Joe who walks toward him—not to destroy, but to remind him of the fight that matters.

**Visual and Audio Theme:**  
Sweaty gym mats and scorched neon highways. The theme builds from low jazz riffs to explosive distortion.

**Episode Ideas:**
1. **"Steel Jaw"** – Joe demolishes a street cyborg in bare-knuckle fashion.
2. **"No Gloves, No Gods"** – Tetsuo challenges Joe with telekinetic illusions.
3. **"One Last Bell"** – Joe faces Tetsuo in a psychic ring of memory.
""",

    ('Akira (1988)', 'Princess Mononoke (1997)'): """# Akira x Princess Mononoke

**Blended Theme:**  
Man’s ambition versus Earth’s wrath.

**Storyline:**  
Tetsuo’s explosion awakens something ancient in the earth—the Deer God, furious at the trauma inflicted on the planet. San and Ashitaka travel through time, entering Neo-Tokyo to stop the spread of psychic corruption.

Eboshi sees the power of psychic energy as a resource, pitting her and Lady Miyako against nature and spirit. As Tetsuo mutates once more, drawing on the earth’s lifeblood, San makes a choice: sacrifice the god within herself to seal him.

**Visual and Audio Theme:**  
Spiritual decay overlays cyberpunk horror. Screaming nature sounds blend with analog synth collapse.

**Episode Ideas:**
1. **"Roots in Steel"** – Trees grow through skyscrapers overnight.
2. **"Red Mist"** – Tetsuo and San face off atop a dying god.
3. **"The Silence of Akira"** – Ashitaka guides Kaneda to the crater temple.
""",

     ('Neon Genesis Evangelion (1995)', 'Attack on Titan: Crimson Bow and Arrow (2014)'): """# Evangelion x Attack on Titan

**Blended Theme:**  
Humanity's will to survive collides with the burden of chosen children.

**Storyline:**  
After the 15th Angel is destroyed, another anomaly appears—this time tearing space between Tokyo-3 and Paradis Island. Titans descend into the city, and in response, NERV deploys EVA-01 to intercept. The Scouts cross over, and Gendo immediately sees the Titan shifters as potential tools.

Eren is drawn to Shinji—both victims of their father’s ambitions, both reluctant saviors. But where Eren is rage, Shinji is fear. As an Angel-titan hybrid emerges from the rift, the two must pilot EVA units—one by science, the other by rage—against the thing threatening both worlds.

**Visual and Audio Theme:**  
Bleak Evangelion surrealism, Titan gore, and apocalyptic choral-mechanical fusion.

**Episode Ideas:**
1. **"Wrath Protocol"** – Eren confronts Gendo, triggering a sync test gone wrong.
2. **"Beast and Beast"** – Levi and Asuka team up to slay a fused Angel-Titan.
3. **"Third Impact: Wall Maria"** – Shinji and Eren face their mirrored trauma inside the EVA core.
""",

    ('Neon Genesis Evangelion (1995)', 'Perfect Blue (1997)'): """# Evangelion x Perfect Blue

**Blended Theme:**  
The collapse of self in a world of surveillance and silent screams.

**Storyline:**  
Mima is selected as a guest singer for a UN morale program based in Tokyo-3. As she arrives, she begins experiencing horrifying visions—of Lilith, of Angels, of her old idol self. Her descent into delusion parallels Rei’s increasing instability, and Shinji finds himself drawn to her fragility.

Meanwhile, a cult develops online, worshipping Mima as a vessel for the new Angel. SEELE plans to use her as the new trigger for Instrumentality. But when reality bends, it’s not just the EVA pilots who must choose themselves over the voices in their heads.

**Visual and Audio Theme:**  
Jump cuts, false reflections, and ambient chaos. Mima’s pop songs fade into Gregorian chants.

**Episode Ideas:**
1. **"Idol Entry Plug"** – Mima is briefly synced with EVA-00 and relives Lilith’s memories.
2. **"Stage Exit"** – Shinji is stalked by a ghostly version of Mima in the command center.
3. **"All the World’s a Core"** – Mima chooses to delete her identity to stop Third Impact.
""",

    ('Neon Genesis Evangelion (1995)', 'Summer Wars (2009)'): """# Evangelion x Summer Wars

**Blended Theme:**  
Digital warfare meets metaphysical despair.

**Storyline:**  
When OZ's infrastructure is attacked by a logic virus resembling Angel code, the Jinnouchi family scrambles for help. NERV intervenes, inserting the MAGI supercomputers into OZ temporarily. Misato sends Rei and Shinji in via remote avatars, while Kazuma (King Kazma) must train with them to fight the data-Angel within the digital world.

As logic and emotion blur, Shinji realizes the Angel is feeding off his suppressed emotions, threatening to create an emotional singularity that would crash both worlds. The fight is no longer physical—but psychological and computational.

**Visual and Audio Theme:**  
OZ's clean, floating interfaces warped by Eva’s abstract existential iconography. Chiptune blends with organ hymns.

**Episode Ideas:**
1. **"A.T. Field Error"** – The MAGI become self-aware in OZ and try to block Rei’s access.
2. **"Kazma Test Plug"** – Kazuma briefly pilots EVA data to shield Tokyo-3 from a digital storm.
3. **"Log(out) to Live"** – Shinji must delete part of himself to expel the Angel.
""",

    ('Neon Genesis Evangelion (1995)', 'Tomorrow’s Joe (1970-1971)'): """# Evangelion x Tomorrow’s Joe

**Blended Theme:**  
Pain has shape—in memory, muscle, and machine.

**Storyline:**  
Joe is recruited by Gendo as a “pilot alternative” in the case of sync ratio failures. He scoffs at the idea of syncing with a giant robot but accepts after seeing Shinji break down during a test. He trains in NERV’s shadow boxing simulation, brawling his way through EVA feedback until he finds his match—not with a monster, but with himself.

Rei watches silently, curious about this fighter who doesn’t rely on prophecy or prophecy. Joe challenges Shinji not to run—and maybe, just maybe, finds someone worth protecting beyond the next bell.

**Visual and Audio Theme:**  
Gritty, shadow-boxing locker rooms split with psychotic overlays. Droning tones pierced by heartbeat thuds and glove snaps.

**Episode Ideas:**
1. **"Sync Ratio: 0.01"** – Joe tries EVA-02 and is rejected violently.
2. **"Counterpunch"** – Joe fights Shinji in a dream-sequence training loop.
3. **"Bell of the Lilim"** – Joe volunteers to manually deliver a core bomb on foot.
""",

    ('Neon Genesis Evangelion (1995)', 'Princess Mononoke (1997)'): """# Evangelion x Princess Mononoke

**Blended Theme:**  
The apocalypse of nature, the war of souls.

**Storyline:**  
An Angel arrives in the form of a god-beast, spreading a black forest over Tokyo-3. NERV is helpless—EVA units cannot harm the creature without going berserk. Gendo seeks to harvest its A.T. Field, but Rei and Shinji begin seeing visions of the forest’s past, and of a girl named San.

San and Ashitaka cross through into this industrial world, appalled by its corruption. They bring with them the wisdom—and judgment—of the Deer God. Evangelions must kneel not to a god, but to the planet they forgot.

**Visual and Audio Theme:**  
Overgrown EVA units, howling wind, shrine bells, reversed strings.

**Episode Ideas:**
1. **"The Green Impact"** – EVA-00 sprouts vines during sync.
2. **"Blood and Bark"** – San confronts Gendo in Terminal Dogma.
3. **"Forest of Entry Plugs"** – Shinji flees to the forest where time forgets machines.
""",

    ('Attack on Titan: Crimson Bow and Arrow (2014)', 'Perfect Blue (1997)'): """# Attack on Titan x Perfect Blue

**Blended Theme:**  
The distortion of identity on the edge of humanity’s collapse.

**Storyline:**  
Mima awakens inside a walled city with no memory of how she got there. The people around her insist she’s a newly arrived refugee—but she sees flickers of spotlights, fans, and her idol self in mirrors and windows. Eren, Mikasa, and Armin discover her wandering near the edge of Wall Rose.

As Mima unravels under pressure, she begins to believe she might be the reincarnation of a Titan shifter. A cult begins forming around her presence, believing she is the "Titan Madonna" prophesied to save or end humanity. When Mima begins having dreams of the Colossal Titan speaking to her in her own voice, the Scouts must decide whether she’s a threat, a victim, or something else entirely.

**Visual and Audio Theme:**  
Claustrophobic interiors—candlelit basements and crumbling barracks—filled with red curtains and shifting shadows. Dissonant violins pulse with AoT's military drums.

**Episode Ideas:**
1. **"Idol of the Wall"** – Mima collapses after seeing her reflection smile at her.
2. **"Titans in the Theater"** – Eren investigates a cult performing plays based on Mima’s life.
3. **"I’m Not Her"** – Mima confronts a Titan that has taken her face.
""",

    ('Attack on Titan: Crimson Bow and Arrow (2014)', 'Summer Wars (2009)'): """# Attack on Titan x Summer Wars

**Blended Theme:**  
Virtual war meets primal survival.

**Storyline:**  
After the walls fall, remnants of humanity upload what data they can to a surviving digital haven: OZ. As the last remnants of Paradis’ history are digitized, they accidentally bring traces of Titan DNA into OZ’s code.

King Kazma is forced to fight corrupted avatars taking Titan form, and Kenji must prevent a full collapse. Meanwhile, Eren is reconstructed inside OZ as a semi-conscious AI based on historical data—who begins evolving with a mind of his own.

Kazuma and Mikasa must work together to stop this new virtual “Rogue Titan” before it can escape into global control systems.

**Visual and Audio Theme:**  
Blocky OZ environments fused with sinewy Titan overlays. Choir and electronic percussion meet desperate orchestral swells.

**Episode Ideas:**
1. **"Digital Footprint"** – A Titan avatar begins consuming servers in the west wing of OZ.
2. **"Backup Rebellion"** – An archived Eren awakens and overrides security protocols.
3. **"The Last Byte"** – King Kazma delivers a virtual killing blow.
""",

    ('Attack on Titan: Crimson Bow and Arrow (2014)', 'Tomorrow’s Joe (1970-1971)'): """# Attack on Titan x Tomorrow’s Joe

**Blended Theme:**  
Fists and fury in the shadow of extinction.

**Storyline:**  
Joe arrives inside Wall Sina as part of a lost military experiment meant to create supersoldiers through sheer willpower. When he challenges a group of garrison members to a fistfight and wins, Levi takes notice.

Joe trains with the Survey Corps, learning ODM gear while mocking it as a crutch. He inspires younger recruits—especially Eren—with his grit. When a Titan begins adapting to human fighting styles, it’s Joe who steps into the ring, literally, to fight it bare-knuckled.

**Visual and Audio Theme:**  
Bleak training fields, cold air, and gritty matches under gaslight. Jazz-fused military instrumentation.

**Episode Ideas:**
1. **"Boxer of the Barracks"** – Joe wins an underground brawl watched by Hange.
2. **"One Round Titan"** – A human-modeled Titan mimics Joe’s moves.
3. **"Twelve Count Sunset"** – Joe sacrifices himself in a hand-to-hand fight to protect Wall Maria.
""",

    ('Perfect Blue (1997)', 'Summer Wars (2009)'): """# Perfect Blue x Summer Wars

**Blended Theme:**  
Digital identity, mental fracture, and the surveillance of the self.

**Storyline:**  
Years after her breakdown, Mima’s archived persona has been recreated without her consent by OZ’s entertainment division as a nostalgic virtual idol. When this AI Mima begins exhibiting erratic behavior—looping her trauma, altering other users’ memories, and building a cult following—Kenji and Natsuki are sent to investigate.

As the real Mima is pulled into OZ to confront her digital double, her memories begin to unravel once again. King Kazma must escort her through a digital labyrinth of old fan forums, fake performances, and rewritten pasts, all leading to a showdown between identity and illusion.

**Visual and Audio Theme:**  
Candy-colored OZ UI layered with ghosted VHS overlays and flickering spotlights. Minor key piano motifs warped into autotuned echoes.

**Episode Ideas:**
1. **"Replay Idol"** – Mima logs into OZ only to be greeted by herself.
2. **"Simulacrum"** – The AI begins altering accounts to mimic Mima’s memories.
3. **"Delete Me Gently"** – Mima must choose whether to erase her digital past—or embrace it.
""",

    ('Perfect Blue (1997)', 'Tomorrow’s Joe (1970-1971)'): """# Perfect Blue x Tomorrow’s Joe

**Blended Theme:**  
Fame and fighting—two lives spiraling under public eyes.

**Storyline:**  
Mima and Joe meet when she seeks private training to prepare for a dramatic boxing movie comeback. At first, Joe scoffs—he sees her as a diva playing at pain. But as Mima pushes herself, echoes of her past resurface—auditory hallucinations, flashbacks, and a stalker now targeting Joe too.

Joe realizes that Mima’s real fight is invisible—and one he understands all too well. When her stalker stages a “final scene” in a real boxing ring, Joe enters not to win, but to pull Mima back from the edge.

**Visual and Audio Theme:**  
Sweaty gyms warped by spotlight flares and warped applause. Sparse, jazz-tinged scores melt into eerie silence.

**Episode Ideas:**
1. **"Pulled Punches"** – Joe accidentally knocks Mima out in training.
2. **"Shadow in the Ring"** – A stalker impersonates Joe to lure Mima.
3. **"Round Zero"** – Joe and Mima face the final illusion together.
""",

    ('Summer Wars (2009)', 'Tomorrow’s Joe (1970-1971)'): """# Summer Wars x Tomorrow’s Joe

**Blended Theme:**  
Analog heart in a digital war.

**Storyline:**  
Joe is resurrected as a historical icon in a “Retro Fighting Legends” simulation tournament hosted on OZ. But a rogue AI modeled after Love Machine begins absorbing older datasets, gaining emotional instability from Joe’s past.

Kazuma must confront Joe’s avatar, which now believes it's alive—and still fighting toward a future it no longer has. But as the AI's memories of Joe deepen, he begins resisting the virus from within. In a desperate maneuver, Kenji pulls in the real Joe through an old boxing broadcast that syncs with the avatar’s memory, enabling Joe to fight his corrupted self and protect OZ from annihilation.

**Visual and Audio Theme:**  
Bright digital ring arenas surrounded by floating scoreboards and glitching newspaper clippings. Classic boxing ring bell overlaid with cyber glitches and orchestral tension.

**Episode Ideas:**
1. **"Data Gloves"** – Kazuma and Joe train together in a VR gym.
2. **"Shadow Boxer.exe"** – A corrupted Joe AI challenges the real Joe to a final bout.
3. **"No Upload for Old Men"** – Joe’s final punch resets the viral countdown.
"""
}



def generate_crossover(anime1, anime2):
    key = (anime1, anime2)
    reverse_key = (anime2, anime1)
    if key in crossover_database:
        return crossover_database[key]
    elif reverse_key in crossover_database:
        return crossover_database[reverse_key]
    else:
        return f"### Crossover between {anime1} and {anime2}\n\n*Coming soon...* 🚀 (This crossover hasn't been written yet.)"

st.markdown("<h1 style='text-align: center;'>✨ Anime Multiverse Blender ✨</h1>", unsafe_allow_html=True)

st.markdown("""
<div style='text-align: center;'>
    <b>Final Project for course 82279 at Carnegie Mellon University</b><br>
    <b>Made by Ronav Jaiswal</b>
</div>
""", unsafe_allow_html=True)
st.write("")
st.write("")

from PIL import Image
import streamlit as st


image = Image.open("anime_multiverse_banner_landscape.png")
st.image(image, use_container_width=True, caption="Anime Multiverse Blender")

col1, col2 = st.columns(2)

with col1:
    anime1 = st.selectbox("Select First Anime", anime_list, key="anime1_select")
with col2:
    anime2 = st.selectbox("Select Second Anime", anime_list, key="anime2_select")

if anime1 == anime2:
    st.warning("Please select two different anime!")
else:
    if st.button("Generate Crossover"):
        crossover_plot = generate_crossover(anime1, anime2)
        st.session_state.current_plot = crossover_plot
        st.session_state.history.append((datetime.now(), crossover_plot))

if st.session_state.current_plot:
    st.subheader("🔮 Current Crossover")
    st.markdown(st.session_state.current_plot)
    st.button("Save to Favorites", on_click=lambda: st.session_state.favorites.append(st.session_state.current_plot))
    st.button("Clear Current", on_click=lambda: st.session_state.update({"current_plot": ""}))

if st.session_state.history:
    st.subheader("🕰️ Past Crossovers")
    for timestamp, crossover in reversed(st.session_state.history[-10:]):
        st.markdown(f"_{timestamp.strftime('%Y-%m-%d %H:%M:%S')}_  \n{crossover}")

if st.session_state.favorites:
    st.subheader("⭐ Favorites")
    for fav in reversed(st.session_state.favorites):
        st.markdown(fav)
