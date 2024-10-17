# Imports
import streamlit as st
import pandas as pd
import seaborn as sns
import warnings
warnings.filterwarnings("ignore")

# 1. title
st.title("Data Analysis")
st.subheader("Data Analysis using Python & Streamlit")

# 2. uploading file
upload = st.file_uploader("Upload your dataset (CSV file) here")
if upload is not None:
    data = pd.read_csv(upload)

# 3. display dataset    
if upload is not None:
    if st.checkbox("Preview Dataset"):
        if st.button("Head"):
            st.write(data.head())
        if st.button("Tail"):
            st.write(data.tail())
            
# 4. check data type of each column
if upload is not None:
    if st.checkbox("DataType of Each Column"):
        st.text("DataTypes")
        st.write(data.dtypes.astype(str))

# 5. find shape of the dataset
if upload is not None:
    if st.checkbox("Number rows and columns:"):
        st.text("Number of rows")
        st.write(data.shape[0])
        st.text("Number of columns")
        st.write(data.shape[1])
        
# 6. check null values
if upload is not None:
    test = data.isnull().values.any()
    if test == True:
        if st.checkbox("Null values in the dataset"):
            sns.heatmap(data.isnull())
            st.pyplot()
            st.set_option('deprecation.showPyplotGlobalUse', False)
    else:
        st.success("No null values.")

# 7. find duplicated values
if upload is not None:
    test = data.duplicated().any()
    if test == True:
        st.warning("This dataset contains duplicate values.")
        dup = st.selectbox("Do you want to delete duplicates?",\
                           ("Select one", "Yes", "No"))
        if dup == "Yes":
            data = data.drop_duplicates()
            st.text("Duplicate values are removed.")
        else:
            st.text("Duplicates are not removed.")
            
# 8. get overall stats 
if upload is not None:
    if st.checkbox("Summary of The Dataset"):
        # Describe non-numeric columns separately (like course_title)
        st.write(data.describe(exclude=[object]))

        
# 9. About section

if st.button("About app"):
    st.text("Built with Streamlit by Charan K.")
    
            