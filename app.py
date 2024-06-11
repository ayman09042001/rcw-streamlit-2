import streamlit as st
import snowflake.connector as sc
import pandas as pd
def main():
    st.write("### DASHBOARD d'affichage des données de la table etudiants ###") 
    try:
        con = sc.connect(
            account = 'kjbusla-kf63760',
            user = 'AEDDAHBI5',
            password = 'Ziad.akodad02'
        )
        cursor = con.cursor()
    except:
        st.warning("Une erreur est survenue")

    def dataEtudiants():
        sql = "SELECT * FROM rcw.persons.etudiants"
        df = cursor.execute(sql).fetchall()
        return pd.DataFrame(df, columns = ['Nom', 'PRENOM', 'AGE'])
    donnees = dataEtudiants()
    st.write(donnees)

if __name__ == "__main__":
    main()