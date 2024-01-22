import streamlit as st
import queries
import devices
import users


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

        device_manager = devices.Device.load_data_by_device_name(current_device)
        # Der Gerätenamen, den Sie löschen möchten
        #device_name_to_delete = current_device
        # Aufruf der delete_data-Methode
        device_manager.delete_data()
        st.rerun()

    
with tab2:
    st.header("Reservations")

    with st.expander("Add new Reservation"):
        start,end = st.columns(2)
        start_res = start.selectbox("Device",options = ["Dev1","Dev2","Dev3"], key="Start Device")
        end_name = end.text_input("Name", key="E_Name")
        start_date = start.date_input("Start Date", key="Start Date")
        start_time = start.time_input("Start Time", key="Start Time")
        end_date = end.date_input("End Date", key="End Date")
        end_time = end.time_input("End Time", key="End Time")
        if st.button("Add Reservation",key="Add_Reservation"):
            st.success(F"Reservation {end_name} added")
    current_reservation_example = st.selectbox("Select Reservation",options = ["Res1","Res2","Res3"], key="Reservations")
    if st.button("Delete selected Reservation",key="Delete Reservation"):
       st.write("Reservation deleted")
    
with tab3:
    st.header("Maintenace")

    with st.expander("Add new Maintenance"):
        start,end = st.columns(2)
        start_mtn = start.selectbox("Device",options = ["Dev1","Dev2","Dev3"], key="Start_mtn")
        end_name_mtn = end.text_input("Name", key="E_mtn_Name")
        start_mtn_date = start.date_input("Maintenance Date", key="Mtn_Date")
        if st.button("Add Maintenance",key="Add_Maintenance"):
            st.success(F"Maintenence {end_name_mtn} added")
    current_mtn_example = st.selectbox("Select Maintenance",options = ["Mtn1","Mtn2","Mtn3"], key="Maintenances")
    if st.button("Delete selected Maintenance",key="Delete Maintenance"):
       st.write("Maintenance deleted")

with tab4: 
    st.header("User")

    current_user_example = st.selectbox(
    'Select User',options = queries.find_devices(), key="Users") # devices werden ausgegeben und nicht 
    st.write(F"Selected Device: {current_user_example}")

    usrname = st.text_input("New Username", key="New User Name")
    if st.button("Add new User",key="Add new User"):
        st.write(F"User {usrname} added")
        added_user = users.User(usrname, '0')
        added_user.store_data()
        st.rerun

    if st.button("Delete selected User",key="Delete selected User"):
        st.write(F"User {current_user_example} deleted")
        user_manager = users.User.load_data_by_user_name(current_user_example)
        user_manager.delete_data()
        st.rerun
        