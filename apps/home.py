import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_agg import RendererAgg
import seaborn as sns
import gspread as gs
import gspread_dataframe as gd
from oauth2client.service_account import ServiceAccountCredentials

st.set_page_config(layout="wide")
sns.set_style('darkgrid')
_lock = RendererAgg.lock


# gsheets import - ctrl+k ctrl+c comments, ctrl+k ctrl+u uncomments
# scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']
# creds = ServiceAccountCredentials.from_json_keyfile_name('nutritionKey.json', scope)
# client = gs.authorize(creds)
# sheet = client.open('nutrition')
# sheet_instance = sheet.worksheet('main')
# records_df = gd.get_as_dataframe(sheet_instance)
records_df = pd.read_csv('nutrition - sample.csv')
records_df['date'] = pd.to_datetime(records_df['date'])
records_df['weight'] = pd.to_numeric(records_df['weight'])


def app():
    row0_spacer1, row0_1, row0_spacer2, row0_2, row0_spacer3 = st.columns(
    (.1, 2, .2, 1, .1))

    with row0_2:
        st.write('')
        st.write('')
        

    row0_2.header(
        'Home')
    st.write('')
    st.write('')

    row1_spacer1, row1_1, row1_spacer2 = st.columns((.1, 3.2, .1))

    with row1_1:
        st.write('7 last recorded days:')
        st.write(records_df.tail(7))
        records_df['date_only'] = records_df['date'].dt.date

    
    row2_space1, row2_1, row2_space2, row2_2, row2_space3 = st.columns((.1, 1, .1, 1, .1))

    with row2_1, _lock: 
        st.subheader("Weight")
        fig = Figure()
        ax = fig.subplots()
        sns.lineplot(x=records_df['date_only'],y=records_df['weight'], color='blue', ax=ax, markers=True)
        
        #ax.set_ylabel('Weight')
        ax.set(ylim=(0, max(records_df['weight'])+5), ylabel = 'Weight', xlabel = '')
        ax.set_xticklabels(records_df['date_only'], rotation = 45)
        st.pyplot(fig)

    with row2_2, _lock:
        st.subheader("Calories-intake")
        fig = Figure()
        ax = fig.subplots()
        sns.lineplot(x=records_df['date_only'],y=records_df['calories'], color='green', ax = ax, markers=True)
        ax.set(ylim=(0, max(records_df['calories'])+50), ylabel = 'Calories', xlabel = '')
        ax.set_xticklabels(records_df['date_only'], rotation = 45)
        st.pyplot(fig)

    row3_space1, row3_1, row3_space2, row3_2, row3_space3 = st.columns((.1, 1, .1, 1, .1))
    with row3_1, _lock: 
        st.subheader("Macros")
        fig = Figure()
        ax = fig.subplots()
        t = records_df.loc[:, ['date_only', 'carbs', 'protein', 'fat']].melt(id_vars='date_only', var_name = 'macros', value_name = 'grams')
        sns.lineplot(x=t['date_only'],y=t['grams'], hue = t['macros'], color='goldenrod', ax=ax, markers=True)
        
        #ax.set_ylabel('Weight')
        ax.set(ylim=(0, max(t['grams'])+5), ylabel = 'Grams', xlabel = '')
        ax.set_xticklabels(records_df['date_only'], rotation = 45)
        st.pyplot(fig)

    with row3_2, _lock:
        st.subheader("Calories burnt")
        fig = Figure()
        ax = fig.subplots()
        sns.lineplot(x=records_df['date_only'],y=records_df['calories_burnt'], color='goldenrod', ax = ax, markers=True)
        ax.set(ylim=(0, max(records_df['calories_burnt'])+50), ylabel = 'Calories burnt', xlabel = '')
        ax.set_xticklabels(records_df['date_only'], rotation = 45)
        st.pyplot(fig)

    with st.expander('See more'):
        st.write("""
        This is an expander module that may or may not work
        """)