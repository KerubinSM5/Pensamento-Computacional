# Função de validação para números reais
def validate_float(new_text):
    if not new_text:  # Permite campo vazio
        return True
    try:
        float(new_text)
        return True
    except ValueError:
        return False

def limitar_tamanho(widget, maximo):
    """
    Limita o número máximo de caracteres em um widget Tkinter.

    Args:
        widget: O widget Tkinter a ser limitado (e.g., Entry, Text).
        maximo: O número máximo de caracteres permitidos.
    """

    def validate(new_text):
        return len(new_text) <= maximo

    vcmd = (widget.register(validate), '%P')
    widget.configure(validate='key', validatecommand=vcmd)

def todos_campos_preenchidos(widgets):
    """
    Verifica se todos os widgets de entrada de dados em uma lista estão preenchidos.

    Args:
        widgets: Uma lista de widgets Tkinter (e.g., Entry, Text).

    Returns:
        True se todos os widgets estiverem preenchidos, False caso contrário.
    """
    valido = True
    msg = ""
    for widget in widgets:
        if not widget[0].get():
            msg += widget[1] + "\n"
            valido = False
    return [valido, msg]