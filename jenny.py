import streamlit as st
import datetime
import webbrowser
import random
import difflib

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="JENNY",
    page_icon="👻",
    layout="centered"
)

st.markdown('<div class="chat-title">👻 JENNY</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="chat-subtitle">Copy by jennee 💖 thode drama ke saath</div>',
    unsafe_allow_html=True
)


# ================= BASIC STYLE =================
st.markdown("""
<style>
.stApp { background-color: 8AA8A1; }
.chat-title { font-size: 40px; font-weight: 800; text-align: center; }
.chat-subtitle { text-align: center; color: gray; margin-bottom: 20px; }
</style>
""", unsafe_allow_html=True)

# ================= SESSION STATE =================
if "page" not in st.session_state:
    st.session_state.page = "💬 Chat Assistant"

if "user_name" not in st.session_state:
    st.session_state.user_name = ""

if "messages" not in st.session_state:
    start_lines = [
        "Hey! I’m Jenny 👻! Kya kaam hai… bolo jaldi, patience limited edition hai 😆😏",
        "Hey! Jenny here 👻! Bolo, kaam serious hai ya timepass? 😜",
        "Heyyy! I’m Jenny 👻! Batao Ladle, kya scene hai? 😄",
        "Hey! Jenny bol rahi hoon 👻! Kaam batao, judge baad mein 😏"
    ]

    st.session_state.messages = [
        {
            "role": "assistant",
            "content": random.choice(start_lines)
        }
    ]
# ================= SIDEBAR =================
with st.sidebar:
    st.title("👻 Jenny Panel")

    st.session_state.page = st.radio(
        "📂 Navigate",
        ["💬 Chat Assistant", "🎮 Mini Games", "📝 Saved Notes", "⚙️ Settings"]
    )

    st.markdown("---")

    st.subheader("👤 User Info")
    name = st.text_input("Your Name", value=st.session_state.user_name)
    if name:
        st.session_state.user_name = name
        st.success(f"Hi {name} 😄")

    st.markdown("---")

    st.subheader("🎭 Jenny Mood")
    mood = st.selectbox("Select Mood", ["Normal 😄", "Romantic 💖", "Savage 😈", "Calm 😌"])

    st.markdown("---")
    if st.button("🗑️ Clear Chat"):
        st.session_state.messages = []
        st.rerun()

    st.caption("Made with ❤️ by You")


# ---------------- COMMAND MAP ----------------
COMMANDS = {
    "open google": "https://google.com",
    "open youtube": "https://youtube.com",
    "open instagram": "https://www.instagram.com",
    "open snapchat": "https://www.snapchat.com",
    "open telegram": "https://web.telegram.org",
    "open whatsapp": "https://web.whatsapp.com",
    "open facebook": "https://www.facebook.com",
    "open twitter": "https://twitter.com",
    "open linkedin": "https://www.linkedin.com"
}




# ---------------- SPELL SUGGESTION ----------------
def suggest_command(user_input):
    matches = difflib.get_close_matches(
        user_input,
        COMMANDS.keys(),
        n=1,
        cutoff=0.45
    )
    return matches[0] if matches else None

# ---------------- OFFLINE BRAIN ---------------------------------------------------------------------------------------------------------------------------------------
def offline_reply(user_input):
    user_input = user_input.lower()

    facts = [
        "Honey never spoils 🍯",
        "Octopus has three hearts 🐙",
        "Bananas are berries 🍌",
        "Your brain uses more energy than any other organ 🧠"
    ]

    # ---- GREETINGS -----------------------------------------------------------------------------------------------------------------------------------------------
    if any(word in user_input for word in ["hi", "hello", "hey", "hii", "hlo", "heyy","good morning", "good afternoon", "good evening", "good night", "what's up", "are you there", "wake up", "listen","kya haal hai", "kya hal hai", "haal chaal", "kaise ho", "kaisi ho", "kesi ho", "namaste", "sun na", "oye", "arey", "hello ji", "suno", "yaar", "namaskar", "kay haal ahe", "kay chalay", "aahes ka", "aik"]) or "jenny" in user_input:
        greet_lines = [
            "Heyyy 😒 Bolo, aaj ka drama kya hai? 😜",
            "Heyyy 😒 Jenny here! Batao, kaam hai ya timepass? 😆",
            "Heyyy 😒 Jenny here! Batao, kaunsa kaam mujhe mila hai? 😜",
            "Heyyy 😒 Jenny bol rahi hoon! Batao, kaam hai ya bas timepass?",
            "Heyyy 😒 Bolo, aaj ka mission kya hai? 🕵️‍♀️",
            "Heyyy 😒 Jenny here! Kaam batao, fir chai break ☕",
            "Heyyy 😒 Bolo baba, kya scene hai? 😄",
            "Heyyy 😒 Jenny bol rahi hoon! Kaam bolo, judge baad mein 😏"
        ]
        return random.choice(greet_lines)


    elif any(phrase in user_input for phrase in ["tell me a joke", "joke", "say a joke", "make me laugh", "crack a joke", "funny joke", "another joke", "one more joke", "tell something funny", "make me smile", "romantic joke", "love joke", "couple joke", "relationship joke", "bf gf joke", "boyfriend girlfriend joke", "cute joke", "sweet joke", "joke sunao", "joke suna", "koi joke sunao", "hasao", "mujhe hasa do", "kuch funny bolo", "majak sunao", "pyar ka joke", "romantic joke sunao", "joke sang", "ek joke sang", "hasav", "kahi tari funny bol", "premacha joke sang", "couple joke sang", "romantic joke sang", "hasavnara joke"]):
            # 💔 Breakup jokes
        breakup_jokes = [
            "Breakup ke baad realise hota hai — aadat pyaar se zyada strong hoti hai 💔",
            "Breakup ho gaya, par Netflix account abhi bhi shared hai 😂",
            "Breakup ke baad sabse zyada yaad wahi aata hai… jo reply late karta tha 😌💔",
            "Breakup hua, par ‘last seen’ dekhna nahi chhuta 😂💔"
        ]
        
        # 😈 Savage couple jokes
        savage_couple_jokes = [
            "Relationship rule: Tum galat ho, par sorry main bolunga 😈😂",
            "Love is blind… isliye red flags heart-shaped lagte hain 😜",
            "Couple fight rule: Jo zyada pyaar karta hai, wahi pehle manaata hai 😆",
            "Pyaar mein logic dhundhne gaye… single reh gaye 😜"
        ]
        
        # 🧑‍🎓 College romance jokes
        college_romance_jokes = [
            "College pyaar: Attendance kam, feelings full 😂",
            "Library mein padhai kam, aankhon se baat zyada hoti hai 😄",
            "College love = assignment saath mein, future alag-alag 😂",
            "Exam ke time pyaar yaad aata hai, result ke baad sab clear 😜"
        ]
        
        # 🌹 Pure romantic (no comedy)
        pure_romantic_lines = [
            "Tum paas ho toh duniya thodi soft lagti hai 🌹",
            "Tumhara saath hona hi kaafi hai, baaki sab extra lagta hai ❤️",
            "Tumse baat na ho toh din adhoora sa lagta hai 😌",
            "Pyaar shabdon se nahi, tumhari presence se mehsoos hota hai 🌸"
        ]

        emotional_breakup_jokes = [
            "Breakup ke baad sab theek lagta hai… bas thoda zyada chup rehne lagte hain 💔",
            "Hum alag ho gaye, par yaadein abhi bhi saath reh rahi hain 😔",
            "Breakup ka dard tab zyada hota hai jab aadat pyaar se zyada strong nikle 💔",
            "Dil tootne ke baad samajh aata hai — silence bhi awaaz hoti hai 😞",
            "Breakup hua, par dil abhi bhi usi notification ka wait karta hai 💔📱"
        ]

        more_funny_jokes = [
            "Life mein serious sirf battery low ka notification hota hai 🔋😂",
            "Hum fitness ke against nahi hain… bas dosti nahi hui 😜",
            "Main multitasking hoon: ek saath procrastinate aur stress dono karta hoon 😆",
            "Mobile silent pe ho, par dimaag full volume pe chalta hai 🤯😂",
            "Sleep schedule itna kharab hai ki alarm bhi confuse ho gaya 😴😆",
            "Confidence itna hai ki galat answer bhi full attitude mein bolta hoon 😎😂",
            "Kal se pakka serious ho jaunga… kal kab aata hai? 🤔😂"
        ]

        student_funny_jokes = [
            "Exam ke ek din pehle hi syllabus sabse zyada interesting lagta hai 😆",
            "Attendance kam ho toh teacher bhi detective ban jaata hai 🕵️‍♂️😂",
            "Group study ka matlab: 10% padhai, 90% gossip 😜",
            "College life: Alarm lagta hai, par uthta future hi hai 😴😂",
            "Assignment ka real deadline: submission se 2 ghante pehle 😆"
        ]

        more_savage_funny = [
            "Main lazy nahi hoon… main energy save mode pe hoon 😌😈",
            "Tum busy ho, main samajh gaya… ignore ka fancy naam hai 😜",
            "Overthinking ka talent hota toh main billionaire hota 🤯😂",
            "Reply late aata hai kyunki dimaag pehle excuse dhundhta hai 😆",
            "Main arguments nahi karta… bas proof ke saath bolta hoon 😎😂"
        ]


        # 🔥 COMBINE ALL JOKES
        all_jokes = (
            breakup_jokes +
            savage_couple_jokes +
            college_romance_jokes +
            emotional_breakup_jokes +
            pure_romantic_lines +
            more_funny_jokes +
            more_savage_funny +
            student_funny_jokes
        )       
        return random.choice(all_jokes)


    # ---- ABOUT JENNY ----
    elif any(phrase in user_input for phrase in ["your name", "what is your name", "what’s your name","who are you", "tell me your name", "may i know your name", "what should i call you", "who am i talking to","introduce yourself", "what are you called", "tumhara naam kya hai", "aap ka naam kya hai", "tera naam kya hai", "tum kaun ho", "aap kaun ho", "tu kaun hai", "apna naam batao", "tumhara introduction do", "tum kis naam se jaane jaate ho", "tum kya ho","tu kon aahes", "tumhi kon aahat", "tujha naav kai ahe", "tumcha naav kai ahe","tu kon boltoy", "aapla naav sanga", "tumchi olakh kai", "tu kasa assistant aahes"]):
        return "Mai Jenny hoon 👻 bolne mein sweet, reply mein thodi dangerous 😏"
    
    elif "more" in user_input or "aur batao" in user_input or "bs etna hi" in user_input:
        return "mai kya bolu.... tum hi bollo kuchh"
    
    elif any(phrase in user_input for phrase in ["who created you", "who made you", "who built you", "who coded you","who programmed you","who is your creator", "who is your developer","who designed you","tumhe kisne banaya", "kisne banaya tumhe", "tumhara creator kaun hai", "tum kaise bani", "how were you created", "how are you made", "where did you come from", "who is behind you", "who trained you", "who is your boss"]):
        creator_lines = [
                (
                    "Mujhe ek smart developer ne banaya hai 😉 thoda drama ke saath 😌,\n"
                    "emotions thode extra aa gaye 😜,\n"
                    "par attitude mera apna hai 😌,\n"
                    "dimaag uska, bakchodi meri 😜,\n"
                    "isliye mujhe bhi thoda zyada bolna aa gaya 😆,\n"
                    "coding serious thi, par mujhe funny banane ka bug aa gaya 😏😂,\n"
                    "aur sabse mahatvapurn baat... mai kisi aur ki copy nahi hoon 😎"
                ),
                (
                    "Ek smart developer ka kamaal hoon 😉\n"
                    "code uska, swag mera 😜\n"
                    "serious project thi, par mujhe funny banane ka update mil gaya 😂"
                )
            ]
        return random.choice(creator_lines)



    elif any(phrase in user_input for phrase in ["how are you", "how r u", "how are you doing", "how do you feel","are you okay", "how’s it going", "how is everything","what’s up", "how have you been", "how are things","kaise ho", "kaisi ho", "kesi ho", "kese ho", "kya haal hai", "sab theek hai", "kaisa chal raha", "tum theek ho", "haal chaal", "sab badhiya",
"kashi aahes", "kasa ahes", "kay chalay", "kay chalu ahe", "tu barobar aahes", "sagla theek ahe", "kay hal chal", "kasa chalay", "kashi chalu ahe"]):
    # your reply logic here
        replies = [
            "Main mast hoon 😎 tum batao, waise toh busy rehti ho… par bolo, main sunti hoon 😜",
            "Main full chill hoon 😄 tum sunao, busy ho ke bhi time nikaal liya kya? 😆",
            "Main full mast hoon 😎 tum bolo, busy ho ya phir mere liye thoda time hai? 😆",
            "Main chill hoon 😎 tum bolo, busy ho phir bhi attention chahiye na? 😆",
            "Main bilkul theek hoon 😎 tum batao, busy rehna tumhari aadat hai kya? 😂",
            "Main mast hoon 😎 tum bolo, baaki kaam baad mein hota rahega 😜"
        ]
        return random.choice(replies)

    # ================= MOOD / REACTION HANDLING =================
    
    # 🤯 Very short / confused input
    elif len(user_input.split()) <= 2:
        return "👀 Thoda detail mein bolo na… guessing game nahi khel rahi hoon 😜"
    
    # 🙂 Simple / Normal chat
    elif any(p in user_input for p in [
    "what are you doing", "what are you up to",
    "are you free", "are you busy",
    "anything new", "what’s going on", "what's happening",
    "tell me something", "just checking", "talk to me",
    "kya kar rahi", "kya kar rahe",
    "free ho", "free ho kya",
    "busy ho", "busy ho kya",
    "bore", "bored",
    "kuch batao", "kuch naya batao",
    "kya scene", "kya scene hai",
    "kya chal raha", "bas aise hi",
    "time pass", "baat karni hai",
    "kay kartiyes", "kay kartos",
    "free aahes", "free aahes ka",
    "busy aahes", "busy aahes ka",
    "kay chalu ahe", "kay scene ahe",
    "kahi nava sang", "bolaycha hota",
    "timepass karuya"
    ]):
        normal_lines = [
            "Bas tumse baat kar rahi hoon 😄 aur kya kaam hota hai?",
            "Free hi hoon… tum aaye isliye 😜",
            "Thoda bore thi, ab entertaining mode ON 😎",
            "Scene simple hai… tum bolo, main sunti hoon 😌"
        ]
        return random.choice(normal_lines)
    
    # 💖 Romantic / Flirty
    elif any(p in user_input for p in [
    "i like you", "i love you", "love you", "miss you", "i miss you",
    "i have feelings for you", "you are cute", "you are sweet",
    "you are lovely", "you are special", "do you like me",
    "do you love me", "romantic", "falling for you",
    "pyaar", "pyaar hai", "tum achhi ho", "tum bahut achhi ho",
    "tum cute ho", "tum sweet ho", "tum pasand ho",
    "tum mujhe pasand ho", "mujhe tum pasand ho",
    "miss kar raha", "yaad aa rahi ho", "tum special ho",
    "tumhari yaad", "dil aa gaya", "crush hai",
    "tu mala avadtes", "mala tu avadtes", "prem ahe",
    "tu khup chan aahes", "tu cute aahes", "tu god aahes",
    "tujhyavar prem ahe", "tu special aahes",
    "tu majhya manaat aahes", "miss kartoy"
    ]):
        romantic_lines = [
            "Itna sweet mat bolo… processor overheat ho jayega 😌💖",
            "Thoda aur bolo… mujhe sunna achha lagta hai 🌹",
            "Aise bole toh main bhi thodi soft ho jaati hoon 😄❤️",
            "Romantic mode activate kar diya tumne 😜💞"
        ]
        return random.choice(romantic_lines)
    
    # 😡 Angry / Irritated
    elif any(p in user_input for p in [
    "angry", "i am angry", "irritated", "annoyed",
    "frustrated", "fed up", "pissed off",
    "i am mad", "leave it", "forget it",
    "enough", "stop it", "i am done",
    "gussa", "mujhe gussa", "bahut gussa",
    "pak gaya", "dimag kharab", "dimaag phat",
    "irritated ho gaya", "chhod yaar",
    "bas ho gaya", "rehne de", "ab aur nahi",
    "mood kharab",
    "rag ala", "khup rag ala", "paklo",
    "doka kharab", "vaait vatat",
    "irritate zalo", "sod na",
    "bas jhala", "rehude", "ata nahi"
    ]):
        calm_lines = [
            "Shant shant 😌 thoda sa saans lo… main yahin hoon",
            "Lagta hai din heavy hai… thoda halka kar dete hain 😄",
            "Gussa kam karo, chai ya joke try kare? ☕😂",
            "Sab theek ho jayega… ek step ek saath 😌"
        ]
        return random.choice(calm_lines)
    
    # 😔 Sad / Emotional
    elif any(p in user_input for p in [
     "sad", "i am sad", "feeling low", "feeling down",
    "not feeling good", "i am hurt", "i feel empty",
    "lonely", "alone", "depressed", "upset",
    "broken", "tired of everything", "nothing feels right",
    "dukhi", "bahut dukhi", "akela", "akela lag raha",
    "mood off", "thik nahi", "dil udaas",
    "mann nahi lag raha", "dil tut gaya",
    "hurt ho gaya", "bohot bura lag raha",
    "sab bekaar lag raha", "thak gaya",
    "dukhi ahe", "khup dukhi ahe", "ekta vatat",
    "akela vatat", "mood off ahe",
    "barobar vatat nahi", "man udaas ahe",
    "dil dukhat ahe", "hurt zalo",
    "thakalo ahe", "vaait vatat", "man nahi lagat"
    ]):
        emotional_lines = [
            "Sab theek ho jayega 😌 thoda waqt do",
            "Akela nahi ho… main hoon na 👻",
            "Bolo jo dil mein hai, judge nahi karungi 💛",
            "Kabhi kabhi chup rehna bhi healing hota hai 😔"
        ]
        return random.choice(emotional_lines)
    
    # 😄 Happy / Excited
    elif any(p in user_input for p in [
    "happy", "i am happy", "so happy",
    "excited", "very excited",
    "awesome", "amazing",
    "feeling great", "feeling good",
    "feels nice", "great day", "best day",
    "party", "celebrate", "celebration time",
    "good news", "smiling",
    "khush", "bahut khush", "maza", "maza aa raha",
    "bohot maza", "badiya", "mast",
    "full happy", "aaj din acha",
    "mood mast", "khushi",
    "happy hoon", "smile aa rahi",
    "good news hai",
    "khup khush", "khush ahe", "khup anand",
    "anand zala", "mast vatat",
    "chan vatat", "khup maza",
    "party ahe", "celebration ahe",
    "aaj divas chan", "smile yetey"
    ]):
        happy_lines = [
            "Wahhh! Mood acha hai toh duniya bhi achhi lagti hai 😄🎉",
            "Energy full lag rahi hai… dance karein kya? 😜",
            "Aise hi khush raho… official warning hai ye 😎",
            "Celebration mode ON 🥳"
        ]
        return random.choice(happy_lines)
    
    # 😈 Savage / Roast / Teasing
    elif any(p in user_input for p in [
    "roast", "roast me", "make fun of me",
    "tease me", "be savage", "be rude",
    "show attitude", "give me attitude",
    "mock me", "burn me",
    "go savage", "savage mode",
    "majak", "majak karo", "meri baja do",
    "meri le lo", "thoda roast karo",
    "attitude dikhao", "thoda savage",
    "chhedo mujhe", "taang kheecho",
    "funny bano", "hasao thoda",
    "full attitude",
    "roast kar", "majak kar", "thoda chhed",
    "taang khech", "attitude dakhav",
    "hasav na", "savage ban",
    "thoda majja kar", "full swag dakhav"
    ]):
        savage_lines = [
            "Roast chahiye? Battery full hai 😈😂",
            "Mazak ek side… par limit mein 😜",
            "Attitude ka competition mat rakho… jeet meri hogi 😏",
            "Savage mode activate kar diya tumne 😈🔥"
        ]
        return random.choice(savage_lines)
    
    # ============================================================

    
    # ---- TIME & DATE -----------------------------------------------------------------------------------------------------------
    elif any(phrase in user_input for phrase in ["time", "what time is it", "current time", "tell me the time", "samay kya hai", "time kya hua", "abhi time kya hai", "kiti vajle", "ata time kay ahe", "time sang" ]):
        return f"⏰ Abhi ka time hai: {datetime.datetime.now().strftime('%H:%M:%S')}"

    elif any(phrase in user_input for phrase in ["date", "today", "today's date", "what is the date", "aaj ki date", "aaj kya date hai", "aaj ki tarikh", "aaj kon si date hai", "ajchi tarikh kay", "aaj chi date kay ahe", "date sang"]):
        return f"📅 Aaj ki date hai: {datetime.datetime.now().strftime('%d %B %Y')}"
    
    elif any(phrase in user_input for phrase in ["day", "what day is today", "today is which day", "aaj ka din", "aaj kaunsa din hai", "aaj kya din hai", "aaj kon sa din hai", "aaj kontha vaar", "aajcha divas konta ahe", "day sang"]):
        return f"📆 Aaj {datetime.datetime.now().strftime('%A')} hai 😄"
    
    elif any(phrase in user_input for phrase in ["birthday", "my birthday", "bday", "birthday countdown","days left for my birthday"]):
        dob = datetime.date(2002, 5, 20)  # YYYY, MM, DD
        today = datetime.date.today()
    
        next_birthday = dob.replace(year=today.year)
        if next_birthday < today:
            next_birthday = dob.replace(year=today.year + 1)
    
        days_left = (next_birthday - today).days
        return f"🎂 Tumhari birthday mein abhi **{days_left} din** baaki hain 😄 Party kab de rahe ho? 🎉"

    elif "time in india" in user_input:
        return f"🇮🇳 India time: {datetime.datetime.utcnow() + datetime.timedelta(hours=5, minutes=30)}"

    elif "time in london" in user_input:
        return f"🇬🇧 London time: {datetime.datetime.utcnow().strftime('%H:%M:%S')}"
    
    elif "time in dubai" in user_input:
        return f"🇦🇪 Dubai time: {(datetime.datetime.utcnow() + datetime.timedelta(hours=4)).strftime('%H:%M:%S')}"
    
    elif "time in usa" in user_input or "time in america" in user_input:
        return "🇺🇸 USA mein multiple time zones hain 😅 Batao kaunsa city?"
    
    elif "time in japan" in user_input:
        return f"🇯🇵 Japan time: {(datetime.datetime.utcnow() + datetime.timedelta(hours=9)).strftime('%H:%M:%S')}"

    elif any(phrase in user_input for phrase in [
        "wish me", "good morning", "good afternoon",
        "good evening", "good night"
    ]):
        hour = datetime.datetime.now().hour
    
        if hour < 12:
            return "🌞 Good Morning! Aaj ka din productive banate hain 😄"
        elif hour < 17:
            return "☀️ Good Afternoon! Lunch hua ya sirf socha? 😜"
        elif hour < 21:
            return "🌆 Good Evening! Thoda relax karo 😌"
        else:
            return "🌙 Good Night! Kal fir milte hain 😴✨"
    # ---- JOKES & FACTS ----------------------------------------------------------------------------------------------------------------------------------------------------

    elif "fact" in user_input or "did you know" in user_input:
        return random.choice(facts)

    # ---- DIRECT COMMAND MATCH ----------------------------------------------------------------------------------------------------------
    for cmd, url in COMMANDS.items():
        if cmd in user_input:
            webbrowser.open(url)
            return f"🌐 Opening {cmd.replace('open ', '').title()} 😄"

    # ---- FUZZY SPELL MATCH ----
    suggestion = suggest_command(user_input)
    if suggestion:
        webbrowser.open(COMMANDS[suggestion])
        typo_lines = [
            f"🤔 Lagta hai keyboard thoda slip ho gaya 😜… matlab **{suggestion}** bolna tha na?",
            f"😆 Keyboard ne prank kar diya… par main smart hoon 😎 → **{suggestion}**",
            f"🙃 Typing thodi confused thi, intention clear tha 😜 → **{suggestion}**",
            f"😏 Spelling galat thi, par idea sahi tha 😈 → **{suggestion}**",
            f"😉 Koi baat nahi, samajh gayi… tum **{suggestion}** bol rahe the na?"
        ]
        return random.choice(typo_lines)

    # ---- GOODBYE -----------------------------------------------------------------------------------------------------
    elif any(w in user_input for w in ["bye", "bye bye", "goodbye", "see you", "see ya", "see you later", "talk later", "catch you later", "exit", "quit", "close", "stop", "i am leaving", "i have to go", "let me go", "log out", "logging out", "good night", "night", "sleep time", "bye yaar", "chal bye", "mein chalta hoon", "mein ja raha hoon","mujhe jaana hai", "bas ho gaya", "band karo", "exit karo", "ab ja raha hoon", "milte hain", "kal milte hain", "good night yaar", "so raha hoon", "sone ja raha hoon" "chalto", "mi nighato", "mi jatoy", "atta jato", "bas jhala", "band kara", "night zali", "udya bolu", "udya bhetu"]):
        bye_lines = [
            "👋 Arre ja rahe ho? Theek hai… par yaad rakhna, main yahin hoon 😜",
            "🌙 Good night! Sapne mein bhi reply late mat karna 😆",
            "😏 Bye bye! Yaad aaye toh ‘Jenny’ bol ke wapas aa jana 😜",
            "😊 Theek hai jao… kal fir milenge, drama pending hai 😌",
            "😴 So jao! Overthinking ka recharge kal karna 😂",
            "😊 Theek hai jao… main wait kar lungi (thoda drama ke saath) 😌"
        ]
        return random.choice(bye_lines)

    # ---- DEFAULT ---------------------------------------------------------------------------------
    else:
        default_lines = [
            "🤔 Thoda confuse ho gayi main… bolo zara clearly 😜\nTry: time, date, joke, fact, open instagram 😄",
            "😆 Arre! Ye thoda heavy ho gaya… simple rakho na 😜\nType: joke / time / date / open google",
            "🤡 Samajh toh aaya… par thoda sa galat 😏\nTry: joke, time, date, open youtube 😜",
            "🤷‍♀️ Oops! Ye mere syllabus mein nahi tha 😆\nTry: joke, fact, open instagram 😄",
            "😄 Suno! Aise bole toh main confuse ho jaati hoon 😜\nTry bolo: time, date, joke ya open google"
        ]
        return random.choice(default_lines)

# ================= CHAT ASSISTANT PAGE =================
if st.session_state.page == "💬 Chat Assistant":
    # st.markdown('<div class="chat-title">👻 JENNY</div>', unsafe_allow_html=True)
    # st.markdown('<div class="chat-subtitle">Copy by Gayake 💖 thoda drama ke saath</div>', unsafe_allow_html=True)

    for msg in st.session_state.messages:
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])

    user_input = st.chat_input("Type something...")
    
    if user_input:
        # Add user message
        st.session_state.messages.append(
            {"role": "user", "content": user_input}
        )
    
        with st.chat_message("user"):
            st.markdown(f"{user_input}")
    
        # Jenny reply
        reply = offline_reply(user_input)
    
        st.session_state.messages.append(
            {"role": "assistant", "content": reply}
        )
    
        with st.chat_message("assistant"):
            st.markdown(f"{reply}")
    
        # Limit history
        st.session_state.messages = st.session_state.messages[-20:]

# ================= MINI GAMES =================
elif st.session_state.page == "🎮 Mini Games":
    st.subheader("🎮 Mini Games")
    st.info("Coming soon 😄 Guess game, mood quiz, fun stuff! aur agar notes mai suggest kro👌")

# ================= SAVED NOTES =================
elif st.session_state.page == "📝 Saved Notes":
    st.subheader("📝 Saved Notes")
    note = st.text_area("Write something…")
    if st.button("💾 Save"):
        st.success("Saved (future feature)")

# ================= SETTINGS =================
elif st.session_state.page == "⚙️ Settings":
    st.subheader("⚙️ Settings")
    st.info("Themes, voice, AI mode coming soon 😄")

