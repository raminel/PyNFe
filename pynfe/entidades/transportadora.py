# -*- coding: utf-8 -*-
from base import Entidade
from pynfe.utils.flags import TIPOS_DOCUMENTO

class Transportadora(Entidade):

    # Dados da Transportadora
    # - Nome/Razão Social (obrigatorio)
    razao_social = str()

    # - Tipo de Documento (obrigatorio) - default CNPJ
    tipo_documento = 'CNPJ'

    # - Numero do Documento (obrigatorio)
    numero_documento = str()

    # - Inscricao Estadual
    inscricao_estadual = str()

    # Endereco
    # - Logradouro (obrigatorio)
    endereco_logradouro = str()

    # - UF (obrigatorio)
    endereco_uf = str()

    # - Municipio (obrigatorio)
    endereco_municipio = str()

