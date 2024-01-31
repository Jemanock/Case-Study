import streamlit as st
import queries
import devices
import users
import reservations


# Eine Überschrift der ersten Ebene
st.write("# Management System")
# Eine Überschrift der zweiten Ebene



tab1, tab2, tab3, tab4 = st.tabs(["Devices","Reservations","Maintenance","User"])
with tab1:
    st.header("Devices")
# Eine Auswahlbox mit hard-gecoded Optionen, das Ergebnis
# wird in current_device_example gespeichert
    current_device = st.selectbox(
    'Select Device',options = queries.find_devices(), key="Devices")
    st.write(F"Selected Device: {current_device}")

    devname = st.text_input("New Device Name", key="New Device Name")
    if st.button("Add new Device",key="Add new Device"):
        st.write(F"Device {devname} added")
        added_diviece = devices.Device(devname, '0')
        added_diviece.store_data()
        st.rerun()

    if st.button("Delete selected Device",key="Delete selected Device"):
        st.write(F"Device {current_device} deleted")

        selected_device = devices.Device.load_data_by_device_name(current_device)
        selected_device.delete_data()
        st.rerun()

    
with tab2:
    st.header("Reservations")

    with st.expander("Add new Reservation"):
        start,end = st.columns(2)
        start_dev = start.selectbox("Device",options = queries.find_devices(), key="Select Device")
        start_name = start.selectbox("User",options = queries.find_users(), key="Select User")
        start_date = start.date_input("Start Date", key="Start Date")
        start_time = start.time_input("Start Time", key="Start Time")
        end_date = end.date_input("End Date", key="End Date")
        end_time = end.time_input("End Time", key="End Time")
        res_id = f"{start_name}_{start_dev}"

        if st.button("Add Reservation",key="Add_Reservation"):
            st.write(F"Reservation {res_id} added")
            added_reservation = reservations.Reservation(res_id, start_date, start_time, end_date, end_time, start_dev, start_name)
            added_reservation.store_data()
            st.rerun()
    
    with st.expander("View Reservations"):
        current_res = st.selectbox(
        'Select Reservation',options = queries.find_reservations(), key="Reservation")
        st.write(F"Selected Reservation: {current_res}")
        selected_res = reservations.Reservation.load_data_by_res_name(current_res)
        #st.write(F"{selected_res.print()}")
        

        if st.button("Delete selected Reservation",key="Delete selected Reservation"):
            st.write(F"Reservation {current_res} deleted")

            
            selected_res.delete_data()
            st.rerun()

    st.dataframe(reservations.Reservation.load_all())    

    
with tab3:
    st.header("Maintenance")
    with st.expander("Add new Maintenance"):
        start,end = st.columns(2)
        start_dev = start.selectbox("Device",options = queries.find_devices(), key="Select Device to maintain")
        start_name = start.selectbox("User",options = queries.find_users(), key="Select Maintenance User")
        start_date = start.date_input("Start Date", key="Start Date Maintenance")
        start_time = start.time_input("Start Time", key="Start Time Maintenance")
        end_date = end.date_input("End Date", key="End Date Maintenance")
        end_time = end.time_input("End Time", key="End Time Maintenance")
        res_id = f"Maintenance_{start_dev}"

        if st.button("Add Maintenance",key="Add_Maintenance"):
            st.write(F"Maintenance {res_id} added")
            added_maintenance = reservations.Reservation(res_id, start_date, start_time, end_date, end_time, start_dev, start_name)
            added_maintenance.store_data()
            st.rerun()

    with st.expander("View Reservations and Maintenance"):
        current_res = st.selectbox(
        'Select Reservation or Maintenance',options = queries.find_reservations(), key="Reservation or Maintenance")
        st.write(F"Selected Reservation or Maintenance: {current_res}")
        selected_res = reservations.Reservation.load_data_by_res_name(current_res)
        #st.write(F"{selected_res.print()}")
        

        if st.button("Delete selected Reservation or Maintenance",key="Delete selected Reservation or Maintenance"):
            st.write(F"Reservation or Maintenance {current_res} deleted")

            
            selected_res.delete_data()
            st.rerun()

    st.dataframe(reservations.Reservation.load_all())
    

with tab4: 
    st.header("User")

    current_user_example = st.selectbox(
    'Select User',options = queries.find_users(), key="Users") # devices werden ausgegeben und nicht 
    st.write(F"Selected Device: {current_user_example}")

    username = st.text_input("New Username", key="New User Name")
    if st.button("Add new User",key="Add new User"):
        st.write(F"User {username} added")
        added_user = users.User(0, username)
        added_user.store_data()
        st.rerun()

    if st.button("Delete selected User",key="Delete selected User"):
        st.write(F"User {current_user_example} deleted")

        selected_user = users.User.load_data_by_user_name(current_user_example)
        selected_user.delete_data()
        st.rerun()
    

