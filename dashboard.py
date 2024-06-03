import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
import matplotlib.ticker as ticker

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
heatmap_tickets = st.sidebar.checkbox("Heat Map: Ticket Count by Location and Year")
heatmap_fines = st.sidebar.checkbox("Heat Map: Fine Amount by Location and Year")
heatmap_infraction_distribution = st.sidebar.checkbox("Heat Map: Infraction Distribution by Year and Code")

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
    sns.lineplot(data=yearly_fines, x='Year', y='Total_Fine_Amount', marker='o')
    plt.title('Total Fine Amount by Year')
    plt.xticks(yearly_fines['Year'])
    plt.ylabel('Total Fine Amount ($)')
    plt.gca().yaxis.set_major_formatter(ticker.FuncFormatter(lambda x, _: f'{x/1e6:.0f}M'))
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

if heatmap_tickets:
    st.subheader("Heat Map: Ticket Count by Location and Year")
    top_locations = filtered_df['Location'].value_counts().nlargest(10).index
    heatmap_data = filtered_df[filtered_df['Location'].isin(top_locations)].pivot_table(
        index='Location', columns='Year', values='Ticket_Count', aggfunc='sum', fill_value=0)
    plt.figure(figsize=(12, 8))
    sns.heatmap(heatmap_data, cmap='viridis', annot=True, fmt="d")
    plt.title('Heat Map of Ticket Count by Location and Year')
    st.pyplot(plt)

if heatmap_infraction_distribution:
    st.subheader("Heat Map: Infraction Distribution by Year")
    
    # Get the top 10 infraction descriptions
    top_infractions = filtered_df.groupby('Infraction_Description')['Ticket_Count'].sum().nlargest(10).index
    top_infraction_df = filtered_df[filtered_df['Infraction_Description'].isin(top_infractions)]
    
    heatmap_infraction = top_infraction_df.pivot_table(index='Infraction_Description', columns='Year', values='Ticket_Count', aggfunc='sum', fill_value=0)
    plt.figure(figsize=(12, 8))
    sns.heatmap(heatmap_infraction, cmap='viridis', annot=True, fmt=".1f")
    plt.title('Heat Map of Top 10 Infraction Distribution by Year and Code')
    st.pyplot(plt)

if heatmap_fines:
    st.subheader("Heat Map: Fine Amount by Location and Year")
    top_locations = filtered_df['Location'].value_counts().nlargest(10).index
    heatmap_fines = filtered_df[filtered_df['Location'].isin(top_locations)].pivot_table(
        index='Location', columns='Year', values='Total_Fine_Amount', aggfunc='sum', fill_value=0)
    plt.figure(figsize=(12, 8))
    sns.heatmap(heatmap_fines, cmap='viridis', annot=True, fmt=".1f")
    plt.title('Heat Map of Fine Amount by Location and Year')
    st.pyplot(plt)
