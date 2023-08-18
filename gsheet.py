from gspreadsheet import GSpreadsheet
reader = GSpreadsheet("https://docs.google.com/spreadsheets/d/1iEglpQdbpbISokTyPJZonYN2XRHrMGtEUHm3cXcakZM/edit?usp=sharing")
reader.to_JSON()
