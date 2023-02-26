import pandas as pd
import streamlit as st
import plotly.express as px

# page config
st.set_page_config(
    page_title='pokemon app',
    page_icon='👌',
    layout='wide'
)
st.sidebar.title('🦖🦕 pokemon app')
st.image( 'pokelysis/pikachu.jpeg', use_column_width= True)

# load data
@st.cache_data
def load_pokemon():
    data = pd.read_csv('pokelysis/pokemon.csv', index_col=0)
    return data

with st.spinner('loading pokemon data ...'):
    pokemon = load_pokemon()
    st.sidebar.success("loaded pokemon data")

show_data = st.sidebar.checkbox ('Show the dataset')
if show_data:
    st.subheader ('Pokemon Data')
    st.dataframe(pokemon, use_container_width = True)

type1 = st.sidebar.selectbox('Select Pokemon Type', pokemon ['Type 1'].unique())
subset = pokemon [pokemon['Type 1'] == type1 ] #filter

tabs = st.tabs(['Data', 'Univariant Analysis', 'Bivariate Analysis'])

# Data tab
tabs[0].subheader(f'{type1} Pokemons')
tabs[0].dataframe(subset, use_container_width = True)

# Univariate Analysis Tool
# Attack
ss = subset.sort_values(by = 'Attack')
fig1 = px.histogram (ss, x = 'Attack', nbins = 20)
fig2 = px.bar (ss, x = 'Name', y = 'Attack')
tabs[1].subheader(f'{type1} Stats')
type[1].subheader('Attack')
tabs[1].plotly_chart(fig1, use_container_width = True)
tabs[1].plotly_chart(fig2, use_container_width = True)

# Defense
ss = subset.sort_values(by = 'Defense')
fig1 = px.histogram (ss, x = 'Defense', nbins = 20)
fig2 = px.bar (ss, x = 'Name', y = 'Defense')
tabs[1].subheader(f'{type1} Stats')
type[1].subheader('Defense')
tabs[1].plotly_chart(fig1, use_container_width = True)
tabs[1].plotly_chart(fig2, use_container_width = True)

# can be done the same for HP, Sp. Atk, Sp. Def, Speed

# Bivariate Analysis tab
