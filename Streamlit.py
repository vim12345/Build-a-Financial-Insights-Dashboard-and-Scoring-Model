import streamlit as st

# Streamlit App
st.title("Financial Insights Dashboard")

uploaded_file = st.file_uploader("Upload your CSV file", type="csv")

if uploaded_file:
    file_path = "family_financial_and_transactions_data.xlsx"  # Replace with your file's path
    df = pd.read_excel(file_path)
    st.write(df.head())

    # Display family scores
    family_scores = df.groupby('Family ID')['Financial Score'].mean().reset_index()
    st.bar_chart(family_scores, x='Family ID', y='Financial Score', use_container_width=True)

    # Recommendations
    st.write("### Recommendations")
    for _, row in df.iterrows():
        if row['Financial Score'] < 50:
            st.write(f"Family {row['Family ID']}: Consider reducing discretionary spending and increasing savings.")
