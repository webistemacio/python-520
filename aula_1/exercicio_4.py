lista_de_usuarios = [
  {
    "nome": "qMHHOwoAaYECgB",
    "idade": 49,
    "email": "yMEpqGsegWXw@4linux.com",
    "sexo": "?",
    "endereco": "Rua NIbCtFYJpZtRJg"
  },
  {
    "nome": "GJBxVjGYtVEqmRasx",
    "idade": 23,
    "email": "mBZWAcaUDCVioOQEdIu@4linux.com",
    "sexo": "?",
    "endereco": "Rua VFJGPBuNRnz"
  },
  {
    "nome": "TFeiNzjMuAfyYHksx",
    "idade": 39,
    "email": "BEjDyrdxPJoniHIDFgZ@4linux.com",
    "sexo": "?",
    "endereco": "Rua AEhMBiFAuGgSAiuIyx"
  },
  {
    "nome": "EguHnoFTrUAuUUoery",
    "idade": 37,
    "email": "QzqgJRboorIzKjKp@4linux.com",
    "sexo": "?",
    "endereco": "Rua LgktJSYDjo"
  },
  {
    "nome": "zDjQIfYyTwtzetXMJvDs",
    "idade": 25,
    "email": "CZBArUyyMa@4linux.com",
    "sexo": "F",
    "endereco": "Rua DEPwqBeLgyylX"
  },
  {
    "nome": "FDLtOesbqzdqzGe",
    "idade": 47,
    "email": "MakWfrgesmuBb@4linux.com",
    "sexo": "F",
    "endereco": "Rua qVLKGbVYOPRNTdrRYA"
  },
  {
    "nome": "xrffFndgNldHhb",
    "idade": 20,
    "email": "MUvdkHayaYULCTkSDH@4linux.com",
    "sexo": "F",
    "endereco": "Rua ZwkeJCYdeZgEcX"
  },
  {
    "nome": "RyfOocoNhyuEDSN",
    "idade": 50,
    "email": "ggQNSQvIOmDqZj@4linux.com",
    "sexo": "M",
    "endereco": "Rua kvvnDojQEMsHMXzc"
  },
  {
    "nome": "GAXCbICkOjzNZxU",
    "idade": 31,
    "email": "ClNJyJMhNfmTvyQxxYvQ@4linux.com",
    "sexo": "?",
    "endereco": "Rua yIParNvhlayIcGup"
  },
  {
    "nome": "wvaTNhfqPOlnt",
    "idade": 29,
    "email": "EwTJHbRTCrfYF@4linux.com",
    "sexo": "F",
    "endereco": "Rua bGCVdBFXSzcVBeLvKYUZ"
  },
  {
    "nome": "qhDBAYlbwaSMar",
    "idade": 27,
    "email": "AwDWEkwtZcGgaHlsaW@4linux.com",
    "sexo": "M",
    "endereco": "Rua hVYSkEHTmaBIJG"
  },
  {
    "nome": "fAZzfzvEySnSei",
    "idade": 44,
    "email": "wrzgKwORTAnliywEq@4linux.com",
    "sexo": "M",
    "endereco": "Rua cSdMqmMvebnTd"
  },
  {
    "nome": "HJBLhUuMHeAogrtbeq",
    "idade": 47,
    "email": "akKkICosKJbUdVcLTCnQ@4linux.com",
    "sexo": "F",
    "endereco": "Rua IhyoOwKTUCQlBvDuVVYS"
  },
  {
    "nome": "vEeSluRuOmIJTFrgNA",
    "idade": 35,
    "email": "wrCGKAsQRlWLKUSH@4linux.com",
    "sexo": "?",
    "endereco": "Rua ZRfcRxPsJPO"
  },
  {
    "nome": "OyehQbxCsnSGPBLcviBs",
    "idade": 23,
    "email": "fnndYbeFLPmhB@4linux.com",
    "sexo": "?",
    "endereco": "Rua cnquXCCUji"
  },
  {
    "nome": "JDZdCgzulyGWW",
    "idade": 30,
    "email": "brPbOrQBWfIBikDA@4linux.com",
    "sexo": "M",
    "endereco": "Rua HgtuwqKeMin"
  },
  {
    "nome": "MoinSGxEySEgrb",
    "idade": 36,
    "email": "qolygpBXCKEeur@4linux.com",
    "sexo": "?",
    "endereco": "Rua xoVGMdTrFKHboQRzFd"
  },
  {
    "nome": "XStrcVVPyieJJznYZ",
    "idade": 49,
    "email": "doKMuRYdKwolzgkq@4linux.com",
    "sexo": "M",
    "endereco": "Rua jeTpYoJAHnSeWAUWG"
  },
  {
    "nome": "uWVZbFSfdE",
    "idade": 30,
    "email": "WpRAukMAAygh@4linux.com",
    "sexo": "?",
    "endereco": "Rua QQvsljaHXnhqjHlg"
  },
  {
    "nome": "jgVjBVFVVKui",
    "idade": 43,
    "email": "SCUVGmVBRpREfAMIleo@4linux.com",
    "sexo": "?",
    "endereco": "Rua ioMdZJPBgdMUzWsDg"
  }
]
#Testar e imprimir somente os e-mails que contiverem "l" ou "j".

lista_final = []
for n in lista_de_usuarios:
    if 'l' in n['email'].lower() or 'j' in n['email'].lower():
      if n['idade'] > 25:
        lista_final.append(n)

print(lista_final)
