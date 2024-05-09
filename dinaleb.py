def read_dna_seq(name_file):
  diccionario_dna = {}
  #Abre archiuvo:
  dna_file =  open(name_file, 'r')
  #Lee TODO el archivo en una sola linea de texto
  # readline, lee línea por línea
  # readlines, regresa una lista de cadenas con todo el archivo.
  data = dna_file.readlines()
  diccionario_dna["descriptor"] = data[0]
  sequencia = ""
  for i in range(1, len(data)):
    sequencia = sequencia + data[i].replace('\n', '')
    #data[i][0:len(data[i])-1]
  diccionario_dna["secuencia"] = sequencia
  #Cierra el archivo
  dna_file.close()
  return diccionario_dna

def secuencia_complementaria(diccionario):
  secuencia = diccionario["secuencia"]
  complementaria = ""
  for nucleotido in secuencia:
    if nucleotido == 'A':
      complementaria += 'T'
    elif nucleotido == 'T':
      complementaria += 'A'
    elif nucleotido == 'C':
      complementaria += 'G'
    elif nucleotido == 'G':
      complementaria += 'C'
  diccionario["complementaria"] = complementaria
  return diccionario


def dna2rna(dicccionario):
  dicccionario["rna"] = dicccionario["secuencia"].replace('T', 'U')
  return dicccionario


def cuentaRNA( diccionario ):
  tripletes = ["UUU", "UUA", "UAA"]
  aux = {}
  total = 0
  for triplet in tripletes:
    contador = 0
    for repeticiones in range(0, len(diccionario["rna"]), 3):
      if triplet == diccionario["rna"][repeticiones:repeticiones+3]:
        contador += 1
    aux[triplet] = contador
    total = total + contador
  for triplet in tripletes:
    aux[triplet] = (aux[triplet] * 100 / total) 
  print(aux)


def rna2protein(dicccionario):
  seq_proteins = ""
  rna = dicccionario["rna"]
  dic_proteinas = {"UUU":"F", "UUA":"L"}
  for i in range(0, len(rna), 3):
    codon = rna[i:i+ 3]
    if codon in dic_proteinas:
      seq_proteins +=dic_proteinas[codon]
  dicccionario["proteinas"] = seq_proteins

  return dicccionario



def menu():
  print("Bienvenido a VIRUS 1.0")
  opcion = -1
  while opcion != 11:
    print("1.Carga la secuencia de DNA (pide nombre del archivo fasta a cargar)")
    print("2.Genera la secuencia complementaria")
    print("3.Convierte de DNA a RNA")
    print("4.Convierte de RNA a DNA")
    print("5.Busca en DNA")
    print("6.Busca en RNA")
    print("7.Busca en Proteínas")
    print("8.Porcentajes de nucleótidos")
    print("9.RNA a Matriz")
    print("10.Investigación")
    print("11.Salir")
    opcion = int(input("Dame opcion: "))
    if opcion < 1 or opcion > 11:
      print("ERROR, checa las opciones")
    elif opcion == 11:
      print("Bye")
    elif opcion == 1:
      archivo = input("Dame archivo: ")
      dna_diccionario = read_dna_seq(archivo)
      print(dna_diccionario["descriptor"])
      print(dna_diccionario["secuencia"][0:100])
    elif opcion == 2:
      secuencia_complementaria(dna_diccionario)
      print(dna_diccionario["descriptor"])
      print(dna_diccionario["secuencia"][0:100])
      print(dna_diccionario["complementaria"][0:100])
    elif opcion == 3:
      secuencia_complementaria(dna_diccionario)
      dna2rna (dna_diccionario)
      print(dna_diccionario["descriptor"])
      print(dna_diccionario["rna"][0:100])

    elif opcion == 8:
      cuentaRNA(dna_diccionario)







