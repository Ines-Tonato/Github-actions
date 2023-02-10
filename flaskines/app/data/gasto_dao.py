from app.data.models.gasto import Gasto


class GastoDao:
    def select_all(self,db) -> list[Gasto]:
        cursor = db.cursor()
        cursor.execute('SELECT * FROM gastos')
        gastos_en_db = cursor.fetchall()
        gastos : list[Gasto]=list()
        for gasto_en_db in gastos_en_db:
           gastos.append(Gasto(gasto_en_db[0],gasto_en_db[1],gasto_en_db[2],gasto_en_db[3],gasto_en_db[4] ))
        cursor.close()
        return gastos