import re

def validacao(form):

    cadastro_concluído = {'message': 'Usuario Cadastrado'}

    errors = {'message': 'Erro no Cadastro do Usuario',
              'errors':
              {}}
    
    try:
        validacao_nome(form)
    except ValueError as e:
        errors['errors']['Nome'] = str(e)

    try:
        validacao_cnpj(form)
    except ValueError as e:
        errors['errors']['CNPJ'] = str(e)
    try:
        validacao_email(form)
    except ValueError as e:
        errors['errors']['Email'] = str(e)

    try:
        validacao_senha(form)
    except ValueError as e:
        errors['errors']['Senha'] = str(e)

    if errors['errors']:
        return errors
    else:
        return cadastro_concluído



def validacao_nome(form):
    if "Nome" not in form:
        raise ValueError("Campo não informado.")

    if form['Nome'] is None:
        raise ValueError("Campo está vazio.")

    if not isinstance(form['Nome'], str):
        raise ValueError("Campo deve ser uma String")
    
    if len(form['Nome']) > 255:
        raise ValueError("Campo deve ter no máximo 255 caracteres.")
    
    else:
        return True
    
def validacao_cnpj(form):
    if "CNPJ" not in form:
        raise ValueError("Campo não informado.")
    
    if form['CNPJ'] is None:
        raise ValueError("Campo está vazio.")

    if not isinstance(form['CNPJ'], str):
        raise ValueError("Campo deve ser uma String")
    
    if len(form['CNPJ']) != 14:
        raise ValueError("Campo deve ter 14 Caracteres")
    
    else:
        return True

def validacao_email(form):
    if "Email" not in form:
        raise ValueError("Campo não informado.")
    
    if form['Email'] is None:
        raise ValueError("Campo está vazio.")

    if not isinstance(form['Email'], str):
        raise ValueError("Campo deve ser uma String")
    
    if len(form['Email']) > 255:
        raise ValueError("Campo deve ter no máximo 255 caracteres")
    
    valid_email = r"@([a-zA-Z0-9.-]+\.[a-zA-Z]{2,})$"

    if re.search(valid_email, form['Email']) is None:
        raise ValueError("Campo inválido")
    
    else:
        return True
    
def validacao_senha(form):
    if "Senha" not in form:
        raise ValueError("Campo não informado.")
    
    if form['Senha'] is None:
        raise ValueError("Campo está vazio.")

    if not isinstance(form['Senha'], str):
        raise ValueError("Campo deve ser uma String")
    
    valid_senha = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*[^a-zA-Z0-9]).+$'
    
    if len(form['Senha']) < 8 and re.search(valid_senha, form['Senha']) is None :
        raise ValueError("Campo deve ter no mínimo 8 caracteres com maiusculas, minusculas e um caractere especial")

def validacao_celular(form):
    if "Celular" not in form:
        raise ValueError("Campo não informado.")
    
    if form['Celular'] is None:
        raise ValueError("Campo está vazio.")

    if not isinstance(form['Celular'], str):
        raise ValueError("Campo deve ser uma String")
    
    valid_num = r"^\+\d{1,3}\d{2}\d{8,9}$"

    if re.search(valid_num, form['Celular']) is None:
        raise ValueError("Número inválido. Use o formato: +DDIDDDNÚMERO (ex: +5511912345678)")
    

    
    

    

