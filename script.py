# Criar estrutura organizada dos arquivos para o projeto GitHub
import os

# Criar diretório principal
os.makedirs('planilha-corrida-7km', exist_ok=True)

# Estrutura de arquivos do projeto
arquivos_projeto = {
    'README.md': """# 🏃‍♂️ Planilha Profissional de Corrida 7km

Sistema web completo para acompanhamento de treinos de corrida com objetivo de completar 7km em pace 4:40/km em 6 semanas.

## 📋 Sobre o Projeto

Aplicação desenvolvida para **Mauro** (47 anos) e **Franciane** (35 anos) com as seguintes funcionalidades:

- ✅ **Plano de 6 semanas** estruturado (07/10 a 16/11/2025)
- ✅ **Dashboard personalizado** por atleta com KPIs em tempo real
- ✅ **Registro de treinos** com cálculos automáticos
- ✅ **Simulados e testes** (3km, 5km, 7km) com recalibração de zonas
- ✅ **Monitoramento de carga** (sRPE Load, monotonia, strain)
- ✅ **Acompanhamento corporal** semanal
- ✅ **Alertas de segurança** automáticos

## 🎯 Meta do Programa

**Objetivo:** Completar 7km em pace 4:40/km (32:40 total)  
**Baseline:** 5km em 30:00 (pace 6:00/km)  
**Prazo:** 6 semanas (meta ambiciosa)  
**Frequência:** 3x/semana (Terça, Quarta, Domingo)  

## 🚀 Como Usar

1. **Acesse a aplicação:** [Link do GitHub Pages]
2. **Selecione o atleta** (Mauro ou Franciane)
3. **Explore o dashboard** com métricas atuais
4. **Registre treinos** após cada sessão
5. **Acompanhe evolução** nos gráficos e KPIs

## 📱 Tecnologias

- **HTML5** - Estrutura da aplicação
- **CSS3** - Design responsivo e moderno  
- **JavaScript** - Lógica e interatividade
- **LocalStorage** - Armazenamento de dados local
- **GitHub Pages** - Hospedagem gratuita

## 🔧 Funcionalidades Técnicas

- **Cálculos automáticos:** Pace médio, sRPE Load, progressão de carga
- **Validações inteligentes:** Alertas para RPE alto, carga excessiva
- **Interface responsiva:** Funciona em desktop, tablet e celular
- **Dados persistentes:** Informações salvas localmente no navegador

## 📊 Estrutura do Plano

### Semanas 1-2: Base + Introdução Limiar
- Tempo introdutório e contínuo
- **Teste 3km** (15/10/2025)

### Semanas 3-4: VO2 + Especificidade  
- Intervalados curtos e médios
- **Simulado 5km** (28/10/2025)

### Semanas 5-6: Pico + Taper
- Trabalho específico pace alvo
- **Simulado 7km OBJETIVO** (12/11/2025)

## ⚠️ Considerações Importantes

Esta é uma **meta muito ambiciosa** (melhoria de ~22% em 6 semanas). O sistema inclui:

- Monitoramento rigoroso de carga
- Alertas de segurança automáticos  
- Flexibilidade para ajustes baseados nos simulados
- Foco na prevenção de lesões

## 📧 Suporte

Para dúvidas ou melhorias, abra uma issue neste repositório.

---

*Desenvolvido com foco em segurança, performance e usabilidade.*""",
    
    'GUIA_PUBLICACAO.md': """# 📖 Guia de Publicação no GitHub Pages

## Passo a Passo Completo

### 1️⃣ Preparar Arquivos
- Baixe todos os arquivos deste repositório
- Mantenha a estrutura de pastas intacta

### 2️⃣ Criar Repositório no GitHub
1. Acesse [github.com](https://github.com) e faça login
2. Clique em **"New repository"** (botão verde)
3. Nome sugerido: `planilha-corrida-7km`
4. Marque **"Public"** (obrigatório para GitHub Pages gratuito)
5. Marque **"Add a README file"**
6. Clique **"Create repository"**

### 3️⃣ Upload dos Arquivos
1. No repositório criado, clique **"uploading an existing file"**
2. Arraste **TODOS** os arquivos para a área:
   - `index.html`
   - `style.css` 
   - `app.js`
   - `README.md`
   - `GUIA_PUBLICACAO.md`
3. Na caixa de commit, escreva: `Adicionar aplicação de treino de corrida`
4. Clique **"Commit changes"**

### 4️⃣ Ativar GitHub Pages
1. No repositório, vá na aba **"Settings"**
2. Role até a seção **"Pages"** (menu lateral esquerdo)
3. Em **"Source"**, selecione **"Deploy from a branch"**
4. Em **"Branch"**, selecione **"main"**
5. Deixe **"/ (root)"** selecionado
6. Clique **"Save"**

### 5️⃣ Acessar o Site
1. Aguarde 2-3 minutos para processamento
2. Acesse: `https://SEU-USUARIO.github.io/planilha-corrida-7km`
3. 🎉 **Site online e funcionando!**

## 🔄 Atualizações Futuras

Para atualizar o site:
1. Faça upload de novos arquivos no repositório
2. As mudanças ficam online automaticamente
3. Sem necessidade de reativar GitHub Pages

## 💡 Dicas Importantes

- ✅ Mantenha o repositório **público** para GitHub Pages gratuito
- ✅ O arquivo `index.html` deve estar na raiz do repositório  
- ✅ Aguarde alguns minutos após mudanças para ver atualizações
- ✅ Use sempre HTTPS na URL final para segurança

## 🆘 Solução de Problemas

**Site não carrega?**
- Verifique se GitHub Pages está ativado nas configurações
- Confirme que `index.html` está na raiz do repositório
- Aguarde até 10 minutos para propagação

**Mudanças não aparecem?**
- Force refresh: Ctrl+F5 (Windows) ou Cmd+Shift+R (Mac)
- Limpe cache do navegador
- Aguarde alguns minutos para propagação

---

*Qualquer dúvida, consulte a [documentação oficial do GitHub Pages](https://pages.github.com/)*"""
}

# Criar os arquivos organizados
for arquivo, conteudo in arquivos_projeto.items():
    caminho = f'planilha-corrida-7km/{arquivo}'
    with open(caminho, 'w', encoding='utf-8') as f:
        f.write(conteudo)

print("Arquivos de documentação criados:")
for arquivo in arquivos_projeto.keys():
    print(f"✅ {arquivo}")

print(f"\nEstrutura do projeto criada na pasta: planilha-corrida-7km/")
print("Próximos passos: Baixar os arquivos da aplicação (HTML, CSS, JS) e adicionar à pasta.")