# Synapse Health - Portal Integrado (Oracle + Módulo Balance)

Este repositório contém o protótipo de alta fidelidade e interativo do **Synapse Health Portal**, desenvolvido como parte de um projeto acadêmico de Ciência de Dados. A aplicação simula um sistema de governança hospitalar e alocação inteligente de escalas médicas/enfermagem, utilizando conceitos de otimização de leitos, análise de fadiga operacional e consultas em linguagem natural (*Natural Language to SQL*).

O objetivo principal desta interface é tangibilizar o modelo conceitual da solução, integrando frentes de monitoramento de fluxo assistencial e inteligência preditiva.

---

## 🚀 Funcionalidades Demonstradas no Protótipo

* **Camada 1: Monitoramento & Jornada Ativa:** Acompanhamento do pipeline do paciente (Triagem, Atendimento, Alocação de Leitos, Alta) e detecção automática de gargalos operacionais.
* **Camada 2: Análise Sazonal & Oracle Select AI:** Simulação de flutuação de internações do SUS por estações climáticas (Verão, Outono, Inverno) com foco geográfico nos Departamentos Regionais de Saúde (DRS) de SP. Inclui uma engine demonstrativa de processamento de linguagem natural para SQL (*NL-to-SQL*).
* **Camada 3: Alocação Módulo Balance:** Matriz analítica de fadiga para profissionais de saúde, permitindo aprovar escalas sugeridas pelo algoritmo ou justificar desvios operacionais.
* **Privacy by Design (LGPD):** Demonstração prática de governança segura, monitorando apenas capacidades físicas e dados operacionais (Protocolo Manchester), mitigando a exposição de dados sensíveis de prontuários.

---

## 🛠️ Como Executar o Projeto Localmente

O projeto foi encapsulado utilizando **Python** e o micro-framework **Flask** para facilitar a execução local por qualquer usuário.

### Pré-requisitos
Certifique-se de ter o **Python 3.x** instalado em sua máquina.

### Passos para execução

1. **Clone este repositório:**
   ```bash
   git clone [https://github.com/seu-usuario/synapse-health-portal.git](https://github.com/seu-usuario/synapse-health-portal.git)
   cd synapse-health-portal
   ```

2. **Instale o Flask**
O projeto utiliza apenas o Flask como dependência de backend (o design e os ícones são carregados via CDN do Tailwind CSS e FontAwesome).
   ```bash
   pip install flask
   ```

3. **Inicie o servidor:**
Execute o script Python principal:
   ```bash
   python app.py
   ```

4. **Acesse no navegador:**
Abra o seu navegador e acesse o endereço local gerado pelo Flask:
   [http://127.0.0.1:5000](http://127.0.0.1:5000)

---

## 🧠 Estrutura de Arquivos

```text
synapse-health-portal/
├── app.py             # Código do servidor Flask (Backend)
├── README.md          # Documentação do projeto
└── templates/         # Pasta contendo a camada de visualização (Frontend)
    └── prot_integrado_synapse_health.html
```

## ⚖️ Conformidade e Privacidade
Em total alinhamento com a Lei Geral de Proteção de Dados (LGPD), este ecossistema prioriza a segurança estrutural de dados de saúde, limitando o escopo analítico a metadados de leitos físicos e fluxos operacionais, sem armazenamento ou manipulação de histórico clínico individual

