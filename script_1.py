# Vou recriar os arquivos principais da aplicação com o código completo

# HTML Principal
html_content = '''<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Planilha Profissional de Corrida 7km - Mauro & Franciane</title>
    <link rel="stylesheet" href="style.css">
    <link rel="icon" type="image/x-icon" href="data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMzIiIGhlaWdodD0iMzIiIHZpZXdCb3g9IjAgMCAzMiAzMiIgZmlsbD0ibm9uZSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KPHBhdGggZD0iTTE2IDJDOC4yIDIgMiA4LjIgMiAxNlM4LjIgMzAgMTYgMzAgMzAgMjMuOCAzMCAxNiAyMy44IDIgMTYgMloiIGZpbGw9IiM0NDcyQzQiLz4KPHN2ZyB3aWR0aD0iMTYiIGhlaWdodD0iMTYiIHg9IjgiIHk9IjgiIGZpbGw9IndoaXRlIiBhcmlhLWxhYmVsPSJSdW5uaW5nIGljb24iPgo8cGF0aCBkPSJNMyA4aDEwdjFIM3ptMCAzaDh2MUgzem0wIDNoNnYxSDNaIi8+Cjwvc3ZnPgo8L3N2Zz4K">
</head>
<body>
    <!-- Seleção de Atleta -->
    <div id="athlete-selection" class="athlete-selection">
        <div class="container">
            <header class="app-header">
                <h1>🏃‍♂️ Programa de Treinamento Profissional</h1>
                <p class="subtitle">Meta: <strong>7km em 4:40/km</strong> em 6 semanas</p>
                <p class="period">07/10/2025 → 16/11/2025 • Terça, Quarta, Domingo</p>
            </header>
            
            <div class="athletes-grid">
                <div class="athlete-card" data-athlete="mauro">
                    <div class="athlete-avatar">
                        <div class="avatar-circle">
                            <span>M</span>
                        </div>
                    </div>
                    <h2>Mauro</h2>
                    <div class="athlete-info">
                        <div class="info-row">
                            <span class="label">Idade:</span>
                            <span class="value">47 anos</span>
                        </div>
                        <div class="info-row">
                            <span class="label">Físico:</span>
                            <span class="value">112kg • 1,91m</span>
                        </div>
                        <div class="info-row">
                            <span class="label">FC Máx:</span>
                            <span class="value">173 bpm</span>
                        </div>
                        <div class="info-row">
                            <span class="label">Baseline 5k:</span>
                            <span class="value">30:00 (6:00/km)</span>
                        </div>
                    </div>
                    <div class="progress-info">
                        <div class="progress-bar">
                            <div class="progress-fill" style="width: 15%;"></div>
                        </div>
                        <span class="progress-text">15% até a meta</span>
                    </div>
                    <button class="btn btn--primary">Acessar Dashboard</button>
                </div>
                
                <div class="athlete-card" data-athlete="franciane">
                    <div class="athlete-avatar">
                        <div class="avatar-circle">
                            <span>F</span>
                        </div>
                    </div>
                    <h2>Franciane</h2>
                    <div class="athlete-info">
                        <div class="info-row">
                            <span class="label">Idade:</span>
                            <span class="value">35 anos</span>
                        </div>
                        <div class="info-row">
                            <span class="label">Físico:</span>
                            <span class="value">63kg • 1,65m</span>
                        </div>
                        <div class="info-row">
                            <span class="label">FC Máx:</span>
                            <span class="value">185 bpm</span>
                        </div>
                        <div class="info-row">
                            <span class="label">Baseline 5k:</span>
                            <span class="value">30:00 (6:00/km)</span>
                        </div>
                    </div>
                    <div class="progress-info">
                        <div class="progress-bar">
                            <div class="progress-fill" style="width: 15%;"></div>
                        </div>
                        <span class="progress-text">15% até a meta</span>
                    </div>
                    <button class="btn btn--primary">Acessar Dashboard</button>
                </div>
            </div>
        </div>
    </div>

    <!-- Dashboard Principal -->
    <div id="main-dashboard" class="main-dashboard" style="display: none;">
        <nav class="top-nav">
            <div class="nav-content">
                <button class="back-btn" onclick="showAthleteSelection()">← Voltar</button>
                <div class="current-athlete">
                    <span class="athlete-name"></span>
                    <span class="current-week"></span>
                </div>
                <div class="nav-links">
                    <button class="nav-link active" data-section="dashboard">Dashboard</button>
                    <button class="nav-link" data-section="plan">Plano 6 Semanas</button>
                    <button class="nav-link" data-section="training">Registrar Treino</button>
                    <button class="nav-link" data-section="tests">Simulados</button>
                    <button class="nav-link" data-section="zones">Zonas</button>
                    <button class="nav-link" data-section="body">Medidas</button>
                </div>
            </div>
        </nav>

        <!-- Dashboard Section -->
        <div id="dashboard-section" class="section active">
            <div class="container">
                <div class="dashboard-header">
                    <h2>Dashboard</h2>
                    <div class="last-update">Última atualização: <span id="last-update">--</span></div>
                </div>
                
                <div class="kpi-grid">
                    <div class="kpi-card primary">
                        <div class="kpi-header">
                            <h3>Meta 7km</h3>
                            <div class="kpi-icon">🎯</div>
                        </div>
                        <div class="kpi-value">4:40/km</div>
                        <div class="kpi-subtitle">32:40 total</div>
                        <div class="kpi-progress">
                            <div class="progress-bar">
                                <div class="progress-fill" style="width: 15%;"></div>
                            </div>
                            <span>15% concluído</span>
                        </div>
                    </div>

                    <div class="kpi-card">
                        <div class="kpi-header">
                            <h3>Melhor 5km</h3>
                            <div class="kpi-icon">⏱️</div>
                        </div>
                        <div class="kpi-value" id="best-5k">30:00</div>
                        <div class="kpi-subtitle" id="best-5k-pace">6:00/km</div>
                        <div class="kpi-change">Baseline</div>
                    </div>

                    <div class="kpi-card">
                        <div class="kpi-header">
                            <h3>Cumprimento</h3>
                            <div class="kpi-icon">✅</div>
                        </div>
                        <div class="kpi-value" id="completion-rate">0%</div>
                        <div class="kpi-subtitle">dos treinos</div>
                        <div class="kpi-change" id="completion-count">0 de 18</div>
                    </div>

                    <div class="kpi-card">
                        <div class="kpi-header">
                            <h3>Carga Semanal</h3>
                            <div class="kpi-icon">📊</div>
                        </div>
                        <div class="kpi-value" id="weekly-load">0</div>
                        <div class="kpi-subtitle">sRPE Load</div>
                        <div class="kpi-change" id="load-status">Dentro do limite</div>
                    </div>
                </div>

                <div class="charts-grid">
                    <div class="chart-card">
                        <h3>Evolução de Pace nos Simulados</h3>
                        <div class="chart-placeholder">
                            <div class="chart-empty">
                                📈 Gráfico será atualizado após os simulados
                            </div>
                        </div>
                    </div>

                    <div class="next-training">
                        <h3>Próximo Treino</h3>
                        <div class="training-card" id="next-training">
                            <div class="training-date">Terça, 08/10/2025</div>
                            <div class="training-type">Tempo Introdutório</div>
                            <div class="training-details">
                                12min aquec Z1-Z2 + 3×6min Z3 (2min trote) + 8-10min desaq
                            </div>
                            <div class="training-meta">
                                <span>⏱️ 55min</span>
                                <span>📏 8.5km</span>
                                <span>💪 Z3</span>
                            </div>
                        </div>
                    </div>
                </div>

                <div class="alerts-section">
                    <h3>Alertas e Notificações</h3>
                    <div class="alerts-container" id="alerts-container">
                        <div class="alert info">
                            <div class="alert-icon">ℹ️</div>
                            <div class="alert-content">
                                <strong>Bem-vindo!</strong> Registre seus treinos para começar o acompanhamento.
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>

        <!-- Plan Section -->
        <div id="plan-section" class="section">
            <div class="container">
                <div class="section-header">
                    <h2>Plano 6 Semanas</h2>
                    <div class="plan-period">07/10/2025 → 16/11/2025</div>
                </div>
                
                <div class="plan-grid" id="plan-grid">
                    <!-- Plano será gerado dinamicamente -->
                </div>
            </div>
        </div>

        <!-- Training Section -->
        <div id="training-section" class="section">
            <div class="container">
                <div class="section-header">
                    <h2>Registrar Treino</h2>
                    <div class="form-subtitle">Preencha os dados após completar seu treino</div>
                </div>
                
                <form id="training-form" class="training-form">
                    <div class="form-grid">
                        <div class="form-group">
                            <label for="training-date">Data do Treino</label>
                            <input type="date" id="training-date" required>
                        </div>

                        <div class="form-group">
                            <label for="training-type">Tipo de Treino</label>
                            <select id="training-type" required>
                                <option value="">Selecione o tipo</option>
                                <option value="tempo-limiar">Tempo/Limiar Z3-Z4</option>
                                <option value="tecnica">Técnica/educativos</option>
                                <option value="longao">Longão específico Z2→Z3</option>
                                <option value="vo2">Intervalado VO2 Z4-Z5</option>
                                <option value="rodagem">Rodagem Z2</option>
                                <option value="simulado-3k">Simulado 3km</option>
                                <option value="simulado-5k">Simulado 5km</option>
                                <option value="simulado-7k">Simulado 7km</option>
                                <option value="transicao">Transição leve + mobilidade</option>
                            </select>
                        </div>

                        <div class="form-group">
                            <label for="training-duration">Duração (minutos)</label>
                            <input type="number" id="training-duration" min="1" max="120" required>
                        </div>

                        <div class="form-group">
                            <label for="training-distance">Distância (km)</label>
                            <input type="number" id="training-distance" min="0.1" max="20" step="0.1" required>
                        </div>

                        <div class="form-group">
                            <label for="average-pace">Pace Médio</label>
                            <input type="text" id="average-pace" placeholder="Calculado automaticamente" readonly>
                        </div>

                        <div class="form-group">
                            <label for="rpe-input">RPE (1-10)</label>
                            <div class="rpe-container">
                                <input type="range" id="rpe-slider" min="1" max="10" value="5">
                                <input type="number" id="rpe-input" min="1" max="10" value="5" required>
                                <div class="rpe-labels">
                                    <span>Muito fácil</span>
                                    <span>Máximo</span>
                                </div>
                            </div>
                        </div>

                        <div class="form-group">
                            <label for="avg-hr">FC Média (bpm)</label>
                            <input type="number" id="avg-hr" min="60" max="220">
                        </div>

                        <div class="form-group">
                            <label for="max-hr">FC Máxima (bpm)</label>
                            <input type="number" id="max-hr" min="60" max="220">
                        </div>

                        <div class="form-group">
                            <label for="completed">Cumpriu o Planejado?</label>
                            <select id="completed" required>
                                <option value="">Selecione</option>
                                <option value="sim">Sim</option>
                                <option value="parcial">Parcial</option>
                                <option value="nao">Não</option>
                            </select>
                        </div>

                        <div class="form-group">
                            <label for="pain-level">Dor (0-10)</label>
                            <input type="number" id="pain-level" min="0" max="10" value="0">
                        </div>

                        <div class="form-group">
                            <label for="pain-location">Local da Dor</label>
                            <input type="text" id="pain-location" placeholder="Ex: joelho direito">
                        </div>

                        <div class="form-group">
                            <label for="sleep-hours">Sono (horas)</label>
                            <input type="number" id="sleep-hours" min="0" max="12" step="0.5">
                        </div>

                        <div class="form-group full-width">
                            <label for="training-notes">Observações</label>
                            <textarea id="training-notes" rows="3" placeholder="Como se sentiu, condições climáticas, etc."></textarea>
                        </div>
                    </div>

                    <div class="form-actions">
                        <button type="submit" class="btn btn--primary">Salvar Treino</button>
                        <button type="button" class="btn btn--secondary" onclick="clearTrainingForm()">Limpar</button>
                    </div>

                    <div class="srpe-display">
                        <strong>sRPE Load calculado: <span id="srpe-value">0</span></strong>
                    </div>
                </form>
            </div>
        </div>

        <!-- Tests Section -->
        <div id="tests-section" class="section">
            <div class="container">
                <div class="section-header">
                    <h2>Simulados & Testes</h2>
                    <div class="form-subtitle">Registre os resultados dos testes programados</div>
                </div>
                
                <div class="tests-grid">
                    <div class="test-card" data-test="3k">
                        <div class="test-header">
                            <h3>Teste 3km</h3>
                            <div class="test-date">15/10/2025 (Semana 2)</div>
                        </div>
                        <div class="test-protocol">
                            10-12min aquecimento + 3km forte + 8-10min desaquecimento
                        </div>
                        <div class="test-result">
                            <div class="result-time" id="result-3k">--:--</div>
                            <div class="result-pace" id="pace-3k">--:--/km</div>
                        </div>
                        <button class="btn btn--outline" onclick="openTestModal('3k')">Registrar Resultado</button>
                    </div>

                    <div class="test-card" data-test="5k">
                        <div class="test-header">
                            <h3>Simulado 5km</h3>
                            <div class="test-date">28/10/2025 (Semana 4)</div>
                        </div>
                        <div class="test-protocol">
                            12-15min aquecimento + 5km competitivo + 8-10min desaquecimento
                        </div>
                        <div class="test-result">
                            <div class="result-time" id="result-5k">30:00</div>
                            <div class="result-pace" id="pace-5k">6:00/km</div>
                        </div>
                        <button class="btn btn--outline" onclick="openTestModal('5k')">Atualizar Resultado</button>
                    </div>

                    <div class="test-card" data-test="7k">
                        <div class="test-header">
                            <h3>Simulado 7km OBJETIVO</h3>
                            <div class="test-date">12/11/2025 (Semana 6)</div>
                        </div>
                        <div class="test-protocol">
                            15-18min aquecimento + 7km competitivo + 8-10min desaquecimento
                        </div>
                        <div class="test-result">
                            <div class="result-time" id="result-7k">--:--</div>
                            <div class="result-pace" id="pace-7k">--:--/km</div>
                        </div>
                        <button class="btn btn--primary" onclick="openTestModal('7k')">Registrar Meta!</button>
                    </div>
                </div>
            </div>
        </div>

        <!-- Zones Section -->
        <div id="zones-section" class="section">
            <div class="container">
                <div class="section-header">
                    <h2>Zonas de Treinamento</h2>
                    <div class="form-subtitle">Zonas atualizadas baseadas nos simulados</div>
                </div>
                
                <div class="zones-table">
                    <div class="zone-row zone-header">
                        <div>Zona</div>
                        <div>Pace (min/km)</div>
                        <div>FC (bpm)</div>
                        <div>RPE</div>
                        <div>Descrição</div>
                    </div>
                    <div class="zone-row z1">
                        <div class="zone-name">Z1 - Recuperação</div>
                        <div class="zone-pace" id="z1-pace">7:30</div>
                        <div class="zone-hr" id="z1-hr">86-103</div>
                        <div class="zone-rpe">1-3</div>
                        <div class="zone-desc">Corrida muito fácil, conversa fluida</div>
                    </div>
                    <div class="zone-row z2">
                        <div class="zone-name">Z2 - Base</div>
                        <div class="zone-pace" id="z2-pace">6:47</div>
                        <div class="zone-hr" id="z2-hr">103-121</div>
                        <div class="zone-rpe">4-5</div>
                        <div class="zone-desc">Corrida confortável, pode conversar</div>
                    </div>
                    <div class="zone-row z3">
                        <div class="zone-name">Z3 - Limiar</div>
                        <div class="zone-pace" id="z3-pace">6:12</div>
                        <div class="zone-hr" id="z3-hr">121-138</div>
                        <div class="zone-rpe">6-7</div>
                        <div class="zone-desc">Esforço moderado a forte</div>
                    </div>
                    <div class="zone-row z4">
                        <div class="zone-name">Z4 - VO2</div>
                        <div class="zone-pace" id="z4-pace">5:30</div>
                        <div class="zone-hr" id="z4-hr">138-155</div>
                        <div class="zone-rpe">7-8</div>
                        <div class="zone-desc">Esforço forte, 3-8 min sustentável</div>
                    </div>
                    <div class="zone-row z5">
                        <div class="zone-name">Z5 - Muito Intenso</div>
                        <div class="zone-pace" id="z5-pace">5:00</div>
                        <div class="zone-hr" id="z5-hr">155-173</div>
                        <div class="zone-rpe">9-10</div>
                        <div class="zone-desc">Esforço máximo, até 3 min</div>
                    </div>
                </div>
            </div>
        </div>

        <!-- Body Section -->
        <div id="body-section" class="section">
            <div class="container">
                <div class="section-header">
                    <h2>Medidas Corporais</h2>
                    <div class="form-subtitle">Coleta semanal - sempre no domingo pela manhã</div>
                </div>
                
                <form id="body-form" class="body-form">
                    <div class="form-grid">
                        <div class="form-group">
                            <label for="measurement-date">Data da Avaliação</label>
                            <input type="date" id="measurement-date" required>
                        </div>

                        <div class="form-group">
                            <label for="body-weight">Peso (kg)</label>
                            <input type="number" id="body-weight" min="30" max="200" step="0.1" required>
                        </div>

                        <div class="form-group">
                            <label for="waist">Cintura (cm)</label>
                            <input type="number" id="waist" min="50" max="150" step="0.1">
                        </div>

                        <div class="form-group">
                            <label for="hip">Quadril (cm)</label>
                            <input type="number" id="hip" min="50" max="150" step="0.1">
                        </div>

                        <div class="form-group">
                            <label for="chest">Peitoral (cm)</label>
                            <input type="number" id="chest" min="50" max="150" step="0.1">
                        </div>

                        <div class="form-group">
                            <label for="thigh">Coxa (cm)</label>
                            <input type="number" id="thigh" min="30" max="100" step="0.1">
                        </div>

                        <div class="form-group full-width">
                            <label for="body-notes">Observações</label>
                            <textarea id="body-notes" rows="2" placeholder="Retenção hídrica, ciclo menstrual, etc."></textarea>
                        </div>
                    </div>

                    <div class="form-actions">
                        <button type="submit" class="btn btn--primary">Salvar Medidas</button>
                        <button type="button" class="btn btn--secondary" onclick="clearBodyForm()">Limpar</button>
                    </div>
                </form>

                <div class="body-evolution">
                    <h3>Evolução das Medidas</h3>
                    <div class="chart-placeholder">
                        📈 Gráfico de evolução será exibido após registrar medidas
                    </div>
                </div>
            </div>
        </div>
    </div>

    <!-- Test Modal -->
    <div id="test-modal" class="modal">
        <div class="modal-content">
            <div class="modal-header">
                <h3 id="modal-title">Registrar Teste</h3>
                <button class="close-modal">&times;</button>
            </div>
            <form id="test-form">
                <div class="form-group">
                    <label for="test-time">Tempo Total (mm:ss)</label>
                    <input type="text" id="test-time" pattern="[0-9]{1,2}:[0-9]{2}" placeholder="00:00" required>
                </div>
                <div class="form-group">
                    <label for="test-hr-avg">FC Média (bpm)</label>
                    <input type="number" id="test-hr-avg" min="60" max="220">
                </div>
                <div class="form-group">
                    <label for="test-hr-max">FC Máxima (bpm)</label>
                    <input type="number" id="test-hr-max" min="60" max="220">
                </div>
                <div class="form-group">
                    <label for="test-rpe">RPE (1-10)</label>
                    <input type="number" id="test-rpe" min="1" max="10" required>
                </div>
                <div class="form-group">
                    <label for="test-conditions">Condições Ambientais</label>
                    <input type="text" id="test-conditions" placeholder="Ex: 25°C, vento fraco">
                </div>
                <div class="form-group">
                    <label for="test-notes">Observações</label>
                    <textarea id="test-notes" rows="3"></textarea>
                </div>
                <div class="modal-actions">
                    <button type="submit" class="btn btn--primary">Salvar Resultado</button>
                    <button type="button" class="btn btn--secondary" onclick="closeTestModal()">Cancelar</button>
                </div>
            </form>
        </div>
    </div>

    <script src="app.js"></script>
</body>
</html>'''

# Salvar o arquivo HTML
with open('planilha-corrida-7km/index.html', 'w', encoding='utf-8') as f:
    f.write(html_content)

print("✅ index.html criado com sucesso!")
print("Tamanho do arquivo:", len(html_content), "caracteres")