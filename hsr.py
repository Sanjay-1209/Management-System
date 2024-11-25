# # # # # import streamlit as st
# # # # # import gspread
# # # # # from oauth2client.service_account import ServiceAccountCredentials
# # # # # import pandas as pd
# # # # # import plotly.express as px

# # # # # # Step 1: Authentication and Google Sheets Access
# # # # # def authenticate_google_sheets():
# # # # #     scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/spreadsheets", "https://www.googleapis.com/auth/drive.file", "https://www.googleapis.com/auth/drive"]
# # # # #     creds = ServiceAccountCredentials.from_json_keyfile_name('path_to_your_service_account_key.json', scope)
# # # # #     client = gspread.authorize(creds)
# # # # #     return client

# # # # # # Step 2: Fetch Lead Data from Google Sheets
# # # # # def get_leads_data():
# # # # #     client = authenticate_google_sheets()
# # # # #     sheet = client.open("HSR_Motors_Leads").sheet1  # Replace with your Google Sheet name
# # # # #     data = sheet.get_all_records()  # Fetch all rows
# # # # #     df = pd.DataFrame(data)
# # # # #     return df

# # # # # # Step 3: Function to Display Lead Listing
# # # # # def lead_listing():
# # # # #     st.title("Lead Listing")
# # # # #     st.write("### Overview of all received leads.")
    
# # # # #     # Load data from Google Sheets
# # # # #     df = get_leads_data()
    
# # # # #     # Filter Leads by Status
# # # # #     status_filter = st.selectbox("Filter by Lead Status", options=["All", "New", "Contacted", "Not Interested"])
# # # # #     if status_filter != "All":
# # # # #         df_filtered = df[df["Status"] == status_filter]
# # # # #     else:
# # # # #         df_filtered = df
    
# # # # #     st.dataframe(df_filtered)

# # # # # # Step 4: Function to Display Lead Details
# # # # # def lead_details():
# # # # #     st.title("Lead Details")
    
# # # # #     # User selects a Lead ID to view details
# # # # #     df = get_leads_data()
# # # # #     lead_id = st.number_input("Enter Lead ID", min_value=1, max_value=len(df), step=1)
    
# # # # #     if lead_id:
# # # # #         lead = df[df["Lead ID"] == lead_id].iloc[0]
# # # # #         st.write(f"### Lead Information")
# # # # #         st.write(f"**Name**: {lead['Name']}")
# # # # #         st.write(f"**Source**: {lead['Source']}")
# # # # #         st.write(f"**Phone**: {lead['Phone']}")
# # # # #         st.write(f"**Email**: {lead['Email']}")
# # # # #         st.write(f"**Status**: {lead['Status']}")

# # # # #         # Update Lead Status
# # # # #         new_status = st.selectbox("Update Lead Status", options=["New", "Contacted", "Not Interested"], index=["New", "Contacted", "Not Interested"].index(lead["Status"]))
# # # # #         if st.button("Update Status"):
# # # # #             sheet = authenticate_google_sheets().open("HSR_Motors_Leads").sheet1
# # # # #             cell = sheet.find(str(lead_id))  # Find the Lead ID cell
# # # # #             sheet.update_cell(cell.row, cell.col + 4, new_status)  # Update the Status column
# # # # #             st.success(f"Lead status updated to: {new_status}")

# # # # # # Step 5: Dashboard Visualization
# # # # # def dashboard():
# # # # #     st.title("Dashboard")
    
# # # # #     # Fetch data
# # # # #     df = get_leads_data()

# # # # #     # Lead Status Distribution
# # # # #     status_counts = df["Status"].value_counts().reset_index()
# # # # #     status_counts.columns = ["Status", "Count"]
# # # # #     fig = px.bar(status_counts, x="Status", y="Count", title="Lead Status Distribution", color="Status")
# # # # #     st.plotly_chart(fig)

# # # # #     # Lead Source Distribution
# # # # #     source_counts = df["Source"].value_counts().reset_index()
# # # # #     source_counts.columns = ["Source", "Count"]
# # # # #     fig2 = px.pie(source_counts, names="Source", values="Count", title="Lead Source Distribution")
# # # # #     st.plotly_chart(fig2)

# # # # #     # Show Total Leads and Active Leads
# # # # #     total_leads = len(df)
# # # # #     active_leads = len(df[df["Status"] == "New"])

# # # # #     st.write(f"**Total Leads**: {total_leads}")
# # # # #     st.write(f"**Active Leads (New)**: {active_leads}")

# # # # # # Step 6: Sidebar Navigation
# # # # # def main():
# # # # #     st.sidebar.title("HSR Motors Lead Management")
    
# # # # #     option = st.sidebar.radio("Select a Screen", ["Lead Listing", "Lead Details", "Dashboard"])

# # # # #     if option == "Lead Listing":
# # # # #         lead_listing()
# # # # #     elif option == "Lead Details":
# # # # #         lead_details()
# # # # #     elif option == "Dashboard":
# # # # #         dashboard()

# # # # # # Run the app
# # # # # if __name__ == "__main__":
# # # # #     main()





# # # import streamlit as st
# # # import pandas as pd
# # # import gspread
# # # from google.oauth2.service_account import Credentials
# # # import plotly.express as px

# # # # # Set up the credentials for accessing Google Sheets
# # # # creds = Credentials.from_service_account_file(r'C:\Users\sanja\OneDrive\Desktop\DeltaX\myfirst-434417-56e48925530b.json')  # Replace with your credentials path


# # # scopes = ["https://www.googleapis.com/auth/spreadsheets", "https://www.googleapis.com/auth/drive.readonly"]
# # # creds = Credentials.from_service_account_file(
# # #     r'C:\Users\sanja\OneDrive\Desktop\DeltaX\myfirst-434417-56e48925530b.json',
# # #     scopes=scopes
# # # )
# # # client = gspread.authorize(creds)
# # # # The ID of your Google Sheet (from the URL)
# # # sheet_id = '16503rram7sWp50q6221OozEdi8t1YNiPSfao0X414ss'  # Replace with your actual Sheet ID
# # # sheet = client.open_by_key(sheet_id).worksheet('HSR_Motors_Leads')  # Replace with your sheet name

# # # # Fetch data from Google Sheets into a DataFrame
# # # data = pd.DataFrame(sheet.get_all_records())

# # # # Function to render Lead Listing
# # # def lead_listing():
# # #     st.title("Lead Listing")
# # #     st.subheader("View all leads and their status")
    
# # #     # Filter by lead status
# # #     status_filter = st.selectbox("Filter by Status", ["All", "New", "Contacted", "Not Interested"])
    
# # #     if status_filter != "All":
# # #         filtered_data = data[data['Status'] == status_filter]
# # #     else:
# # #         filtered_data = data
    
# # #     st.dataframe(filtered_data)

# # # # Function to render Lead Details
# # # def lead_details():
# # #     st.title("Lead Details")
# # #     st.subheader("View detailed lead information")
    
# # #     # Select lead by Lead ID
# # #     lead_id = st.selectbox("Select Lead ID", data['Lead ID'].unique())
# # #     lead_details = data[data['Lead ID'] == lead_id]
    
# # #     if not lead_details.empty:
# # #         st.write(f"**Name**: {lead_details['Name'].values[0]}")
# # #         st.write(f"**Phone**: {lead_details['Phone'].values[0]}")
# # #         st.write(f"**Email**: {lead_details['Email'].values[0]}")
# # #         st.write(f"**Source**: {lead_details['Source'].values[0]}")
# # #         st.write(f"**Status**: {lead_details['Status'].values[0]}")
# # #         st.write(f"**Campaign**: {lead_details['Campaign'].values[0]}")
        
# # #         # Update Status
# # #         new_status = st.selectbox("Update Status", ["New", "Contacted", "Not Interested"], index=["New", "Contacted", "Not Interested"].index(lead_details['Status'].values[0]))
# # #         if st.button("Update Status"):
# # #             sheet.update_cell(lead_details.index[0] + 2, 6, new_status)  # Update the 'Status' column (column 6)
# # #             st.success("Status updated successfully!")

# # # # Function to render Dashboard (Charts)
# # # def dashboard():
# # #     st.title("Lead Management Dashboard")
# # #     st.subheader("Visualize leads data")
    
# # #     # Lead Status Distribution
# # #     status_count = data['Status'].value_counts()
# # #     fig1 = px.pie(status_count, names=status_count.index, values=status_count.values, title="Lead Status Distribution")
# # #     st.plotly_chart(fig1)
    
# # #     # Lead Source Distribution
# # #     source_count = data['Source'].value_counts()
# # #     fig2 = px.bar(source_count, x=source_count.index, y=source_count.values, title="Lead Source Distribution")
# # #     st.plotly_chart(fig2)

# # # # Sidebar Navigation
# # # st.sidebar.title("HSR Motors Lead Management")
# # # page = st.sidebar.radio("Select a page", ["Lead Listing", "Lead Details", "Dashboard"])

# # # # Render the selected page
# # # if page == "Lead Listing":
# # #     lead_listing()
# # # elif page == "Lead Details":
# # #     lead_details()
# # # elif page == "Dashboard":
# # #     dashboard()







# import streamlit as st
# import pandas as pd
# import gspread
# from google.oauth2.service_account import Credentials
# import plotly.express as px

# # Set up the credentials for accessing Google Sheets
# scopes = ["https://www.googleapis.com/auth/spreadsheets", "https://www.googleapis.com/auth/drive.readonly"]
# creds = Credentials.from_service_account_file(
#     r'C:\Users\sanja\OneDrive\Desktop\DeltaX\myfirst-434417-56e48925530b.json',
#     scopes=scopes
# )
# client = gspread.authorize(creds)
# # The ID of your Google Sheet (from the URL)
# sheet_id = '16503rram7sWp50q6221OozEdi8t1YNiPSfao0X414ss'  # Replace with your actual Sheet ID
# sheet = client.open_by_key(sheet_id).worksheet('HSR_Motors_Leads')  # Replace with your sheet name

# # Fetch data from Google Sheets into a DataFrame
# data = pd.DataFrame(sheet.get_all_records())

# # Function to render Lead Listing
# def lead_listing():
#     st.title("Lead Listing")
#     st.subheader("View all leads and their status")
    
#     # Filter by lead status
#     status_filter = st.selectbox("Filter by Status", ["All", "New", "Contacted", "Not Interested"])
    
#     if status_filter != "All":
#         filtered_data = data[data['Status'] == status_filter]
#     else:
#         filtered_data = data
    
#     st.dataframe(filtered_data)

# # Function to render Lead Details
# def lead_details():
#     st.title("Lead Details")
#     st.subheader("View detailed lead information")
    
#     # Select lead by Lead ID
#     lead_id = st.selectbox("Select Lead ID", data['Lead ID'].unique())
#     lead_details = data[data['Lead ID'] == lead_id]
    
#     if not lead_details.empty:
#         st.write(f"**Name**: {lead_details['Name'].values[0]}")
#         st.write(f"**Phone**: {lead_details['Phone'].values[0]}")
#         st.write(f"**Email**: {lead_details['Email'].values[0]}")
#         st.write(f"**Source**: {lead_details['Source'].values[0]}")
#         st.write(f"**Status**: {lead_details['Status'].values[0]}")
#         st.write(f"**Campaign**: {lead_details['Campaign'].values[0]}")

#         # Update Status
#         new_status = st.selectbox("Update Status", ["New", "Contacted", "Not Interested"], index=["New", "Contacted", "Not Interested"].index(lead_details['Status'].values[0]))
#         if st.button("Update Status"):
#             sheet.update_cell(lead_details.index[0] + 2, 6, new_status)  # Update the 'Status' column (column 6)
#             st.success("Status updated successfully!")

# # Function to render Add New Lead
# def add_new_lead():
#     st.title("Add New Lead")
#     st.subheader("Enter details for the new lead")
    
#     lead_id = st.text_input("Lead ID")
#     name = st.text_input("Name")
#     phone = st.text_input("Phone")
#     email = st.text_input("Email")
#     source = st.selectbox("Source", ["Facebook", "Twitter", "Google", "Website", "Offline"])
#     status = st.selectbox("Status", ["New", "Contacted", "Not Interested"])
#     campaign = st.text_input("Campaign")
    
#     if st.button("Add Lead"):
#         new_lead = {
#             "Lead ID": lead_id,
#             "Name": name,
#             "Phone": phone,
#             "Email": email,
#             "Source": source,
#             "Status": status,
#             "Campaign": campaign
#         }
#         # Update the Google Sheet with the new lead
#         sheet.append_row([new_lead["Lead ID"], new_lead["Name"], new_lead["Phone"], new_lead["Email"], new_lead["Source"], new_lead["Status"], new_lead["Campaign"]])
#         st.success("Lead added successfully!")

# # Function to render Dashboard (Charts)
# def dashboard():
#     st.title("Lead Management Dashboard")
#     st.subheader("Visualize leads data")
    
#     # Ensure that you have a column that has a valid datetime format (e.g., 'Date' or 'Lead Created Date')
#     # If 'Date' column exists, use it directly:
#     if 'Date' in data.columns:
#         data['Date'] = pd.to_datetime(data['Date'], errors='coerce')  # Coerce invalid parsing to NaT

#     # Lead Status Distribution
#     status_count = data['Status'].value_counts()
#     fig1 = px.pie(status_count, names=status_count.index, values=status_count.values, title="Lead Status Distribution")
#     st.plotly_chart(fig1)
    
#     # Lead Source Distribution
#     source_count = data['Source'].value_counts()
#     fig2 = px.bar(source_count, x=source_count.index, y=source_count.values, title="Lead Source Distribution")
#     st.plotly_chart(fig2)
    
#     # Lead Status Trend (Over time)
#     if 'Date' in data.columns:
#         status_trend = data.groupby([data['Date'].dt.to_period('M'), 'Status']).size().unstack().fillna(0)
#         fig3 = px.line(status_trend, title="Lead Status Trend Over Time")
#         st.plotly_chart(fig3)
    
#     # Lead Campaign Distribution
#     campaign_count = data['Campaign'].value_counts()
#     fig4 = px.bar(campaign_count, x=campaign_count.index, y=campaign_count.values, title="Lead Campaign Distribution")
#     st.plotly_chart(fig4)
    
#     # Lead Source to Status Conversion Rate (Percentage of leads contacted or not interested per source)
#     source_status_count = data.groupby(['Source', 'Status']).size().unstack().fillna(0)
#     source_status_rate = (source_status_count.T / source_status_count.sum(axis=1)).T * 100
#     fig5 = px.bar(source_status_rate, x=source_status_rate.index, y=source_status_rate.columns, barmode='group', title="Lead Source to Status Conversion Rate")
#     st.plotly_chart(fig5)

# # Sidebar Navigation
# st.sidebar.title("HSR Motors Lead Management")
# page = st.sidebar.radio("Select a page", ["Lead Listing", "Lead Details", "Add Lead", "Dashboard"])

# # Render the selected page
# if page == "Lead Listing":
#     lead_listing()
# elif page == "Lead Details":
#     lead_details()
# elif page == "Add Lead":
#     add_new_lead()
# elif page == "Dashboard":
#     dashboard()








pip install gspread

import streamlit as st
import pandas as pd
import gspread
from google.oauth2.service_account import Credentials
import plotly.express as px

# Set up the credentials for accessing Google Sheets
scopes = ["https://www.googleapis.com/auth/spreadsheets", "https://www.googleapis.com/auth/drive.readonly"]
creds = Credentials.from_service_account_file(
    r'C:\Users\sanja\OneDrive\Desktop\DeltaX\myfirst-434417-56e48925530b.json',
    scopes=scopes
)
client = gspread.authorize(creds)
# The ID of your Google Sheet (from the URL)
sheet_id = '16503rram7sWp50q6221OozEdi8t1YNiPSfao0X414ss'  # Replace with your actual Sheet ID
sheet = client.open_by_key(sheet_id).worksheet('HSR_Motors_Leads')  # Replace with your sheet name

# Fetch data from Google Sheets into a DataFrame
data = pd.DataFrame(sheet.get_all_records())
st.set_page_config(page_title="HSR Motors Lead Management", page_icon="🚘", layout="wide", initial_sidebar_state="expanded", menu_items=None)
# Function to render Lead Listing
def lead_listing():
    global data  # Declare data as global to modify it
    st.title("Lead Listing")
    st.subheader("View all leads and their status")
    
    # Filter by lead status
    status_filter = st.selectbox("Filter by Status", ["All", "New", "Contacted", "Not Interested"])
    
    if status_filter != "All":
        filtered_data = data[data['Status'] == status_filter]
    else:
        filtered_data = data
    
    st.dataframe(filtered_data)

# Function to render Lead Details
def lead_details():
    global data  # Declare data as global to modify it
    st.title("Lead Details")
    st.subheader("View detailed lead information")
    
    # Select lead by Lead ID
    lead_id = st.selectbox("Select Lead ID", data['Lead ID'].unique())
    lead_details = data[data['Lead ID'] == lead_id]
    
    if not lead_details.empty:
        st.write(f"**Name**: {lead_details['Name'].values[0]}")
        st.write(f"**Phone**: {lead_details['Phone'].values[0]}")
        st.write(f"**Email**: {lead_details['Email'].values[0]}")
        st.write(f"**Source**: {lead_details['Source'].values[0]}")
        st.write(f"**Status**: {lead_details['Status'].values[0]}")
        st.write(f"**Campaign**: {lead_details['Campaign'].values[0]}")

        # Update Status
        new_status = st.selectbox("Update Status", ["New", "Contacted", "Not Interested"], index=["New", "Contacted", "Not Interested"].index(lead_details['Status'].values[0]))
        if st.button("Update Status"):
            sheet.update_cell(lead_details.index[0] + 2, 6, new_status)  # Update the 'Status' column (column 6)
            st.success("Status updated successfully!")

# Function to render Add New Lead
def add_new_lead():
    global data  # Declare data as global to modify it
    st.title("Add New Lead")
    st.subheader("Enter details for the new lead")
    
    lead_id = st.text_input("Lead ID")
    name = st.text_input("Name")
    phone = st.text_input("Phone")
    email = st.text_input("Email")
    source = st.selectbox("Source", ["Facebook", "Twitter", "Google", "Website", "Offline"])
    status = st.selectbox("Status", ["New", "Contacted", "Not Interested"])
    campaign = st.text_input("Campaign")
    
    if st.button("Add Lead"):
        new_lead = {
            "Lead ID": lead_id,
            "Name": name,
            "Phone": phone,
            "Email": email,
            "Source": source,
            "Status": status,
            "Campaign": campaign
        }
        # Update the Google Sheet with the new lead
        sheet.append_row([new_lead["Lead ID"], new_lead["Name"], new_lead["Phone"], new_lead["Email"], new_lead["Source"], new_lead["Status"], new_lead["Campaign"]])
        # Update the data locally as well
        data = pd.DataFrame(sheet.get_all_records())  # Refresh data from the sheet
        st.success("Lead added successfully!")

# Function to render Delete Lead
def delete_lead():
    global data  # Declare data as global to modify it
    st.title("Delete Lead")
    st.subheader("Select and delete a lead by Lead ID")
    
    lead_id = st.selectbox("Select Lead ID", data['Lead ID'].unique())
    
    if st.button("Delete Lead"):
        # Get the row index where the lead_id is located
        lead_row = data[data['Lead ID'] == lead_id].index[0] + 2  # Google Sheets are 1-indexed, and row starts at 2
        
        # Convert lead_row to a regular int before passing it to the delete_rows method
        lead_row = int(lead_row)  # Ensure it's a regular int
        
        # Delete the lead from the Google Sheet
        sheet.delete_rows(lead_row)
        
        # Refresh the data in the app
        data = pd.DataFrame(sheet.get_all_records())  # Refresh data from the sheet
        st.success(f"Lead with Lead ID {lead_id} has been deleted successfully!")


# Function to render Dashboard (Charts)
def dashboard():
    global data  # Declare data as global to modify it
    st.title("Lead Management Dashboard")
    st.subheader("Visualize leads data")
    
    # Ensure that you have a column that has a valid datetime format (e.g., 'Date' or 'Lead Created Date')
    # If 'Date' column exists, use it directly:
    if 'Date' in data.columns:
        data['Date'] = pd.to_datetime(data['Date'], errors='coerce')  # Coerce invalid parsing to NaT
    col1 , col2 = st.columns(2)
    with col1:
        # Lead Status Distribution
        status_count = data['Status'].value_counts()
        fig1 = px.pie(status_count, names=status_count.index, values=status_count.values, title="Lead Status Distribution")
        st.plotly_chart(fig1)
    
    with col2:
        # Lead Source Distribution
        source_count = data['Source'].value_counts()
        fig2 = px.bar(source_count, x=source_count.index, y=source_count.values, title="Lead Source Distribution")
        st.plotly_chart(fig2)
        

    col3, col4 = st.columns(2)
    with col3:
        # Lead Status Trend (Over time)
        if 'Date' in data.columns:
            status_trend = data.groupby([data['Date'].dt.to_period('M'), 'Status']).size().unstack().fillna(0)
            fig3 = px.line(status_trend, title="Lead Status Trend Over Time")
            st.plotly_chart(fig3)
        
        # Lead Campaign Distribution
        campaign_count = data['Campaign'].value_counts()
        fig4 = px.bar(campaign_count, x=campaign_count.index, y=campaign_count.values, title="Lead Campaign Distribution")
        st.plotly_chart(fig4)
    with col4:
        # Lead Source to Status Conversion Rate (Percentage of leads contacted or not interested per source)
        source_status_count = data.groupby(['Source', 'Status']).size().unstack().fillna(0)
        source_status_rate = (source_status_count.T / source_status_count.sum(axis=1)).T * 100
        fig5 = px.bar(source_status_rate, x=source_status_rate.index, y=source_status_rate.columns, barmode='group', title="Lead Source to Status Conversion Rate")
        st.plotly_chart(fig5)

# Sidebar Navigation
st.sidebar.title("HSR Motors Lead Management")
page = st.sidebar.radio("Select a page", ["How to use" , "Lead Listing", "Lead Details", "Lead Management", "Dashboard"])

# Render the selected page
if page == "How to use":
    st.header("This tab provides a detailed guide on how to use the application.")
    st.header("Introduction")
    st.write("This application provides an intuitive interface for seamless lead management and data visualization. Below is an overview of its key features and functionalities:")
    
    st.header("Lead Listing")
    st.write("This tab displays comprehensive lead data sourced directly from the database (Google Sheets), accessible to both backend developers and end-users.")
    st.write("Includes a dynamic filter to view leads by status (e.g., All, New, etc.), enabling efficient data segmentation.")
    
    st.header("Lead Details")
    st.write("**This tab enables users to search for specific leads using their unique Lead ID.**")
    st.write("Users can update the status of any lead in real-time.")
    st.write("Updates are instantly reflected in the Lead Listing tab, ensuring consistency across the application. (You can verify this synchronization by revisiting the Lead Listing tab.)")

    st.header("Lead Management")
    st.write("**This tab offers functionality to add new leads and manage associated details.**")
    st.write("Designed for effortless lead creation and streamlined information handling.")

    st.header("Dashboard")
    st.write("**The primary dashboard provides insightful visualizations tailored to the client’s needs.**")
    st.write("Additional visualizations and advanced filters can be integrated as per specific requirements, ensuring a customized and data-driven user experience.")
if page == "Lead Listing":
    lead_listing()
elif page == "Lead Details":
    lead_details()
elif page == "Lead Management":
    action = st.selectbox("Choose an action", ["Add Lead", "Delete Lead"])
    if action == "Add Lead":
        add_new_lead()
    elif action == "Delete Lead":
        delete_lead()
elif page == "Dashboard":
    dashboard()
