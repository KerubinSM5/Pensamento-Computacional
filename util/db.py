import mysql.connector

class SQL:
    def __init__(self, servidor='localhost', usr='root', pwd='senha', esquema='test'):
        self.cnx = mysql.connector.connect(host=servidor,
                                           user=usr,
                                           password=pwd,
                                           database=esquema)

    def __del__(self):
        self.cnx.close()

    def insert(self, comando, params=()):
        cs = self.cnx.cursor()
        cs.execute(comando, params)
        self.cnx.commit()
        idt = cs.lastrowid #retorna o numero de registro do objeto inserido
        cs.close() #libera o recurso *
        return idt

    def upd_del(self, comando, params=()): #Realiza o Update e Delete | retorna número de linhas afetadas
        cs = self.cnx.cursor()
        cs.execute(comando, params)
        self.cnx.commit()
        num = cs.rowcount
        cs.close()
        return num

    def get_cursor(self, comando, params=()):
        cs = self.cnx.cursor()
        cs.execute(comando, params)
        return cs

    def get_int(self, comando, params=()):
        cs = self.cnx.cursor()
        cs.execute(comando, params)
        ret = int(cs.fetchone()[0])
        cs.close()
        return ret

    def get_float(self, comando, params=()):
        cs = self.cnx.cursor()
        cs.execute(comando, params)
        ret = float(cs.fetchone()[0])
        cs.close()
        return ret

    def get_date(self, comando, params=()):
        cs = self.cnx.cursor()
        cs.execute(comando, params)
        data = cs.fetchone()[0]
        ret = str(data.day).zfill(2) + "/" + str(data.month).zfill(2) + "/" + str(data.year)
        cs.close()
        return ret

    def get_time(self, comando, params=()):
        cs = self.cnx.cursor()
        cs.execute(comando, params)
        hora = cs.fetchone()[0]
        total = hora.total_seconds()
        hour = int(total // 3600)
        minutes = int((total % 3600) // 60)
        seconds = int(total % 60)
        ret = f"{hour:02}:{minutes:02}:{seconds:02}"
        cs.close()
        return ret

    def get_string(self, comando, params=()):
        cs = self.cnx.cursor()
        cs.execute(comando, params)
        ret = str(cs.fetchone()[0])
        cs.close()
        return ret

    def get_object(self, comando, params=()):
        cs = self.cnx.cursor()
        cs.execute(comando, params)
        dados = cs.fetchone()
        if dados is None:
            dic = None
        else:
            md = cs.description #nome dos campos
            dic = {col[0]: valor for col, valor in zip(md, dados)} #zip: combina os dados (nome dos campos com dos dados) -
        cs.close()
        return dic

    def get_list(self, comando, params=()):
        cs = self.cnx.cursor()
        cs.execute(comando, params)
        md = cs.description
        catalog = []
        for reg in cs:
            dic = {col[0]: valor for col, valor in zip(md, reg)}
            catalog.append(dic)
        cs.close()
        return catalog