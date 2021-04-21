from basetodo.dbconfig import *


def load_session():
    session_maker = sessionmaker()
    session_maker.configure(bind=engine)
    session = session_maker()
    return session


def cadastrar_categoria(cat):
    s = load_session()
    categoria = Categoria(nome=cat)
    s.add(categoria)
    s.commit()
    s.close()

def deletar_categoria(id):
    s = load_session()
    categoria = s.query(Categoria).filter_by(id=id).all()
    s.delete(categoria)
    s.commit()
    s.close()

def listar_categorias():
    s = load_session()
    categorias = s.query(Categoria).all()
    for i in categorias:
        print (i)

def cadastrar_atividade(descricao,cat):
    s = load_session()
    atividade = Atividade(nome=descricao,status=False,categoria=cat)
    s.add(atividade)
    s.commit()
    s.close()

def deletar_atividade(id):
    s = load_session()
    atividadde = s.query(Atividade).filter_by(id=id).all()
    s.delete(atividade)
    s.commit()
    s.close()

def listar_atividades():
    s = load_session()
    atividade = s.query(Atividade).all()
    for i in atividade:
        print (i)

def buscar_atividades_categoria():
    print (f'De qual categoria deseja saber as atividades?')
    listar_categorias()
    print (f'Digite o Código da Atividade')
    s = load_session()
    categoria_id =  int(input())
    atividades = s.query(Atividade).filter_by(categoria=categoria_id).all()
    for atividade in atividades:
        print (atividade)
    print (f'Deseja buscar o código de mais alguma atividade?(S ou N)')
    fluxo = input()
    if fluxo=="s":
        programa=True
    else:
        programa=False
    return programa



#Command line functions

def fluxo_busca_atividades():
    while buscar_atividades_categoria():
        pass



#excel exports from database
