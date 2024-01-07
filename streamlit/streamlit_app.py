import streamlit as st
from sqlalchemy.sql import text

conn = st.connection('pets_db', type='sql')

with conn.session as s:
    s.execute(text('CREATE TABLE IF NOT EXISTS pet_owners (person TEXT, pet TEXT);'))
    s.execute(text('DELETE FROM pet_owners;'))
    pet_owners = {'ahsan':'puppy','mohsin':'cat','haider':'bear','faisal':"snake"}
    for p in pet_owners:    
        s.execute(text(
            'INSERT INTO pet_owners (person, pet) VALUES (:owner, :pet);'),
             params=dict(owner=p, pet=pet_owners[p]))
        s.commit()

pet_owners = conn.query('select * from pet_owners')

st.dataframe(pet_owners)