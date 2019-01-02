# -*- coding: utf-8 -*-
"""
Spyder Editor

Este é um arquivo de script temporário.
"""
import csv

DELIMITER = ','

def corrige(linha):
    trocas = [['Ã‹', 'E'], ['Ã’', 'O']]
    out = []
    temp = linha.split(DELIMITER)
    for palavra in temp:
        for troca in trocas:
            palavra = palavra.replace(troca[0], troca[1])
        out.append(palavra)
    return out


def file_writer(table):
    with open('trocas.csv', mode='w') as final_file:
        for line in table:
            final_file.write(DELIMITER.join(line))
       

def main():
    with open('bi_datasets_public_web_to_fipe.csv') as csv_file:
        all_lines = csv_file.readlines()
    table = []
    for line in all_lines:
        temp = corrige(line)
        table.append(temp)
    return table



file_writer(main())