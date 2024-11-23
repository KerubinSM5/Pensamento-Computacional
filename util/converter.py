import datetime


def mysql_to_bra(data_mysql):
    """Converte uma data no formato MySQL para dd/mm/aaaa.
    Args:
      data_mysql: String representando a data no formato MySQL (YYYY-MM-DD).
    Returns:
      String com a data no formato dd/mm/aaaa.
    """
    if data_mysql == None:
        return ""
    else:
        data_mysql = str(data_mysql)
        return data_mysql[8:10] + "/" + data_mysql[5:7] + "/" + data_mysql[0:4]


def bra_to_mysql(data_bra):
    """Converte uma data no formato brasileiro (dd/mm/aaaa) para o formato MySQL (YYYY-MM-DD).
    Args:
      data_bra: String representando a data no formato brasileiro (dd/mm/aaaa).
    Returns:
      String com a data no formato MySQL (YYYY-MM-DD).
    """

    # Primeiro, convertemos a string para um objeto datetime
    dt_mysql = data_bra[6:10] + "-" + data_bra[3:5] + "-" + data_bra[0:2]

    # Em seguida, formatamos o objeto datetime para o formato MySQL
    return dt_mysql
