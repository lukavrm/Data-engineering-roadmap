import pandas as pd

dados = {
    "Nome": [
        "Ana Silva","Bruno Santos","Carla Oliveira","Diego Souza","Eduarda Lima",
        "Felipe Costa","Gabriela Alves","Henrique Pereira","Isabela Rocha",
        "João Martins","Karen Rodrigues","Lucas Fernandes","Mariana Gomes",
        "Nicolas Ribeiro","Olivia Carvalho","Pedro Mendes","Rafaela Barbosa",
        "Samuel Teixeira","Tatiane Moreira","Vinicius Cardoso","Amanda Nunes",
        "Beatriz Freitas","Caio Monteiro","Daniela Correia","Eduardo Castro",
        "Fernanda Vieira","Gustavo Ramos","Helena Moraes","Igor Batista",
        "Juliana Pinto","Leonardo Neves","Manuela Reis","Nathan Farias",
        "Patricia Duarte","Ricardo Melo","Sabrina Araújo","Thiago Lopes",
        "Vanessa Tavares","Wagner Moura","Yasmin Correia","Alexandre Martins",
        "Bianca Andrade","César Fonseca","Débora Macedo","Enzo Sales",
        "Flávia Borges","Gabriel Siqueira","Heloísa Martins","Joana Pires",
        "Marcos Viana"
    ],
    "Idade": [
        24,31,28,35,22,40,27,33,29,45,26,30,34,21,38,25,32,42,23,36,27,41,19,37,
        44,26,39,28,31,24,43,20,29,35,47,33,22,30,48,25,36,23,40,32,18,46,27,34,
        29,51
    ],
    "Estado": [
        "São Paulo","Minas Gerais","Rio de Janeiro","Paraná","Bahia","Pernambuco",
        "Ceará","Goiás","Santa Catarina","Rio Grande do Sul","Espírito Santo","Pará",
        "Amazonas","Mato Grosso","Mato Grosso do Sul","Paraíba","Rio Grande do Norte",
        "Alagoas","Sergipe","Maranhão","Piauí","Tocantins","Rondônia","Acre","Amapá",
        "Roraima","São Paulo","Minas Gerais","Rio de Janeiro","Paraná","Bahia",
        "Pernambuco","Ceará","Goiás","Santa Catarina","Rio Grande do Sul",
        "Espírito Santo","Pará","Amazonas","Mato Grosso","Mato Grosso do Sul",
        "Paraíba","Rio Grande do Norte","Alagoas","Sergipe","Maranhão","Piauí",
        "Tocantins","Rondônia","Acre"
    ]
}

df = pd.DataFrame(dados)

# Cria o arquivo Excel REAL
df.to_excel("pessoas_50.xlsx", index=False)

print("Arquivo Excel criado com sucesso!")
