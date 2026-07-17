import streamlit as st
import pandas as pd
import plotly.express as px

# --------------------------------------------------
# Page Config
# --------------------------------------------------
st.set_page_config(
    page_title="IPL Analytics Hub 2026",
    page_icon="🏏",
    layout="wide"
)
###=--------------------------------------------------------------
# call or laod all data set link so it can use easly in code anyway
#=----------------------------------------------------------------


#===============
df = pd.read_csv("batting_stats.csv", index_col=[0])
#==========
df1 = pd.read_csv("bowling_stats.csv", index_col=[0])
#==========
df2 = pd.read_csv("deliveries.csv", index_col=[0])
#==========
df3 = pd.read_csv("fielding_stats.csv", index_col=[0])
#==========
df4 = pd.read_csv("matches.csv", index_col=[0])
#==========
df5 = pd.read_csv("points_table.csv", index_col=[0])
#==========
df6 = pd.read_csv("squads.csv", index_col=[0])       
#==========
df7 = pd.read_csv("venues.csv", index_col=[0])
#==============


# --------------------------------------------------
# Custom CSS Styling
# --------------------------------------------------


st.markdown("""
<style>
    /* ✅ Style the expander header */
    div.streamlit-expanderHeader {
        background-color: #f6fff6;   /* light green background */
        border-left: 8px solid green; /* green side strip */
        padding: 8px;
        border-radius: 4px;
    }

    /* ✅ Equal size sidebar buttons */
    .stButton>button {
        background: linear-gradient(90deg, #ffcc00, #ff5733);
        color: white;
        border-radius: 10px;
        font-weight: bold;
        transition: 0.3s;
        width: 100% !important;   /* full width */
        height: 50px !important;  /* fixed height */
        margin-bottom: 8px;
    }
    .stButton>button:hover {
        background: linear-gradient(90deg, #ff5733, #ffcc00);
        box-shadow: 0 0 15px gold;
    }

    /* ✅ Glow effect for images */
    img {
        border-radius: 10px;
        box-shadow: 0 0 20px 5px gold;
        animation: shine-img 3s infinite;
    }
    @keyframes shine-img {
        0% { box-shadow: 0 0 10px 2px gold; }
        50% { box-shadow: 0 0 25px 8px yellow; }
        100% { box-shadow: 0 0 10px 2px gold; }
    }

    /* ✅ Shiny gradient text effect */
    h1, h2, h3 {
        background: linear-gradient(90deg, #ffcc00, #ffffff, #ffcc00);
        background-size: 200% auto;
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        animation: shine 3s linear infinite;
    }
    @keyframes shine {
        to { background-position: 200% center; }
    }
</style>
""", unsafe_allow_html=True)


# --------------------------------------------------
# Sidebar Navigation with Session State
# --------------------------------------------------
if "page" not in st.session_state:
    st.session_state.page = "Home"

st.sidebar.title("🙏 Welcome")

if st.sidebar.button("🏠 Home"): st.session_state.page = "Home"
if st.sidebar.button("📊 Original Data"): st.session_state.page = "Original Data"
if st.sidebar.button("📈 Visualization"): st.session_state.page = "Visualization"
if st.sidebar.button("📘 Feedback"): st.session_state.page = "Feedback"
if st.sidebar.button("👤 About"): st.session_state.page = "About"

page = st.session_state.page


#------------------------------------------------------





# --------------------------------------------------
# Page Content
# --------------------------------------------------






#===========================================
# Home page 
#=======================================
if page == "Home":
    
    st.markdown("<h1 style='text-align:center;'>🏏 IPL Analytics Hub 2026</h1>", unsafe_allow_html=True)
    st.divider()
    st.subheader("✨ Welcome to the ultimate IPL dashboard")
    st.write("Explore datasets, visualizations, and insights from the Indian Premier League 2026.")
    st.image("ipllogo.webp", caption="IPL Official Logo", use_container_width=True)




    
    st.divider()
    st.subheader("📌 Scope of IPL Analytics Hub")
    st.write("""
    - Provide a centralized platform for exploring IPL datasets (batting, bowling, fielding, matches, venues).
    - Enable interactive visualizations for deeper insights into player and team performance.
    - Support fans, analysts, and students in understanding tournament dynamics.
    - Highlight cultural, commercial, and global impact of the IPL.
    """)


    st.subheader("Explore More Details")

    col1, col2, col3 = st.columns(3)

    if col1.button("🎯 Objectives"):
        st.write("""
        - 📊 Explore raw datasets for batting, bowling, and match statistics  
        - 📈 Build interactive visualizations using Plotly and Streamlit  
        - 🔎 Identify key performance indicators and trends  
        - 🏏 Provide fans, analysts, and students with a user-friendly analytics hub  
        """)

    if col2.button("🛠️ Tools & Libraries"):

        
        st.write("""
        - **Streamlit** → For building interactive web apps  
        - **Pandas** → For data manipulation and analysis  
        - **NumPy** → For numerical computations  
        - **Plotly Express** → For interactive charts and dashboards  
        - **Matplotlib** → For static visualizations  
        - **Seaborn** → For statistical data visualization  
        """)

        with st.expander(" 🛠️ Tools & Libraries   code"):
            import streamlit as st

            code_snippet = """
                                import streamlit as st
                                import pandas as pd
                                import plotly.express as px """


            st.code(code_snippet, language="python")

        

        
    if col3.button("🌍 Impact"):
        st.write("""
        This project demonstrates how data science can transform sports analytics.  
        By analyzing IPL datasets, we can highlight player strengths, team dynamics, 
        and tournament evolution — making cricket more engaging for fans and insightful for analysts.

        The impact of IPL projects built with Streamlit can be significant, as they provide a powerful tool for data analysis and visualization. These projects not only offer deep insights into IPL data but also contribute to academic evaluation, portfolio review, and real-world analytics demonstrations. They can be a valuable asset for sports enthusiasts, analysts, and researchers looking to understand the IPL's evolution and individual player performance






        """)

    # -------------------------------
    # Expander for Extra Info
    # -------------------------------
    with st.expander("📚 Dataset Information (Click to Expand)"):
        st.write("""
        - Batting Stats → Player runs, strike rates, averages  
        - Bowling Stats → Wickets, economy rates, overs bowled  
        - Fielding Stats → Catches, stumpings, run-outs  
        - Matches → Match-level details including toss, winner, scores  
        - Points Table → Team standings and net run rate  
        - Venues → Stadium capacity, location, home team  
        """)
    st.divider()
    st.title("📂 Dataset Source")

    st.write("""
               - The datasets powering this IPL Analytics Hub 2026 are sourced from **Kaggle**, 
                a trusted platform for open data and machine learning projects.  
                They include detailed statistics on batting, bowling, fielding, matches, points tables, squads, and venues.  
                This ensures that the analysis is grounded in reliable, community‑validated data.
            """)

    st.markdown("👉 [Kaggle IPL 2026 Dataset](https://www.kaggle.com/datasets/krishd123/ipl-2026-complete-dataset)")

    with st.expander("ℹ️ More About the Dataset"):
               st.write("""
            - **Publisher**: Kaggle community dataset by KrishD123  
            - **Coverage**: IPL 2026 season (all matches, teams, players, venues)  
            - **Format**: CSV files for easy integration with Pandas and Streamlit  
            - **Use Cases**:  
                - Exploratory Data Analysis (EDA)  
                - Predictive modeling (e.g., win probability, player performance)  
                - Interactive dashboards and visualizations  
                - Academic projects and portfolio building  
            """)



    st.divider()

    st.subheader("🌍 Why This Project Matters")
    st.write("""
    The IPL is more than just cricket — it’s a global phenomenon.  
    This project demonstrates how **data science transforms sports analytics**:  
    - 📊 Identifying key performance indicators  
    - 🔎 Understanding team dynamics and strategies  
    - 🏆 Highlighting player strengths and match-winning contributions  
    - 🌐 Offering fans and analysts a user-friendly way to explore IPL data  
    """)
    st.divider()
    st.subheader("✨ Impact")
    st.write("""
    By analyzing IPL datasets, we can highlight player strengths, team dynamics, 
    and tournament evolution — making cricket more engaging for fans and insightful 
    for analysts. The hub also serves as a valuable resource for **students, 
    researchers, and professionals** working on sports analytics projects.
    """)


    
    # -------------------------------
    # Summary Section with Widgets
    # -------------------------------
    st.divider()
    
    st.subheader("📊 Quick IPL 2026 Summary")

    # Metrics in columns
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Teams", "10")
    col2.metric("Matches Played", "74")
    col3.metric("Total Runs", "25,430")
    col4.metric("Viewership", "600M+")

    # Progress bar example
    st.subheader("Tournament Progress")
    st.progress(1.00)  # 85% completed






#####----------------------------------------------------------------------------------------------
#####  Original Data set page   
#####---------------------------------------------------------------------------##########
elif page == "Original Data":
    st.title("📊 Original Dataset Explorer")
    st.divider()

    st.write("""
    Welcome to the Original Dataset Explorer. 
    This section provides detailed information about each dataset used in the IPL Analytics Hub 2026 project.
    Each tab below contains not only the raw data but also a comprehensive explanation of its purpose, 
    structure, and potential insights. Toggle the tables on/off for a cleaner view.
    """)

    if "show_tables" not in st.session_state:
        st.session_state.show_tables = True

    toggle = st.button("🔄 Toggle Tables")

    if toggle:
        st.session_state.show_tables = not st.session_state.show_tables

    tab1, tab2, tab3, tab4, tab5, tab6, tab7, tab8 = st.tabs(
        ["🏏 Batting Stats", "🎯 Bowling Stats", "🚚 Deliveries", "🧤 Fielding Stats",
         "🏟️ Matches", "📈 Points Table", "👥 Squads", "📍 Venues"])
    if st.session_state.show_tables:
        with tab1:
            with st.expander("🏏 Batting Stats Dataset"):
                st.write("""
                        - The batting statistics dataset is one of the most crucial components of IPL analytics. 
                        It contains detailed information about every batsman’s performance across matches. 
                        Key columns include player name, runs scored, balls faced, strike rate, boundaries hit, 
                        and average runs per match. Analysts use this dataset to identify consistent performers, 
                        explosive hitters, and players who anchor innings. It also helps in comparing batting 
                        strategies across teams and seasons. For example, strike rate analysis can reveal 
                        aggressive batting styles, while averages highlight stability. This dataset is often 
                        combined with match outcomes to see how batting performances influence team success. 
                        Coaches and selectors rely on batting stats to make decisions about batting order, 
                        substitutions, and retention of players. Fans can explore this dataset to track their 
                        favorite players’ progress. Data scientists can apply regression models to predict 
                        future performance based on historical batting stats. Visualization of runs distribution 
                        across overs can uncover trends in powerplay vs death overs. Strike rate vs average 
                        scatter plots are commonly used to categorize batsmen into aggressive vs consistent. 
                        This dataset also supports fantasy league predictions, where player value is tied to 
                        batting output. In summary, batting stats form the backbone of performance analysis 
                        in IPL and provide endless opportunities for insights.
                    """)
            df = pd.read_csv("batting_stats.csv", index_col=[0])
            st.dataframe(df, use_container_width=True)
            st.download_button("⬇️ Download Batting Stats CSV", df.to_csv().encode("utf-8"), "batting_stats.csv", "text/csv")
        with tab2:
            with st.expander("🎯 Bowling Stats Dataset"):
                st.write("""
    - The bowling statistics dataset captures the performance of bowlers across matches. 
    It includes wickets taken, overs bowled, runs conceded, economy rate, strike rate, 
    and best bowling figures. Analysts use this dataset to evaluate the effectiveness 
    of bowlers in different match situations. Economy rate is critical in T20 cricket, 
    as restricting runs often matters more than taking wickets. Strike rate indicates 
    how frequently a bowler takes wickets. Comparing spinners vs pacers across venues 
    can reveal pitch behavior. This dataset helps coaches decide bowling lineups and 
    strategies for specific opponents. For example, some bowlers excel in powerplays, 
    while others dominate in death overs. Fans can explore bowling stats to identify 
    match-winning spells. Data scientists can model wicket probabilities based on 
    overs and batsmen faced. Visualization of economy rate trends across seasons 
    highlights consistent performers. Bowling stats also feed into fantasy league 
    scoring systems. In short, this dataset is essential for understanding the 
    defensive and attacking aspects of IPL bowling.
    """)
            df1 = pd.read_csv("bowling_stats.csv", index_col=[0])
            st.dataframe(df1, use_container_width=True)
            st.download_button("⬇️ Download Bowling Stats CSV", df1.to_csv().encode("utf-8"), "bowling_stats.csv", "text/csv")

        with tab3:
            with st.expander("🚚 Deliveries Dataset"):
                st.write("""
    - The deliveries dataset is the most granular dataset in IPL analytics. 
    It records ball-by-ball details including over number, ball number, 
    batsman, bowler, runs scored, extras, and dismissals. This dataset 
    allows micro-level analysis of match dynamics. Analysts can study 
    batting patterns against specific bowlers, effectiveness of yorkers 
    in death overs, or success rates of spinners in middle overs. 
    Deliveries data supports advanced metrics like dot ball percentage, 
    boundary frequency, and dismissal types. Coaches use this dataset 
    to plan match strategies and identify weaknesses in opponents. 
    Fans can relive iconic deliveries and match moments. Data scientists 
    can build predictive models for runs per ball or dismissal likelihood. 
    Visualization of run flow across overs provides insights into momentum 
    shifts. Deliveries dataset is also used for win probability models 
    that update ball by ball. In essence, this dataset is the heartbeat 
    of IPL analytics, capturing the smallest unit of play.
    """)
            df2 = pd.read_csv("deliveries.csv", index_col=[0])
            st.dataframe(df2, use_container_width=True)
            st.download_button("⬇️ Download Deliveries CSV", df2.to_csv().encode("utf-8"), "deliveries.csv", "text/csv")


        with tab4:
            with st.expander("🧤 Fielding Stats Dataset"):
                st.write("""
    - The fielding dataset highlights contributions that often go unnoticed. 
    It includes catches, stumpings, run-outs, and fielding positions. 
    Analysts use this dataset to evaluate the impact of fielders on match outcomes. 
    Exceptional fielding can change the course of a match by saving runs or 
    effecting crucial dismissals. Coaches rely on this dataset to identify 
    agile fielders and assign them to critical positions. Fans can explore 
    spectacular catches and run-outs. Data scientists can model the probability 
    of dismissals based on fielding positions. Visualization of fielding 
    contributions across teams shows which teams excel in defense. Fielding 
    stats also influence player selection and retention. In short, this dataset 
    ensures that fielding contributions are recognized and analyzed.
    """)
            df3 = pd.read_csv("fielding_stats.csv", index_col=[0])
            st.dataframe(df3, use_container_width=True)
            st.download_button("⬇️ Download Fielding Stats CSV", df3.to_csv().encode("utf-8"), "fielding_stats.csv", "text/csv")


        with tab5:
            with st.expander("🏟️ Matches Dataset"):
                st.write("""
    - The matches dataset provides match-level information such as date, venue, 
    teams, toss results, and winners. Analysts use this dataset to study 
    team performance trends across seasons. Toss results can be correlated 
    with match outcomes to see if batting first or chasing is advantageous. 
    Venue analysis reveals home ground advantages. Coaches use this dataset 
    to plan strategies for specific venues and opponents. Fans can explore 
    match histories and rivalries. Data scientists can build models to 
    predict match outcomes based on toss and venue. Visualization of win 
    percentages across venues highlights team strengths. Matches dataset 
    also supports scheduling and logistics analysis. In short, this dataset 
    provides the big picture of IPL matches.
    """)
            df4 = pd.read_csv("matches.csv", index_col=[0])
            st.dataframe(df4, use_container_width=True)
            st.download_button("⬇️ Download Matches CSV", df4.to_csv().encode("utf-8"), "matches.csv", "text/csv")


        with tab6:
            with st.expander("📈 Points Table Dataset"):
                st.write("""
                        - The points table dataset summarizes team standings. It includes matches 
                        played, wins, losses, points, and net run rate. Analysts use this dataset 
                            to track team progress across the season. Net run rate often decides 
                        qualification for playoffs. Coaches use this dataset to motivate teams 
                        and set targets. Fans follow the points table to see their team’s 
                        position. Data scientists can simulate playoff scenarios based on 
                        remaining matches. Visualization of points progression across rounds 
                        shows momentum shifts. Points table dataset is essential for understanding 
                        the competitive landscape of IPL.
                    """)
            df5 = pd.read_csv("points_table.csv", index_col=[0])
            st.dataframe(df5, use_container_width=True)
            st.download_button("⬇️ Download Points Table CSV", df5.to_csv().encode("utf-8"), "points_table.csv", "text/csv")


        with tab7:
            with st.expander("👥 Squads Dataset"):
                st.write("""
                         -   The squads dataset lists players in each team along with their roles. 
                        It includes batsmen, bowlers, all-rounders, and wicketkeepers. Analysts 
                        use this dataset to study team composition and balance. Coaches rely 
                        on this dataset for team selection and strategy. Fans explore squads 
                        to see their favorite players. Data scientists can analyze the impact 
                        of team composition on match outcomes. Visualization of squad balance 
                        shows strengths and weaknesses. Squads dataset also supports auction 
                        analysis and player retention strategies. In short, this dataset 
                        provides insights into team building and management.
                    """)
            df6 = pd.read_csv("squads.csv", index_col=[0])
            st.dataframe(df6, use_container_width=True)
            st.download_button("⬇️ Download Squads CSV", df6.to_csv().encode("utf-8"), "squads.csv", "text/csv")


        with tab8:
            with st.expander("📍 Venues Dataset"):
                st.write("""
                        - The venues dataset provides detailed information about the stadiums and grounds where IPL matches are played. 
                        It includes venue names, cities, states, and capacities. Analysts use this dataset to study home ground 
                        advantages, crowd capacity, and geographical distribution of matches. Coaches and teams rely on venue data 
                        to plan strategies based on pitch conditions and historical performance at specific grounds. Fans can explore 
                        iconic stadiums and their histories. Data scientists can correlate venue characteristics with match outcomes, 
                        such as whether certain venues favor batting or bowling. Visualization of venue distribution across states 
                            highlights the spread of IPL matches. This dataset is essential for understanding the role of stadiums in 
                            shaping the dynamics of the league.
                     """)
            df7 = pd.read_csv("venues.csv", index_col=[0])
            st.dataframe(df7, use_container_width=True)
            st.download_button("⬇️ Download Venues CSV", df7.to_csv().encode("utf-8"), "venues.csv", "text/csv")

    else:
        st.warning("⚠️ Tables are hidden. Click 'Toggle Tables' to show them again.")





############-----======================================================================================        
############   Visualization Page
############-----===================================================================-------------####
elif page == "Visualization":
    st.title("📈 IPL Visualizations")
    st.divider()

    st.subheader("🎨 Explore Visualizations by Dataset")

    # Create 8 tabs for datasets
    tab1, tab2, tab3, tab4, tab5, tab6, tab7, tab8 = st.tabs(
        ["🏏 Batting Stats", "🎯 Bowling Stats", "🚚 Deliveries", "🧤 Fielding Stats",
         "🏟️ Matches", "📈 Points Table", "👥 Squads", "📍 Venues"]
    )

# -------------------------------
# Batting Stats Tab
# -------------------------------
    with tab1:
        

        

  
    # Load dataset
        df = pd.read_csv("batting_stats.csv", index_col=[0])
        with st.expander("📊 DataSet"):
            st.write(df)
    # -------------------------------
    # Summary Section
    # -------------------------------
        with st.expander("📊 Quick Summary of Batting Stats"):
            st.write(f"""
    - Total Players: **{df['batsman'].nunique()}**
    - Total Runs Recorded: **{df['runs'].sum()}**
    - Highest Individual Score: **{df['runs'].max()}**
    - Average Runs per Player: **{round(df['runs'].mean(), 2)}**
    - Missing Values: **{df.isnull().sum().sum()}**
    """)


            st.title("Columns Details")
            st.write(df.columns)
            st.title("Sum of all NAN values in columns")
            st.write(df.isnull().sum())
            st.title("Describe")
            st.write(df.describe())
        with st.expander("📊 Quick Summary of Batting Stats(After cleaning)"):
            st.write("- No need for cleaning")


        st.divider()
        st.subheader("🎨 Choose a Visualization")

    # -------------------------------
    # Graph Buttons
    # -------------------------------
        if st.button("🏏 Runs by Batsman"):
            fig1 = px.bar(df, x="batsman", y="runs", color="team",
                      title="Compare total runs scored by each batsman across teams")
            st.plotly_chart(fig1, use_container_width=True)
            st.markdown("**Key Points:** Shows top run scorers and team contributions.")

        if st.button("⚡ Average vs Strike Rate"):
            fig2 = px.scatter(df, x="average", y="strike_rate", color="team", size="runs",
                          title="Average vs Strike Rate (bubble size = runs)")
            st.plotly_chart(fig2, use_container_width=True)
            st.markdown("**Key Points:** Balance between consistency and aggression.")

        if st.button("🔥 Impact Distribution"):
            fig3 = px.box(df, x="team", y="impact", color="team",
                      title="Distribution of impact scores per team")
            st.plotly_chart(fig3, use_container_width=True)
            st.markdown("**Key Points:** Spread of player impact within each team.")

        if st.button("💥 Boundary Count"):
            fig4 = px.bar(df, x="batsman", y="fours", color="sixes",
                      title="Boundary Count (Fours vs Sixes)")
            st.plotly_chart(fig4, use_container_width=True)
            st.markdown("**Key Points:** Compares batsmen’s ability to hit boundaries.")

        if st.button("🎯 Conversion of Fifties to Hundreds"):
            fig5 = px.scatter(df, x="hundreds", y="fifties", size="runs", color="team",
                          title="Shows which batsmen convert fifties into hundreds")
            st.plotly_chart(fig5, use_container_width=True)
            st.markdown("**Key Points:** Identifies players who turn starts into big scores.")

        if st.button("⚡ Efficiency of Batsmen"):
            fig6 = px.scatter(df, x="balls_faced", y="runs", color="team",
                          title="Efficiency of batsmen (runs per ball)")
            st.plotly_chart(fig6, use_container_width=True)
            st.markdown("**Key Points:** Shows strike efficiency by comparing runs per ball.")

        if st.button("🌐 Sunburst Breakdown"):
            fig7 = px.sunburst(df, path=["team","batsman","strike_rate","runs","high_score"],
                           color="team",
                           title="Team → Batsman → Strike Rate → Runs → High Score")
            st.plotly_chart(fig7, use_container_width=True)
            st.markdown("**Key Points:** Hierarchical view of team and player performance.")

# -------------------------------
# Bowling Stats Tab
# -------------------------------
    with tab2:
        df1 = pd.read_csv("bowling_stats.csv", index_col=[0])
        with st.expander("📊 DataSet"):
            st.write(df1)
        with st.expander("📊 Bowling Stats Visualizations(Before cleaning)"):

    # -------------------------------
    # Summary Section
    # -------------------------------
            st.write(f"""
    - Total Bowlers: **{df1['bowler'].nunique()}**
    - Total Wickets Taken: **{df1['wickets'].sum()}**
    - Best Economy Rate: **{df1['economy'].min()}**
    - Average Bowling Impact: **{round(df1['impact'].mean(), 2)}**
    - Missing Values: **{df1.isnull().sum().sum()}**
    """)





            st.title("Columns Details")
            st.write(df1.columns)
            st.title("Sum of all NAN values in columns")
            st.write(df1.isnull().sum())
            st.title("Describe")
            st.write(df1.describe())
        with st.expander("📊 Bowling Stats Visualizations(After cleaning)"):
            st.write("- No Need for cleaning")

        st.divider()
        st.subheader("🎨 Choose a Visualization")

    # -------------------------------
    # Graph Buttons
    # -------------------------------
        if st.button("🎯 Wickets vs Economy Rate", key="bowl_wickets_economy"):
            fig = px.scatter(df1, x="wickets", y="economy", color="team", size="impact",
                         title="Wickets vs Economy Rate")
            st.plotly_chart(fig, use_container_width=True)
            st.markdown("**Key Points:** Shows how wicket-taking ability relates to economy rate. Bigger bubbles = higher impact.")

        if st.button("🔥 Bowler Impact Score", key="bowl_impact"):
            fig = px.bar(df1, x="bowler", y="impact", color="team",
                     title="Bowler Impact Score")
            st.plotly_chart(fig, use_container_width=True)
            st.markdown("**Key Points:** Highlights which bowlers contribute most to match outcomes.")

        if st.button("⚡ Dot Balls vs Wickets", key="bowl_dotballs"):
            fig = px.scatter(df1, x="dot_balls", y="wickets", size="overs", color="team",
                         title="Dot Balls vs Wickets")
            st.plotly_chart(fig, use_container_width=True)
            st.markdown("**Key Points:** Shows pressure-building ability (dot balls) vs wicket-taking power.")

        if st.button("📊 Bowling Average Distribution", key="bowl_avg_dist"):
            fig = px.box(df1, x="team", y="avg", color="team",
                     title="Bowling Average Distribution by Team")
            st.plotly_chart(fig, use_container_width=True)
            st.markdown("**Key Points:** Compares consistency of bowlers across teams.")

        if st.button("🏆 Five-Wicket Hauls", key="bowl_5wh"):
            fig = px.bar(df1, x="bowler", y="5wh", color="team",
                     title="Five-Wicket Hauls by Bowler")
            st.plotly_chart(fig, use_container_width=True)
            st.markdown("**Key Points:** Identifies bowlers with match-winning spells.")

        if st.button("🏅 Four-Wicket Hauls", key="bowl_4wh"):
            fig = px.bar(df1, x="bowler", y="4wh", color="team",
                         title="Four-Wicket Hauls by Bowler")
            st.plotly_chart(fig, use_container_width=True)
            st.markdown("**Key Points:** Highlights bowlers who frequently deliver impactful performances.")

        if st.button("🌐 Sunburst Breakdown", key="bowl_sunburst"):
            fig = px.sunburst(df1, path=["team","bowler","overs","balls","runs"],
                              title="Team → Bowler → Overs → Balls → Runs")
            st.plotly_chart(fig, use_container_width=True)
            st.markdown("**Key Points:** Hierarchical view of team and bowler workload with runs conceded.")

        if st.button("🌳 Treemap: Wickets vs Runs", key="bowl_treemap"):
            fig = px.treemap(df1, path=["team","wickets","runs"], color="bowler",
                             title="Team Bowling Performance: Wickets vs Runs")
            st.plotly_chart(fig, use_container_width=True)
            st.markdown("**Key Points:** Compares team bowling efficiency by wickets taken vs runs conceded.")





        

    # -------------------------------
    # Deliveries Tab
    # -------------------------------
        with tab3:
    # -------------------------------
    # Load Dataset
    # -------------------------------
            df2 = pd.read_csv("deliveries.csv", index_col=[0])
            with st.expander("📊 DataSet"):
                st.write(df2)
    # -------------------------------
    # Initial Summary (Before Cleaning)
    # -------------------------------
            with st.expander("📊 Deliveries Summary (Before Cleaning)"):
                st.write(f"""
                - Total Deliveries Recorded: **{len(df2)}**
                - Unique Wicket Types: **{df2['wicket_type'].nunique()}**
                - Most Common Wicket Type: **{df2['wicket_type'].mode()[0]}**
                - Unique Bowlers: **{df2['bowler'].nunique()}**
                - Unique Strikers: **{df2['striker'].nunique()}**
                - Missing Values: **{df2.isnull().sum().sum()}**
                """)
                st.write("👉 Visualization shows some missing values in the dataset.")

            st.divider()
            st.subheader("🧹 Filling Missing Values")

            # -------------------------------
            # Data Cleaning
            # -------------------------------
            df2.fillna({"wicket_type": "not_out"}, inplace=True)
            df2.fillna({"player_dismissed": "unknown_player"}, inplace=True)
            df2.fillna({"fielder": "unknown_player"}, inplace=True)

            # -------------------------------
            # Cleaned Summary (After Cleaning)
            # -------------------------------
            with st.expander("📊 Deliveries Summary (After Cleaning)"):

                

                code_snippet = """#- fill NAN values
            df2.fillna({"wicket_type": "not_out"}, inplace=True)
            df2.fillna({"player_dismissed": "unknown_player"}, inplace=True)
            df2.fillna({"fielder": "unknown_player"}, inplace=True)
"""

                st.code(code_snippet, language="python")


                
                st.write(f"""
                - Total Deliveries Recorded: **{len(df2)}**
                - Unique Wicket Types: **{df2['wicket_type'].nunique()}**
                - Most Common Wicket Type: **{df2['wicket_type'].mode()[0]}**
                - Unique Bowlers: **{df2['bowler'].nunique()}**
                - Unique Strikers: **{df2['striker'].nunique()}**
                - Missing Values: **{df2.isnull().sum().sum()}**
                """)
                st.write("✅ All missing values have been filled successfully.")



            st.divider()
            st.subheader("📋 Cleaned Deliveries Dataset Preview")
            st.write(" -  click on toggle button to show or hide clean data set")
    ####-----------------------
    #### Clean data set view
    ####----------------------
            if "show_cleaned" not in st.session_state:
                st.session_state.show_cleaned = False

            if st.button("🔄 Toggle Cleaned Dataset"):
                st.session_state.show_cleaned = not st.session_state.show_cleaned

           

            if st.session_state.show_cleaned:
                st.dataframe(df2, use_container_width=True)
            else:
                st.info("ℹ️ Cleaned dataset is hidden. Click the button above to view it.")

            st.divider()
            st.subheader("🎨 Choose a Visualization")

    # -------------------------------
    # Graph Buttons
    # -------------------------------
            if st.button("🏟️ Runs Distribution by Venue", key="del_runs_venue"):
                fig = px.box(df2, x="venue", y="runs_of_bat",
                             title="Runs Distribution by Venue")
                st.plotly_chart(fig, use_container_width=True)
                st.markdown("**Key Points:** Shows how batting runs vary across different stadiums.")

            if st.button("➕ Extras Breakdown", key="del_extras_pie"):
                fig = px.pie(df2, names="extras", title="Extras Breakdown")
                st.plotly_chart(fig, use_container_width=True)
                st.markdown("**Key Points:** Highlights proportion of wides, no‑balls, leg‑byes, etc.")

            if st.button("⚰️ Wicket Types Distribution", key="del_wicket_types"):
                fig = px.histogram(df2[df2["wicket_type"].notna()], x="wicket_type",
                                   title="Distribution of Wicket Types")
                st.plotly_chart(fig, use_container_width=True)
                st.markdown("**Key Points:** Shows how batsmen are most often dismissed.")

            if st.button("🎯 Top Bowlers by Wickets", key="del_top_bowlers"):
                fig = px.bar(df2[df2["wicket_type"].notna()].groupby("bowler")["wicket_type"].count().reset_index(),
                             x="bowler", y="wicket_type", title="Top Bowlers by Wickets")
                st.plotly_chart(fig, use_container_width=True)
                st.markdown("**Key Points:** Identifies leading wicket‑takers.")

            if st.button("🏏 Top Strikers by Runs", key="del_top_strikers"):
                fig = px.bar(df2.groupby("striker")["runs_of_bat"].sum().reset_index(),
                             x="striker", y="runs_of_bat", title="Top Batsmen by Runs")
                st.plotly_chart(fig, use_container_width=True)
                st.markdown("**Key Points:** Shows batsmen contributing the most runs.")

            if st.button("⚡ Runs vs Extras Scatter", key="del_runs_extras"):
                fig = px.scatter(df2, x="runs_of_bat", y="extras", color="innings",
                                 title="Runs vs Extras per Ball")
                st.plotly_chart(fig, use_container_width=True)
                st.markdown("**Key Points:** Compares scoring shots with extras conceded.")

            if st.button("🎻 Runs Distribution by Innings", key="del_violin_innings"):
                fig = px.violin(df2, x="innings", y="runs_of_bat", box=True, points="all",
                                title="Runs Distribution by Innings")
                st.plotly_chart(fig, use_container_width=True)
                st.markdown("**Key Points:** Shows scoring spread between first and second innings.")

            if st.button("🌐 Sunburst: Team & Striker", key="del_sunburst_striker"):
                fig = px.sunburst(df2, path=["batting_team","striker"], values="runs_of_bat",
                                  title="Runs Contribution by Team and Striker")
                st.plotly_chart(fig, use_container_width=True)
                st.markdown("**Key Points:** Hierarchical view of team contributions via individual batsmen.")

            if st.button("📊 Histogram of Runs per Ball", key="del_hist_runs"):
                fig = px.histogram(df2, x="runs_of_bat", nbins=6,
                                   title="Distribution of Runs per Ball")
                st.plotly_chart(fig, use_container_width=True)
                st.markdown("**Key Points:** Shows frequency of singles, boundaries, and dot balls.")

            if st.button("🌳 Treemap of Wickets", key="del_treemap_wickets"):
                fig = px.treemap(df2[df2["wicket_type"].notna()],
                                 path=["bowling_team","bowler","wicket_type"],
                                 title="Treemap of Wickets by Team and Bowler")
                st.plotly_chart(fig, use_container_width=True)
                st.markdown("**Key Points:** Visualizes dismissal distribution across teams and bowlers.")

            if st.button("🏟️ Wickets by Venue", key="del_wickets_venue"):
                fig = px.bar(df2[df2["wicket_type"].notna()].groupby("venue")["wicket_type"].count().reset_index(),
                             x="venue", y="wicket_type", title="Wickets by Venue")
                st.plotly_chart(fig, use_container_width=True)
                st.markdown("**Key Points:** Highlights venues where most wickets fall.")

            if st.button("🎻 Extras by Bowling Team", key="del_violin_extras"):
                fig = px.violin(df2, x="bowling_team", y="extras", box=True, points="all",
                                title="Extras Distribution by Bowling Team")
                st.plotly_chart(fig, use_container_width=True)
                st.markdown("**Key Points:** Shows which teams concede the most extras.")

            if st.button("📊 Histogram of Extras per Ball", key="del_hist_extras"):
                fig = px.histogram(df2, x="extras", title="Histogram of Extras per Ball")
                st.plotly_chart(fig, use_container_width=True)
                st.markdown("**Key Points:** Distribution of extras across deliveries.")

            if st.button("🎻 Runs by Over", key="del_violin_over"):
                fig = px.violin(df2, x="over", y="runs_of_bat", box=True, points="all",
                                title="Runs Distribution Across Overs")
                st.plotly_chart(fig, use_container_width=True)
                st.markdown("**Key Points:** Shows scoring patterns across overs.")

            if st.button("🌐 Sunburst: Venue & Innings", key="del_sunburst_venue"):
                fig = px.sunburst(df2, path=["venue","innings"], values="runs_of_bat",
                                  title="Runs by Venue and Innings")
                st.plotly_chart(fig, use_container_width=True)
                st.markdown("**Key Points:** Hierarchical breakdown of runs by venue and innings.")

            if st.button("🌳 Treemap: Stage & Team", key="del_treemap_stage"):
                fig = px.treemap(df2, path=["stage","batting_team"], values="runs_of_bat",
                                 title="Runs by Stage and Team")
                st.plotly_chart(fig, use_container_width=True)
                st.markdown("**Key Points:** Shows how runs are distributed across tournament stages.")







    # -------------------------------
    # Fielding Stats Tab
    # -------------------------------
    with tab4:
        # -------------------------------
        # Load Dataset
        # -------------------------------
        df3 = pd.read_csv("fielding_stats.csv", index_col=[0])
        with st.expander("📊 DataSet"):
            st.write(df5)
        # -------------------------------
        # Fielding Stats Summary
        # -------------------------------
        with st.expander("📊 Fielding Stats Summary(Before cleaning)"):
            st.write(f"""
            - Total Records: **{len(df3)}**
            - Columns: **{list(df3.columns)}**
            - Missing Values: **{df3.isnull().sum().sum()}**
            """)
            st.write("👉 Data Set is fully clean.")
        with st.expander("📊 Fielding Stats Summary(After cleaning)"):
            st.write("- No need to clean")


        st.divider()
        st.subheader("🎨 Choose a Visualization")

        # -------------------------------
        # Visualizations with Buttons
        # -------------------------------
        if st.button("🏏 Catches by Player Across Teams"):
            fig = px.bar(df3, x="player", y="catches", color="team",
                         title="Catches by Player Across Teams")
            st.plotly_chart(fig, use_container_width=True)
            st.markdown("**Key Points:** Shows which players contribute most catches for their teams.")

        if st.button("📈 Line Chart of CPM Across Players"):
            fig = px.line(df3, x="player", y="cpm",
                          title="Line Chart of CPM Across Players")
            st.plotly_chart(fig, use_container_width=True)
            st.markdown("**Key Points:** Highlights consistency of players in catches per match.")

        if st.button("🔮 3D Scatter of Team, Player, Catches"):
            fig = px.scatter_3d(df3, x="team", y="player", z="catches", color="team",
                                title="3D Chart of Team vs Player vs Catches")
            st.plotly_chart(fig, use_container_width=True)
            st.markdown("**Key Points:** Visualizes team-player-catches relationship in 3D space.")

        if st.button("🥧 Team Contribution in Catches"):
            fig = px.pie(df3, names="team", values="catches",
                         title="Team Contribution in Catches")
            st.plotly_chart(fig, use_container_width=True)
            st.markdown("**Key Points:** Reveals which team contributes the most catches overall.")

        if st.button("⚡ Matches Played vs Catches Taken"):
            fig = px.scatter(df3, x="matches", y="catches", color="team", size="catches",
                             title="Matches Played vs Catches Taken")
            st.plotly_chart(fig, use_container_width=True)
            st.markdown("**Key Points:** Highlights consistency — players who take more catches per match.")

        if st.button("🏆 Top 10 Catchers"):
            fig = px.bar(df3.sort_values("catches", ascending=False).head(10),
                         x="catches", y="player", orientation="h", color="team",
                         title="Top 10 Catchers")
            st.plotly_chart(fig, use_container_width=True)
            st.markdown("**Key Points:** Quickly identifies the best fielders in the dataset.")

        if st.button("📦 Distribution of Catches per Match by Team"):
            fig = px.box(df3, x="team", y="cpm", color="team",
                         title="Distribution of Catches per Match by Team")
            st.plotly_chart(fig, use_container_width=True)
            st.markdown("**Key Points:** Compares how consistent each team’s fielders are.")

        if st.button("🌟 Top 10 Fielders by CPM"):
            fig = px.bar(df3.sort_values("cpm", ascending=False).head(10),
                         x="cpm", y="player", orientation="h", color="team",
                         title="Top 10 Fielders by CPM")
            st.plotly_chart(fig, use_container_width=True)
            st.markdown("**Key Points:** Highlights the most reliable catchers across the league.")

        if st.button("🌞 Sunburst Graph of Team → Player → Catches"):
            fig = px.sunburst(df3, path=["team", "player", "catches"],
                              title="Team → Player → Catches")
            st.plotly_chart(fig, use_container_width=True)
            st.markdown("**Key Points:** Hierarchical view of team and player contributions in catches.")













    # -------------------------------
    # Matches Tab
    # -------------------------------
    with tab5:
    # -------------------------------
    # Load Dataset
    # -------------------------------
        df4 = pd.read_csv("matches.csv", index_col=[0])

        # -------------------------------
        # Matches Dataset Preview
        # -------------------------------
        with st.expander("📊 Dataset"):
            st.write(df4)

        # -------------------------------
        # Matches Dataset Summary (Before Cleaning)
        # -------------------------------
        with st.expander("📊 Matches Dataset Summary & Diagnostics (Before Cleaning)"):
            st.write(f"""
            - Total Records: **{len(df4)}**
            - Columns: **{list(df4.columns)}**
            - Missing Values: **{df4.isnull().sum().sum()}**
            """)
            st.write("⚠️ Missing values found in the dataset.")
            st.write("### ❌ Missing Values by Column")
            st.write(df4.isnull().sum())
            st.write("### 📈 Descriptive Statistics")
            st.write(df4.describe())

        # -------------------------------
        # Data Cleaning
        # -------------------------------
        df4.fillna({"first_ings_score": df4["first_ings_score"].mode()[0]}, inplace=True)
        df4.fillna({"first_ings_wkts": df4["first_ings_wkts"].mode()[0]}, inplace=True)
        df4.fillna({"second_ings_score": df4["second_ings_score"].mode()[0]}, inplace=True)
        df4.fillna({"second_ings_wkts": df4["second_ings_wkts"].mode()[0]}, inplace=True)
        df4.fillna({"match_winner": "noresult"}, inplace=True)
        df4.fillna({"wb_runs": df4["wb_runs"].median()}, inplace=True)
        df4.fillna({"wb_wickets": df4["wb_wickets"].mode()[0]}, inplace=True)
        df4.fillna({"balls_left": df4["balls_left"].median()}, inplace=True)
        df4.fillna({"player_of_the_match": "unknownplayer"}, inplace=True)
        df4.fillna({"highscore": df4["highscore"].mean()}, inplace=True)
        df4.fillna({"best_bowling": "unknownplayer"}, inplace=True)
        df4.fillna({"best_bowling_figure": df4["best_bowling_figure"].mode()[0]}, inplace=True)
        df4.fillna({"top_scorer":"unknownplayer"},inplace=True)
        # -------------------------------
        # Matches Dataset Summary (After Cleaning)
        # -------------------------------
        with st.expander("📊 Matches Dataset Summary & Diagnostics (After Cleaning)"):

            code_snippet = """####- for fill NAN values
            df4.fillna({"first_ings_score": df4["first_ings_score"].mode()[0]}, inplace=True)
        df4.fillna({"first_ings_wkts": df4["first_ings_wkts"].mode()[0]}, inplace=True)
        df4.fillna({"second_ings_score": df4["second_ings_score"].mode()[0]}, inplace=True)
        df4.fillna({"second_ings_wkts": df4["second_ings_wkts"].mode()[0]}, inplace=True)
        df4.fillna({"match_winner": "noresult"}, inplace=True)
        df4.fillna({"wb_runs": df4["wb_runs"].median()}, inplace=True)
        df4.fillna({"wb_wickets": df4["wb_wickets"].mode()[0]}, inplace=True)
        df4.fillna({"balls_left": df4["balls_left"].median()}, inplace=True)
        df4.fillna({"player_of_the_match": "unknownplayer"}, inplace=True)
        df4.fillna({"highscore": df4["highscore"].mean()}, inplace=True)
        df4.fillna({"best_bowling": "unknownplayer"}, inplace=True)
        df4.fillna({"best_bowling_figure": df4["best_bowling_figure"].mode()[0]}, inplace=True)
        df4.fillna({"top_scorer":"unknownplayer"},inplace=True)

                                
                                """

            st.code(code_snippet, language="python")


            
            st.write(f"""
            - Total Records: **{len(df4)}**
            - Columns: **{list(df4.columns)}**
            - Missing Values: **{df4.isnull().sum().sum()}**
            """)
            st.write("✅ All missing values have been filled successfully.")
            st.write("### 📈 Updated Descriptive Statistics")
            st.write(df4.describe())

        st.divider()
        st.subheader("🎨 Choose a Visualization")
           



        # -------------------------------
        # Visualizations with Buttons
        # -------------------------------
        if st.button("🏆 Player of the Match Awards"):
            fig = px.bar(df4, x="player_of_the_match", title="Player of the Match Awards")
            st.plotly_chart(fig, use_container_width=True)
            st.markdown("**Key Points:** Highlights the most impactful players across matches.")

        if st.button("🏟️ Match Winners by Venue"):
            fig = px.treemap(df4, path=["venue","match_winner"], title="Match Winners by Venue")
            st.plotly_chart(fig, use_container_width=True)
            st.markdown("**Key Points:** Shows which venues favor certain teams.")

        if st.button("📊 Match Results by Tournament Stage"):
            fig = px.bar(df4, x="stage", color="match_result", title="Match Results by Tournament Stage")
            st.plotly_chart(fig, use_container_width=True)
            st.markdown("**Key Points:** Compares outcomes across group stage, playoffs, and finals.")

        if st.button("🎲 Toss Decision vs Match Result"):
            fig = px.bar(df4, x="toss_decision", color="match_result", title="Impact of Toss Decision on Match Result")
            st.plotly_chart(fig, use_container_width=True)
            st.markdown("**Key Points:** Reveals whether batting/fielding first after toss impacts winning.")

        if st.button("⏳ Balls Left by Stage"):
            fig = px.box(df4, x="stage", y="balls_left", title="Balls Left by Stage")
            st.plotly_chart(fig, use_container_width=True)
            st.markdown("**Key Points:** Shows how close matches are at different stages.")

        if st.button("➕ Extras Impact on Match Result"):
            fig = px.scatter(df4, x="wb_runs", y="second_ings_score", color="match_result", title="Extras Impact on Match Result")
            st.plotly_chart(fig, use_container_width=True)
            st.markdown("**Key Points:** Highlights how wide-ball runs influence match outcomes.")

        if st.button("🔥 Super Over Matches Frequency"):
            fig = px.histogram(df4, x="super_over_match", title="Super Over Matches Frequency")
            st.plotly_chart(fig, use_container_width=True)
            st.markdown("**Key Points:** Shows how often matches went into a super over.")

        if st.button("🎯 Top Scorer vs Match Result"):
            fig = px.bar(df4, x="top_scorer", color="match_result", title="Top Scorer vs Match Result")
            st.plotly_chart(fig, use_container_width=True)
            st.markdown("**Key Points:** Identifies players whose scoring correlates with wins.")

        if st.button("🤝 Match Winner vs Player of the Match"):
            fig = px.bar(df4, x="match_winner", color="player_of_the_match", title="Match Winner vs Player of the Match")
            st.plotly_chart(fig, use_container_width=True)
            st.markdown("**Key Points:** Shows which teams’ wins align with standout performances.")

        if st.button("🎳 Best Bowling Performances"):
            fig = px.bar(df4, x="best_bowling", y="best_bowling_figure", title="Best Bowling Performances")
            st.plotly_chart(fig, use_container_width=True)
            st.markdown("**Key Points:** Highlights bowlers with the best figures in matches.")

        if st.button("📈 Top Scorer vs High Score"):
            fig = px.scatter(df4, x="top_scorer", y="highscore", title="Top Scorer vs High Score")
            st.plotly_chart(fig, use_container_width=True)
            st.markdown("**Key Points:** Shows correlation between top scorers and their highest scores.")

        if st.button("🏟️ Player of the Match by Venue"):
            fig = px.treemap(df4, path=["venue","player_of_the_match"], title="Player of the Match by Venue")
            st.plotly_chart(fig, use_container_width=True)
            st.markdown("**Key Points:** Reveals which venues see standout performances.")

        if st.button("📊 Venue vs First Innings Score"):
            fig = px.box(df4, x="venue", y="first_ings_score", title="Venue vs First Innings Score")
            st.plotly_chart(fig, use_container_width=True)
            st.markdown("**Key Points:** Compares scoring trends across venues.")

        if st.button("📊 First vs Second Innings Score"):
            fig = px.scatter(df4, x="first_ings_score", y="second_ings_score", color="match_result", title="First vs Second Innings Score")
            st.plotly_chart(fig, use_container_width=True)
            st.markdown("**Key Points:** Helps identify winning score thresholds.")

        if st.button("🪙 Toss Winner vs Match Winner"):
            fig = px.pie(df4, names="toss_winner", title="Toss Winner vs Match Winner")
            st.plotly_chart(fig, use_container_width=True)
            st.markdown("**Key Points:** Shows how often toss winners also win the match.")

        if st.button("🎲 Toss Decision Across Tournament Stages"):
            fig = px.bar(df4, x="stage", color="toss_decision", title="Toss Decision Across Tournament Stages")
            st.plotly_chart(fig, use_container_width=True)
            st.markdown("**Key Points:** Compares toss decisions across different stages.")
    # -------------------------------
    # Points Table Tab
    # -------------------------------
    with tab6:
        # -------------------------------
        # Load Dataset
        # -------------------------------
        df5 = pd.read_csv("points_table.csv", index_col=[0])
        with st.expander("📊 Dataset"):
            st.write(df5)

        # -------------------------------
        # Points Table Dataset Summary
        # -------------------------------
        with st.expander("📊 Points Table Summary & Diagnostics(Before cleaning)"):
            st.write(f"""
            - Total Records: **{len(df5)}**
            - Columns: **{list(df5.columns)}**
            - Missing Values: **{df5.isnull().sum().sum()}**
            """)
            st.write("👉 Dataset is fully clean.")
            st.write("### 📈 Descriptive Statistics")
            st.write(df5.describe())
        with st.expander("📊 Points Table Summary & Diagnostics(After cleaning)"):
            st.write("- No need to clean data set")

        st.divider()
        st.subheader("🎨 Choose a Visualization")

        # -------------------------------
        # Visualizations with Buttons
        # -------------------------------
        if st.button("⚡ Matches Played vs Wins by Team"):
            fig = px.scatter(df5, x="team", y="matches", color="wins",
                             title="Matches Played vs Wins by Team")
            st.plotly_chart(fig, use_container_width=True)
            st.markdown("**Key Points:** Shows correlation between matches played and wins.")

        if st.button("📈 Points Trend Across Teams"):
            fig = px.line(df5, x="team", y="points", title="Points Trend Across Teams")
            st.plotly_chart(fig, use_container_width=True)
            st.markdown("**Key Points:** Highlights how teams accumulate points over the season.")

        if st.button("📊 Matches Played by Team"):
            fig = px.line(df5, x="team", y="matches", title="Matches Played by Team")
            st.plotly_chart(fig, use_container_width=True)
            st.markdown("**Key Points:** Compares match participation across teams.")

        if st.button("🏆 Matches vs Wins"):
            fig = px.bar(df5, x="team", y="matches", color="wins",
                         title="Matches Played vs Wins")
            st.plotly_chart(fig, use_container_width=True)
            st.markdown("**Key Points:** Highlights consistency in converting matches into wins.")

        if st.button("❌ Matches vs Defeats"):
            fig = px.bar(df5, x="team", y="matches", color="defeats",
                         title="Matches Played vs Defeats")
            st.plotly_chart(fig, use_container_width=True)
            st.markdown("**Key Points:** Shows which teams struggle despite playing many matches.")

        if st.button("🤝 Ties vs Matches"):
            fig = px.bar(df5, x="ties", y="matches", color="team",
                         title="Ties vs Matches by Team")
            st.plotly_chart(fig, use_container_width=True)
            st.markdown("**Key Points:** Displays frequency of tied matches across teams.")

        if st.button("📦 Matches Distribution by Team"):
            fig = px.box(df5, x="team", y="matches", color="points",
                         title="Distribution of Matches by Team")
            st.plotly_chart(fig, use_container_width=True)
            st.markdown("**Key Points:** Compares spread of matches played with points earned.")

        if st.button("🥧 Matches Count by Team"):
            count = df5.groupby("team").size().reset_index(name="count")
            fig = px.pie(count, names="team", values="count", title="Matches Distribution by Team")
            st.plotly_chart(fig, use_container_width=True)
            st.markdown("**Key Points:** Shows how matches are distributed among teams.")

        if st.button("🌞 Team Outcomes Breakdown"):
            fig = px.sunburst(df5, path=["team","matches","wins","defeats","ties","abandoned"],
                              color="team", title="Team Outcomes Breakdown")
            st.plotly_chart(fig, use_container_width=True)
            st.markdown("**Key Points:** Hierarchical view of team performance outcomes.")

        if st.button("🔥 Heatmap of Wins by Team"):
            fig = px.density_heatmap(df5, x="team", y="wins", title="Heatmap of Wins by Team")
            st.plotly_chart(fig, use_container_width=True)
            st.markdown("**Key Points:** Highlights win intensity across teams.")

        if st.button("🚫 Abandoned Matches by Team"):
            fig = px.bar(df5, x="team", y="abandoned", color="team",
                         title="Abandoned Matches by Team")
            st.plotly_chart(fig, use_container_width=True)
            st.markdown("**Key Points:** Shows which teams have most abandoned matches.")

        if st.button("🎈 Wins vs Points Bubble Chart"):
            fig = px.scatter(df5, x="wins", y="points", size="matches", color="team",
                             title="Wins vs Points Bubble Chart")
            st.plotly_chart(fig, use_container_width=True)
            st.markdown("**Key Points:** Reveals how wins translate into points.")

        if st.button("⚖️ Wins vs Defeats Comparison"):
            fig = px.scatter(df5, x="wins", y="defeats", color="team",
                             title="Wins vs Defeats Comparison")
            st.plotly_chart(fig, use_container_width=True)
            st.markdown("**Key Points:** Shows balance between victories and losses.")

        if st.button("🏅 Points Table by Team"):
            fig = px.bar(df5.sort_values("points", ascending=False),
                         x="points", y="team", orientation="h", color="nrr",
                         title="Points Table by Team")
            st.plotly_chart(fig, use_container_width=True)
            st.markdown("**Key Points:** Ranks teams based on points and net run rate.")

        if st.button("🚀 Points vs Net Run Rate"):
            fig = px.scatter(df5, x="points", y="nrr", color="team", size="wins",
                             title="Points vs Net Run Rate")
            st.plotly_chart(fig, use_container_width=True)
            st.markdown("**Key Points:** Shows how net run rate correlates with points earned.")

        if st.button("🔮 3D Scatter: Matches vs NRR by Team"):
            fig = px.scatter_3d(df5, x="team", y="matches", z="nrr", color="team",
                                title="3D Scatter Plot: Matches vs NRR by Team")
            st.plotly_chart(fig, use_container_width=True)
            st.markdown("**Key Points:** Provides a 3D view of team performance metrics.")





        

    # -------------------------------
    # Squads Tab
    # -------------------------------
    with tab7:
        # -------------------------------
        # Load Dataset
        # -------------------------------
        df6 = pd.read_csv("squads.csv", index_col=[0])

        # -------------------------------
        # Squads Dataset Preview
        # -------------------------------
        with st.expander("📊 Dataset"):
            st.write(df6)

        # -------------------------------
        # Squads Dataset Summary (Before Cleaning)
        # -------------------------------
        with st.expander("📊 Squads Dataset Summary & Diagnostics (Before Cleaning)"):
            st.write(f"""
            - Total Records: **{len(df6)}**
            - Columns: **{list(df6.columns)}**
            - Missing Values: **{df6.isnull().sum().sum()}**
            """)
            st.write("⚠️ Missing values found in the dataset.")
            st.write("### ❌ Missing Values by Column")
            st.write(df6.isnull().sum())
            st.write("### 📈 Descriptive Statistics")
            st.write(df6.describe())

        # -------------------------------
        # Data Cleaning
        # -------------------------------
        df6.fillna({"designation": "player"}, inplace=True)

        # -------------------------------
        # Squads Dataset Summary (After Cleaning)
        # -------------------------------
        with st.expander("📊 Squads Dataset Summary & Diagnostics (After Cleaning)"):
            code_snippet = """####- for fill NAN values
            df6.fillna({"designation": "player"}, inplace=True)
                                
                                """

            st.code(code_snippet, language="python")
            st.write(f"""
            - Total Records: **{len(df6)}**
            - Columns: **{list(df6.columns)}**
            - Missing Values: **{df6.isnull().sum().sum()}**
            """)
            st.write("✅ All missing values have been filled successfully.")
            st.write("### 📈 Updated Descriptive Statistics")
            st.write(df6.describe())

        st.divider()
        st.subheader("🎨 Choose a Visualization")

        # -------------------------------
        # Visualizations with Buttons
        # -------------------------------
        if st.button("🏏 Number of Players per Team"):
            fig = px.bar(df6, x="team_name", y="player", title="Number of Players per Team")
            st.plotly_chart(fig, use_container_width=True)
            st.markdown("**Key Points:** Shows squad size across different teams.")

        if st.button("🎭 Player Roles across Teams"):
            fig = px.scatter(df6, x="player", y="role", color="team_name",
                             title="Player Roles across Teams")
            st.plotly_chart(fig, use_container_width=True)
            st.markdown("**Key Points:** Highlights distribution of roles among players in each team.")

        if st.button("🌳 Team and Player Hierarchy"):
            fig = px.treemap(df6, path=["team_name","player"], color="team_name",
                             title="Team and Player Hierarchy")
            st.plotly_chart(fig, use_container_width=True)
            st.markdown("**Key Points:** Hierarchical breakdown of teams and their players.")

        if st.button("🌍 Players by Nationality"):
            fig = px.sunburst(df6, path=["nationality","player"], color="nationality",
                              title="Players by Nationality")
            st.plotly_chart(fig, use_container_width=True)
            st.markdown("**Key Points:** Shows how players are distributed across nationalities.")

        if st.button("🎻 Role Distribution among Players"):
            fig = px.violin(df6, x="player", y="role", color="role",
                            box=True, points="all", title="Role Distribution among Players")
            st.plotly_chart(fig, use_container_width=True)
            st.markdown("**Key Points:** Compares spread of roles across players.")

        if st.button("📈 Player Designations"):
            fig = px.line(df6, x="player", y="designation", color="designation",
                          title="Player Designations")
            st.plotly_chart(fig, use_container_width=True)
            st.markdown("**Key Points:** Shows designation trends across players.")

        if st.button("🌞 Team, Player, and Role Breakdown"):
            fig = px.sunburst(df6, path=["team_name","player","role"],
                              title="Team, Player, and Role Breakdown")
            st.plotly_chart(fig, use_container_width=True)
            st.markdown("**Key Points:** Hierarchical view of team composition by role.")

        if st.button("📊 Number of Players by Nationality"):
            count_nat = df6.groupby("nationality").size().reset_index(name="count")
            fig = px.bar(count_nat, x="nationality", y="count",
                         title="Number of Players by Nationality")
            st.plotly_chart(fig, use_container_width=True)
            st.markdown("**Key Points:** Highlights which nationalities dominate the squads.")

        if st.button("🌳 Nationality, Team, and Player Hierarchy"):
            fig = px.treemap(df6, path=["nationality","team_name","player"], color="nationality",
                             title="Nationality, Team, and Player Hierarchy")
            st.plotly_chart(fig, use_container_width=True)
            st.markdown("**Key Points:** Hierarchical view of nationality → team → player.")

        if st.button("📦 Designation Spread by Team"):
            fig = px.box(df6, x="team_name", y="designation", color="team_name",
                         title="Designation Spread by Team")
            st.plotly_chart(fig, use_container_width=True)
            st.markdown("**Key Points:** Compares designation distribution across teams.")

        if st.button("🥧 Role Distribution among Players"):
            count_role = df6.groupby("role").size().reset_index(name="count")
            fig = px.pie(count_role, names="role", values="count",
                         title="Role Distribution among Players")
            st.plotly_chart(fig, use_container_width=True)
            st.markdown("**Key Points:** Shows proportion of batsmen, bowlers, all-rounders, and wicketkeepers.")

        if st.button("🌞 Role and Designation Breakdown"):
            fig = px.sunburst(df6, path=["role","designation","player"], color="role",
                              title="Role and Designation Breakdown")
            st.plotly_chart(fig, use_container_width=True)
            st.markdown("**Key Points:** Hierarchical view of role → designation → player.")















# -------------------------------
# Venues Tab
#--------------------------------
    with tab8:
        df7 = pd.read_csv("venues.csv", index_col=[0])
        with st.expander("📊 Dataset"):
            st.write(df7)
        # -------------------------------
        # Venues Dataset Summary
        # -------------------------------
        with st.expander("📊 Venues Dataset Summary & Diagnostics(Before cleaning)"):
            st.write(f"""
            - Total Records: **{len(df7)}**
            - Columns: **{list(df7.columns)}**
            - Missing Values: **{df7.isnull().sum().sum()}**
            """)
            st.write("✅ Dataset is fully clean.")
            st.write("### 📈 Descriptive Statistics")
            st.write(df7.describe())
        with st.expander("📊 Venues Dataset Summary & Diagnostics(After cleaning)"):
            st.write("- No need for cleaning")

        st.divider()
        st.subheader("🎨 Choose a Visualization")

        # -------------------------------
        # Visualizations with Buttons
        # -------------------------------
        if st.button("🌞 Sunburst: State → City → Stadium"):
            fig = px.sunburst(df7, path=["state","city","venue_stadium"], values="capacity",
                              color="state", title="Stadiums by State and City")
            st.plotly_chart(fig, use_container_width=True)
            st.markdown("**Key Points:** Shows hierarchical distribution of stadiums across states and cities.")

        if st.button("📈 Area Chart: Stadium Capacity by Venue"):
            fig = px.area(df7.sort_values("capacity"), x="venue_stadium", y="capacity",
                          title="Area Chart: Stadium Capacity by Venue")
            st.plotly_chart(fig, use_container_width=True)
            st.markdown("**Key Points:** Highlights stadiums with the largest capacities.")

        if st.button("🏙️ Stadium Capacity by City"):
            fig = px.bar(df7, x="capacity", y="city", orientation="h", color="state",
                         title="Stadium Capacity by City")
            st.plotly_chart(fig, use_container_width=True)
            st.markdown("**Key Points:** Compares stadium sizes across different cities.")

        if st.button("🌳 Treemap: State → City → Stadium"):
            fig = px.treemap(df7, path=["state","city","venue_stadium"], values="capacity",
                             color="capacity", title="Stadiums by State and City")
            st.plotly_chart(fig, use_container_width=True)
            st.markdown("**Key Points:** Provides a hierarchical view of stadiums by state and city.")

        if st.button("⚡ Scatter: Capacity vs City"):
            fig = px.scatter(df7, x="city", y="capacity", color="state", size="capacity",
                             title="Stadium Capacity Distribution by City")
            st.plotly_chart(fig, use_container_width=True)
            st.markdown("**Key Points:** Shows which cities host larger stadiums.")

        if st.button("🌞 Sunburst: Home Team → Stadium"):
            fig = px.sunburst(df7, path=["home_team","venue_stadium"], values="capacity",
                              color="home_team", title="Home Teams and Their Stadiums")
            st.plotly_chart(fig, use_container_width=True)
            st.markdown("**Key Points:** Displays stadiums grouped by their home teams.")

        if st.button("📦 Box Plot: Capacity Distribution by State"):
            fig = px.box(df7, x="state", y="capacity", color="state",
                         title="Capacity Distribution by State")
            st.plotly_chart(fig, use_container_width=True)
            st.markdown("**Key Points:** Compares stadium capacity ranges across states.")

        if st.button("🏟️ Bar: Stadium Capacity by Venue"):
            fig = px.bar(df7, x="venue_stadium", y="capacity", color="home_team",
                         title="Stadium Capacity by Venue")
            st.plotly_chart(fig, use_container_width=True)
            st.markdown("**Key Points:** Highlights stadiums with the highest capacity per team.")

        if st.button("🔥 Heatmap: State vs Capacity"):
            fig = px.density_heatmap(df7, x="state", y="capacity",
                                     title="Heatmap of Stadium Capacity by State")
            st.plotly_chart(fig, use_container_width=True)
            st.markdown("**Key Points:** Shows intensity of stadium capacities across states.")

        if st.button("🥧 Stadiums by Home Team"):
            count_team = df7.groupby("home_team").size().reset_index(name="count")
            fig = px.pie(count_team, names="home_team", values="count",
                         title="Number of Stadiums by Home Team")
            st.plotly_chart(fig, use_container_width=True)
            st.markdown("**Key Points:** Reveals which teams have multiple home stadiums.")

        if st.button("🥧 Stadiums by State"):
            count_state = df7.groupby("state").size().reset_index(name="count")
            fig = px.pie(count_state, names="state", values="count",
                         title="Number of Stadiums by State")
            st.plotly_chart(fig, use_container_width=True)
            st.markdown("**Key Points:** Shows which states have the most stadiums.")

        if st.button("🔮 3D Scatter: City vs State vs Capacity"):
            fig = px.scatter_3d(df7, x="city", y="state", z="capacity",
                                color="home_team", size="capacity",
                                title="3D Scatter Plot: City, State, and Capacity")
            st.plotly_chart(fig, use_container_width=True)
            st.markdown("**Key Points:** Provides a 3D view of stadium distribution by city, state, and capacity.")













###-------------------------------------------------------------------#######
###    Feedback Page
###=-----------------------------------------------------------------=#######
elif page == "Feedback":
    st.title("📘 Feedback ")
    st.divider()

    
    # -------------------------------
    # Interactive Buttons for Details
    # -------------------------------
    
    # Like / Dislike Section
    # -------------------------------
    st.subheader("👍👎 Do you like IPL?")
    col1, col2 = st.columns(2)

    with col1:
        if st.button("👍 Like"):
            st.success("Great! You like IPL 🎉")

    with col2:
        if st.button("👎 Dislike"):
            st.warning("Not a fan of IPL 😢")


    # -------------------------------
    # Widgets for Fun Interaction
    # -------------------------------
    st.subheader("📊 Quick Poll")
    favorite = st.radio("Which aspect of IPL interests you most?", 
                        ["Batting", "Bowling", "Fielding", "Team Strategies", "Audience Trends"])
    st.success(f"✅ You selected:< {favorite} >you like it most")




    # -------------------------------
    # Widgets for Fun Interaction
    # -------------------------------
        # -------------------------------
    

    # -------------------------------
    # Interactive Survey (Better than Quick Poll)
    # -------------------------------
    st.subheader("📊 User Survey: Share Your Preferences")

    # Rating sliders
    batting_score = st.slider("Rate your interest in Batting Analytics", 1, 10, 7)
    bowling_score = st.slider("Rate your interest in Bowling Analytics", 1, 10, 6)
    fielding_score = st.slider("Rate your interest in Fielding Analytics", 1, 10, 5)
    strategy_score = st.slider("Rate your interest in Team Strategies", 1, 10, 8)
    audience_score = st.slider("Rate your interest in Audience Trends", 1, 10, 9)

    # Show results in a bar chart
    st.subheader("📈 Your Preferences Overview")

    survey_data = pd.DataFrame({
        "Aspect": ["Batting", "Bowling", "Fielding", "Team Strategies", "Audience Trends"],
        "Interest Level": [batting_score, bowling_score, fielding_score, strategy_score, audience_score]
    })

    fig = px.bar(survey_data, x="Aspect", y="Interest Level", color="Aspect",
                 title="User Interest Levels in IPL Analytics")
    st.plotly_chart(fig, use_container_width=True)

    # -------------------------------
    # Extra Widgets for Usability
    # -------------------------------
    st.subheader("📝 Feedback")
    feedback = st.text_area("Tell us what feature you’d like to see next:")
    if st.button("Submit Feedback"):
        st.success("✅ Thank you for your feedback! We’ll use it to improve the dashboard.")

    st.subheader("🔔 Notifications")
    notify = st.checkbox("Receive updates when new IPL data is added")
    if notify:
        st.info("You’ll be notified about new datasets and visualizations.")


#==================================----------------------=============================================
#   About page
#==================================----------------------======================

elif page == "About":
    st.title("👤 About IPL Analytics Hub 2026")
    st.write("The Indian Premier League (IPL) is a professional Twenty20 cricket league in India, combining high-level cricket, entertainment, and commercial spectacle.")
    st.image("ipl2026.jpg", use_container_width=True)
    st.divider()
    
    
    

    st.divider()

    st.subheader("🏏 What is IPL Analytics Hub?")
    st.write("""
    IPL Analytics Hub 2026 is a comprehensive dashboard built to explore, analyze, 
    and visualize the rich datasets of the Indian Premier League. It combines 
    **data science, interactive visualizations, and sports analytics** to provide 
    fans, analysts, and researchers with deep insights into player and team performance.
    """)

    st.subheader("🛠️ Technology Stack")
    st.write("""
    - **Streamlit** → Interactive web app framework  
    - **Pandas & NumPy** → Data manipulation and numerical analysis  
    - **Plotly Express** → Interactive charts and dashboards  
    - **Matplotlib & Seaborn** → Statistical and static visualizations  
    - **Kaggle IPL Dataset** → Reliable source of IPL 2026 statistics  
    """)

    
   

    st.divider()
    


    st.title("✅ Conclusion")
    st.divider()

    st.subheader("🏏 Wrapping Up IPL Analytics Hub 2026")
    st.write("""
    The IPL Analytics Hub 2026 has brought together diverse datasets — batting, bowling, 
    fielding, matches, squads, venues, and points tables — into one interactive platform.  
    By combining **Streamlit, Pandas, and Plotly**, we’ve transformed raw statistics into 
    meaningful insights that highlight player performance, team dynamics, and tournament trends.
    """)

    st.subheader("🌍 Key Takeaways")
    st.write("""
    - 📊 Centralized access to IPL datasets for fans, analysts, and researchers  
    - ⚡ Interactive visualizations that make complex data easy to understand  
    - 🏆 Insights into match outcomes, player impact, and team strategies  
    - 🌐 Demonstrates the cultural and commercial significance of IPL through data science  
    """)

    st.subheader("🚀 Future Scope")
    st.write("""
    - Integration of **predictive models** (e.g., win probability, player performance forecasting)  
    - Enhanced **real-time analytics** during live matches  
    - Expansion into **fantasy league support** with player value predictions  
    - Deeper **venue and pitch analysis** to guide team strategies  
    """)

    st.subheader("👨‍💻 Developer Note")
    st.write("""
    This project was built with passion for cricket and data science.  
    It showcases how modern tools can turn raw statistics into meaningful insights.  
    Contributions, feedback, and ideas are always welcome to make the hub even better!
    """)

    st.subheader("✨ Final Note")
    st.write("""
    This project is more than just a dashboard — it’s a demonstration of how 
    **data science and visualization can transform sports analytics**.  
    The IPL Analytics Hub 2026 is designed to inspire fans, empower analysts, 
    and support students in exploring the fascinating world of cricket through data.
    """)




    st.divider()
    st.title("🙏 Thank You")
    st.divider()

    st.subheader("💡 Closing Note")
    st.write("""
    Thank you for exploring the **IPL Analytics Hub 2026**.  
    This project was built to bring together the excitement of cricket and the power of data science.  
    We hope the interactive visualizations and insights helped you understand the tournament better 
    and inspired you to explore sports analytics further.
    """)
    

