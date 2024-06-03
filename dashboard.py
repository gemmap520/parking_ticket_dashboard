import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

# Load the data
df = pd.read_csv('processed_parking_tickets.csv')

# Rename columns for clarity
df.columns = ['Year', 'Infraction_Code', 'Infraction_Description', 'Location', 'Total_Fine_Amount', 'Ticket_Count']

# Set Streamlit page title
st.title("Parking Tickets Analysis Dashboard")

# Sidebar for user input
st.sidebar.title("Select Graphs to Display")
yearly_trend = st.sidebar.checkbox("Yearly Trend of Parking Tickets")
total_fine_by_year = st.sidebar.checkbox("Total Fine Amount by Year")
top_locations = st.sidebar.checkbox("Top 10 Locations with Most Tickets")
infraction_distribution = st.sidebar.checkbox("Distribution of Infraction Types")
infraction_fines = st.sidebar.checkbox("Total Fine Amount by Infraction Type")
fine_vs_ticket_scatter = st.sidebar.checkbox("Scatter Plot: Fine Amount vs. Ticket Count by Location")
heatmap_tickets = st.sidebar.checkbox("Heat Map: Ticket Count by Location and Year")
heatmap_fines = st.sidebar.checkbox("Heat Map: Fine Amount by Location and Year")
infraction_code_dist = st.sidebar.checkbox("Infraction Code Distribution Over the Years")

# Year range selection
min_year = int(df['Year'].min())
max_year = int(df['Year'].max())
year_range = st.slider("Select Year Range", min_year, max_year, (min_year, max_year))

# Filter data based on selections
filtered_df = df[(df['Year'] >= year_range[0]) & (df['Year'] <= year_range[1])]

# Draw graphs based on user selection
if yearly_trend:
    st.subheader("Yearly Trend of Parking Tickets")
    yearly_tickets = filtered_df.groupby('Year')['Ticket_Count'].sum().reset_index()
    plt.figure(figsize=(10, 6))
    sns.barplot(data=yearly_tickets, x='Year', y='Ticket_Count', palette='viridis')
    plt.title('Yearly Trend of Parking Tickets')
    st.pyplot(plt)

if total_fine_by_year:
    st.subheader("Total Fine Amount by Year")
    yearly_fines = filtered_df.groupby('Year')['Total_Fine_Amount'].sum().reset_index()
    plt.figure(figsize=(10, 6))
    sns.lineplot(data=yearly_fines, x='Year', y='Total_Fine_Amount', marker='o', palette='viridis')
    plt.title('Total Fine Amount by Year')
    plt.xticks(yearly_fines['Year'])
    st.pyplot(plt)


if top_locations:
    st.subheader("Top 10 Locations with Most Tickets")
    top_locations = filtered_df.groupby('Location')['Ticket_Count'].sum().nlargest(10).reset_index()
    plt.figure(figsize=(10, 6))
    sns.barplot(data=top_locations, x='Ticket_Count', y='Location', palette='viridis')
    plt.title('Top 10 Locations with Most Tickets')
    st.pyplot(plt)

if infraction_distribution:
    st.subheader("Distribution of Infraction Types")
    infraction_distribution = filtered_df.groupby('Infraction_Description')['Ticket_Count'].sum().nlargest(10).reset_index()
    plt.figure(figsize=(10, 6))
    sns.barplot(data=infraction_distribution, x='Ticket_Count', y='Infraction_Description', palette='viridis')
    plt.title('Distribution of Infraction Types')
    st.pyplot(plt)

if infraction_fines:
    st.subheader("Total Fine Amount by Infraction Type")
    infraction_fines = filtered_df.groupby('Infraction_Description')['Total_Fine_Amount'].sum().nlargest(10).reset_index()
    plt.figure(figsize=(10, 6))
    sns.barplot(data=infraction_fines, x='Total_Fine_Amount', y='Infraction_Description', palette='viridis')
    plt.title('Total Fine Amount by Infraction Type')
    st.pyplot(plt)

if fine_vs_ticket_scatter:
    st.subheader("Scatter Plot: Fine Amount vs. Ticket Count by Location")
    plt.figure(figsize=(10, 6))
    sns.scatterplot(data=filtered_df, x='Total_Fine_Amount', y='Ticket_Count', hue='Location', palette='viridis')
    plt.title('Fine Amount vs. Ticket Count by Location')
    st.pyplot(plt)

if heatmap_tickets:
    st.subheader("Heat Map: Ticket Count by Location and Year")
    heatmap_data = filtered_df.pivot_table(index='Location', columns='Year', values='Ticket_Count', aggfunc='sum', fill_value=0)
    plt.figure(figsize=(12, 8))
    sns.heatmap(heatmap_data, cmap='viridis')
    plt.title('Heat Map of Ticket Count by Location and Year')
    st.pyplot(plt)

if heatmap_fines:
    st.subheader("Heat Map: Fine Amount by Location and Year")
    heatmap_fines = filtered_df.pivot_table(index='Location', columns='Year', values='Total_Fine_Amount', aggfunc='sum', fill_value=0)
    plt.figure(figsize=(12, 8))
    sns.heatmap(heatmap_fines, cmap='viridis')
    plt.title('Heat Map of Fine Amount by Location and Year')
    st.pyplot(plt)

if infraction_code_dist:
    st.subheader("Infraction Code Distribution Over the Years")
    infraction_code_dist = filtered_df.groupby(['Year', 'Infraction_Code'])['Ticket_Count'].sum().unstack().fillna(0)
    plt.figure(figsize=(12, 8))
    sns.heatmap(infraction_code_dist, cmap='viridis')
    plt.title('Infraction Code Distribution Over the Years')
    st.pyplot(plt)
