lista_usuarios = [
  {
    "nome": "nfGVelWlILJEOjT",
    "idade": 32
  },
  {
    "nome": "uDRPRSHVoJokVwuR",
    "idade": 30
  },
  {
    "nome": "TnEMEWFhNFUbFVhvy",
    "idade": 43
  },
  {
    "nome": "ZwRzZeYRam",
    "idade": 26
  },
  {
    "nome": "mDOsqRmysEYmhQsVXg",
    "idade": 23
  },
  {
    "nome": "iqHMYKzJHgkVAnDkbHc",
    "idade": 35
  },
  {
    "nome": "RFyKuOeMIkLHb",
    "idade": 33
  },
  {
    "nome": "FZksBLrFBEpNCsEmB",
    "idade": 28
  },
  {
    "nome": "VHMWWJyZyLMKBYphvJq",
    "idade": 44
  },
  {
    "nome": "HCkcPvCjkJCPcmsCIlKH",
    "idade": 39
  },
  {
    "nome": "EPXKAHzEdVqUQsxUHea",
    "idade": 40
  },
  {
    "nome": "yOxoMtlSZlsGuU",
    "idade": 46
  },
  {
    "nome": "akfoJPtDbgqjfJ",
    "idade": 42
  },
  {
    "nome": "ADPTSubBPwYloFggX",
    "idade": 39
  },
  {
    "nome": "YBpEOkmiHwJQUgsJpsQN",
    "idade": 21
  },
  {
    "nome": "CdeRWIMIKtzxuoHuCSG",
    "idade": 25
  },
  {
    "nome": "TVvOiIkYXMATz",
    "idade": 48
  },
  {
    "nome": "uhyWGBPyiBRyLjYdcuk",
    "idade": 31
  },
  {
    "nome": "xdnsnLMhdVrYxYq",
    "idade": 24
  },
  {
    "nome": "KmUimTYUUUqJHTi",
    "idade": 32
  }
  ]

  #Imprimir o nome e a idade dos usuários com mais de 30 anos

for n in lista_usuarios:
    if (n['idade']) > 30: 
      print(n['nome'], n['idade'])
    else:
      print('Usuario {} menor que 30 anos !'.format(n['nome']))
