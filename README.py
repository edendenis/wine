#!/usr/bin/env python
# coding: utf-8

# # Como instalar/configurar o WineHQ no Linux Ubuntu
# 
# ## Resumo
# 
# Neste documento estão contidos os principais comandos e configurações para instalar/configurar o WineHQ no Linux Ubuntu.
# 
# ## _Abstract_
# 
# _This document contains the main commands and settings for installing/configuring WineHQ on Linux Ubuntu._

# ## Revisão(ões)/Versão(ões)

# |Revisão número|Data da revisão|Descrição da revisão|Autor da revisão|
# |:-:|:-:|:-|:-|
# |0|21/10/2023|<ul><li>Revisão inicial/criação do documento.</li></ul>|Eden Denis F. da S. L. Santos|

# ## 1. Instalar o WineHQ no Linux Ubuntu [1]
# 
# Para instalar o WineHQ no Linux Ubuntu, você pode seguir estas etapas:
# 
# 1. Abra o terminal. Você pode fazer isso pressionando: `Ctrl + Alt + T`
# 
# 2. Certifique-se de que seu sistema esteja atualizado.
# 
# 2.1 Buscar as atualizações disponíveis para os pacotes que estão instalados em seu sistema. Digite o seguinte comando e pressione `Enter`: `sudo apt update -y`
# 
# 2.2 Realmente atualizar os pacotes instalados para as suas versões mais recentes, com base na última vez que você executou `sudo apt update`. Digite o seguinte comando e pressione `Enter`: `sudo apt upgrade -y`
# 
# 3. **Preparação:** Se o seu sistema é 64 bit, habilite a arquitetura 32 (se você não já tiver): `sudo dpkg --add-architecture i386` 
# 
# 4. **Adicionar o repositório:** baixar e adicionar a chave do repositório:
# 
# ```
# sudo mkdir -pm755 /etc/apt/keyrings
# sudo wget -O /etc/apt/keyrings/winehq-archive.key https://dl.winehq.org/wine-builds/winehq.key
# ```

# ## 1.1 Código completo
# 
# Para instalar o Whatsap no Linux Ubuntu sem precisar digitar linha por linha, você pode seguir estas etapas:
# 
# 1. Abra o terminal. Você pode fazer isso pressionando: `Ctrl + Alt + T`
# 
# 2. Digite o seguinte comando e pressione `Enter`:
# 
# ```
# sudo apt update -y
# sudo apt upgrade -y
# sudo dpkg --add-architecture i386
# sudo mkdir -pm755 /etc/apt/keyrings
# sudo wget -O /etc/apt/keyrings/winehq-archive.key https://dl.winehq.org/wine-builds/winehq.key
# ```

# ## Referências
# 
# [1] OPENAI. ***Ubuntu winehq repository:*** https://wiki.winehq.org/Ubuntu (texto adaptado). Acessado em: 21/10/2023 00:09.
