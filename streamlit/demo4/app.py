# Import python packages
import streamlit as st
from snowflake.snowpark.context import get_active_session



# Write directly to the app
st.title("Snowflake Streamlit App :balloon:")
st.write(
    """List all the streamlit apps in my streamlit  database
    """
)


session = get_active_session()

sql = f"SELECT STAGE_NAME, CREATED FROM  STREAMLIT_DEV.INFORMATION_SCHEMA.STAGES "

data = session.sql(sql).collect()
# Display list of stages in Streamlit
st.write("List of stages:")

st.write(data)

stages = [row[1] for row in data]

st.write("Number of Streamlit apps:", len(stages))