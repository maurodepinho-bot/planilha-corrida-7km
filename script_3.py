# JavaScript completo para a aplicação
js_content = '''// Aplicação de Treino de Corrida - JavaScript Principal
let currentAthlete = null;
let currentSection = 'dashboard';
let trainingData = {};
let testResults = {};
let bodyMeasurements = {};

// Dados da aplicação
const appData = {
    atletas: {
        mauro: {
            nome: "Mauro",
            idade: 47,
            peso: 112,
            altura: 1.91,
            fc_max: 173,
            fc_rep: 65,
            baseline_5k: "30:00",
            meta_7k: "32:40"
        },
        franciane: {
            nome: "Franciane",
            idade: 35,
            peso: 63,
            altura: 1.65,
            fc_max: 185,
            fc_rep: 55,
            baseline_5k: "30:00",
            meta_7k: "32:40"
        }
    },
    
    plano_6_semanas: [
        {
            semana: 1,
            data_inicio: "07/10/2025",
            treinos: {
                terca: {
                    objetivo: "Tempo introdutório",
                    tipo: "tempo-limiar",
                    estrutura: "12min aquec Z1-Z2 + 3×6min Z3 (2min trote) + 8-10min desaq",
                    duracao: 55,
                    distancia: 8.5,
                    zona: "Z3"
                },
                quarta: {
                    objetivo: "Rodagem + técnica",
                    tipo: "tecnica",
                    estrutura: "30-35min Z2 + 6×100m strides (60-90s) + 8-10min mobilidade",
                    duracao: 55,
                    distancia: 6.0,
                    zona: "Z2 + strides"
                },
                domingo: {
                    objetivo: "Longão progressivo",
                    tipo: "longao",
                    estrutura: "45-50min Z2 + 8-10min Z3 leve + 5-8min desaq",
                    duracao: 60,
                    distancia: 9.0,
                    zona: "Z2→Z3"
                }
            }
        },
        {
            semana: 2,
            data_inicio: "14/10/2025",
            treinos: {
                terca: {
                    objetivo: "Tempo contínuo",
                    tipo: "tempo-limiar",
                    estrutura: "12-15min aquec + 18-22min Z3 + 8-10min desaq",
                    duracao: 50,
                    distancia: 7.5,
                    zona: "Z3"
                },
                quarta: {
                    objetivo: "Teste 3km forte",
                    tipo: "simulado",
                    estrutura: "10-12min aquec + 4×30s strides + 3km forte + 8-10min desaq",
                    duracao: 45,
                    distancia: 5.0,
                    zona: "Teste forte",
                    teste: true
                },
                domingo: {
                    objetivo: "Longão Z2",
                    tipo: "longao",
                    estrutura: "55-60min Z2 + 5min desaq",
                    duracao: 60,
                    distancia: 9.5,
                    zona: "Z2"
                }
            }
        },
        {
            semana: 3,
            data_inicio: "21/10/2025",
            treinos: {
                terca: {
                    objetivo: "VO2 curto",
                    tipo: "vo2",
                    estrutura: "12-15min aquec + 6×400m Z4 (2min trote) + 8-10min desaq",
                    duracao: 55,
                    distancia: 6.5,
                    zona: "Z4"
                },
                quarta: {
                    objetivo: "Tempo curto + Z2",
                    tipo: "tempo-limiar",
                    estrutura: "10-12min aquec + 2×8-10min Z3 (2-3min trote) + 6-8min desaq",
                    duracao: 55,
                    distancia: 7.0,
                    zona: "Z3"
                },
                domingo: {
                    objetivo: "Longão específico",
                    tipo: "longao",
                    estrutura: "40-45min Z2 + 12-15min prog até Z3-alto + 5-8min desaq",
                    duracao: 60,
                    distancia: 9.5,
                    zona: "Z2→Z3-alto"
                }
            }
        },
        {
            semana: 4,
            data_inicio: "28/10/2025",
            treinos: {
                terca: {
                    objetivo: "Simulado 5km",
                    tipo: "simulado",
                    estrutura: "12-15min aquec + 4×20-30s strides + 5km competitivo + 8-10min desaq",
                    duracao: 50,
                    distancia: 7.0,
                    zona: "Competitivo 5km",
                    teste: true
                },
                quarta: {
                    objetivo: "Rodagem + técnica",
                    tipo: "tecnica",
                    estrutura: "30-35min Z2 + 6×100m strides + 8-10min mobilidade",
                    duracao: 55,
                    distancia: 6.0,
                    zona: "Z2 + strides"
                },
                domingo: {
                    objetivo: "Longão reduzido",
                    tipo: "longao",
                    estrutura: "45-50min Z2 + 5-8min desaq",
                    duracao: 55,
                    distancia: 8.5,
                    zona: "Z2"
                }
            }
        },
        {
            semana: 5,
            data_inicio: "04/11/2025",
            treinos: {
                terca: {
                    objetivo: "Tempo específico",
                    tipo: "tempo-limiar",
                    estrutura: "12-15min aquec + 2×12-14min Z3-Z4 baixo (3min pausa) + 8-10min desaq",
                    duracao: 58,
                    distancia: 8.0,
                    zona: "Z3-Z4 baixo"
                },
                quarta: {
                    objetivo: "VO2 médio",
                    tipo: "vo2",
                    estrutura: "12-15min aquec + 5×800m Z4 (2-3min trote) + 6-8min desaq",
                    duracao: 60,
                    distancia: 7.5,
                    zona: "Z4"
                },
                domingo: {
                    objetivo: "Longão específico",
                    tipo: "longao",
                    estrutura: "35-40min Z2 + 15-18min prog até pace alvo 7km + 5-8min desaq",
                    duracao: 60,
                    distancia: 9.0,
                    zona: "Z2→Pace alvo"
                }
            }
        },
        {
            semana: 6,
            data_inicio: "11/11/2025",
            treinos: {
                terca: {
                    objetivo: "Afinar ritmo",
                    tipo: "tempo-limiar",
                    estrutura: "10-12min aquec + 4×5min Z3-Z4 baixo (2min trote) + 6-8min desaq",
                    duracao: 50,
                    distancia: 7.0,
                    zona: "Z3-Z4 baixo"
                },
                quarta: {
                    objetivo: "Simulado 7km",
                    tipo: "simulado",
                    estrutura: "15-18min aquec + 4×20s strides + 7km competitivo + 8-10min desaq",
                    duracao: 60,
                    distancia: 10.0,
                    zona: "Pace alvo 4:40/km",
                    teste: true
                },
                domingo: {
                    objetivo: "Soltura",
                    tipo: "tecnica",
                    estrutura: "25-35min Z1-Z2 + mobilidade",
                    duracao: 35,
                    distancia: 5.0,
                    zona: "Z1-Z2"
                }
            }
        }
    ],
    
    zonas: {
        mauro: {
            z1: { pace: "7:30", fc: "86-103", rpe: "1-3", desc: "Recuperação" },
            z2: { pace: "6:47", fc: "103-121", rpe: "4-5", desc: "Base aeróbica" },
            z3: { pace: "6:12", fc: "121-138", rpe: "6-7", desc: "Limiar" },
            z4: { pace: "5:30", fc: "138-155", rpe: "7-8", desc: "VO2 máx" },
            z5: { pace: "5:00", fc: "155-173", rpe: "9-10", desc: "Muito intenso" }
        },
        franciane: {
            z1: { pace: "7:12", fc: "92-111", rpe: "1-3", desc: "Recuperação" },
            z2: { pace: "6:30", fc: "111-129", rpe: "4-5", desc: "Base aeróbica" },
            z3: { pace: "5:54", fc: "129-148", rpe: "6-7", desc: "Limiar" },
            z4: { pace: "5:18", fc: "148-166", rpe: "7-8", desc: "VO2 máx" },
            z5: { pace: "4:48", fc: "166-185", rpe: "9-10", desc: "Muito intenso" }
        }
    }
};

// Inicialização
document.addEventListener('DOMContentLoaded', function() {
    loadStoredData();
    initializeEventListeners();
    showAthleteSelection();
});

// Carregar dados salvos
function loadStoredData() {
    const stored = localStorage.getItem('runningAppData');
    if (stored) {
        const data = JSON.parse(stored);
        trainingData = data.trainingData || {};
        testResults = data.testResults || {};
        bodyMeasurements = data.bodyMeasurements || {};
    }
}

// Salvar dados
function saveData() {
    const dataToSave = {
        trainingData,
        testResults,
        bodyMeasurements,
        lastUpdate: new Date().toISOString()
    };
    localStorage.setItem('runningAppData', JSON.stringify(dataToSave));
}

// Event Listeners
function initializeEventListeners() {
    // Seleção de atleta
    document.querySelectorAll('.athlete-card').forEach(card => {
        card.addEventListener('click', function() {
            const athlete = this.dataset.athlete;
            selectAthlete(athlete);
        });
    });

    // Navegação
    document.querySelectorAll('.nav-link').forEach(link => {
        link.addEventListener('click', function() {
            const section = this.dataset.section;
            showSection(section);
        });
    });

    // Formulário de treino
    document.getElementById('training-form').addEventListener('submit', saveTraining);
    document.getElementById('training-duration').addEventListener('input', calculatePaceAndSRPE);
    document.getElementById('training-distance').addEventListener('input', calculatePaceAndSRPE);
    document.getElementById('rpe-slider').addEventListener('input', syncRPE);
    document.getElementById('rpe-input').addEventListener('input', syncRPE);

    // Formulário de medidas corporais
    document.getElementById('body-form').addEventListener('submit', saveBodyMeasurement);

    // Formulário de teste
    document.getElementById('test-form').addEventListener('submit', saveTestResult);

    // Modal
    document.querySelector('.close-modal').addEventListener('click', closeTestModal);
    document.getElementById('test-modal').addEventListener('click', function(e) {
        if (e.target === this) closeTestModal();
    });

    // Definir data atual
    const today = new Date().toISOString().split('T')[0];
    document.getElementById('training-date').value = today;
    document.getElementById('measurement-date').value = today;
}

// Seleção de atleta
function selectAthlete(athlete) {
    currentAthlete = athlete;
    document.getElementById('athlete-selection').style.display = 'none';
    document.getElementById('main-dashboard').style.display = 'block';
    
    updateAthleteInfo();
    showSection('dashboard');
    updateDashboard();
    generatePlan();
    updateZones();
}

function showAthleteSelection() {
    currentAthlete = null;
    document.getElementById('athlete-selection').style.display = 'flex';
    document.getElementById('main-dashboard').style.display = 'none';
}

// Atualizar informações do atleta
function updateAthleteInfo() {
    const athleteData = appData.atletas[currentAthlete];
    document.querySelector('.athlete-name').textContent = athleteData.nome;
    document.querySelector('.current-week').textContent = getCurrentWeek();
}

function getCurrentWeek() {
    const startDate = new Date('2025-10-07');
    const today = new Date();
    const diffTime = today - startDate;
    const diffWeeks = Math.ceil(diffTime / (1000 * 60 * 60 * 24 * 7));
    
    if (diffWeeks < 1) return 'Programa inicia em breve';
    if (diffWeeks > 6) return 'Programa concluído';
    return `Semana ${diffWeeks} de 6`;
}

// Navegação entre seções
function showSection(section) {
    currentSection = section;
    
    // Atualizar navegação ativa
    document.querySelectorAll('.nav-link').forEach(link => {
        link.classList.remove('active');
    });
    document.querySelector(`[data-section="${section}"]`).classList.add('active');
    
    // Mostrar seção
    document.querySelectorAll('.section').forEach(sec => {
        sec.classList.remove('active');
    });
    document.getElementById(`${section}-section`).classList.add('active');
    
    // Atualizações específicas por seção
    if (section === 'dashboard') updateDashboard();
    if (section === 'tests') updateTestsDisplay();
}

// Atualizar Dashboard
function updateDashboard() {
    if (!currentAthlete) return;
    
    const athleteTrainings = trainingData[currentAthlete] || [];
    const athleteTests = testResults[currentAthlete] || {};
    
    // Atualizar KPIs
    updateCompletionRate(athleteTrainings);
    updateWeeklyLoad(athleteTrainings);
    updateBestTimes(athleteTests);
    updateNextTraining();
    updateAlerts(athleteTrainings);
    
    // Atualizar última atualização
    document.getElementById('last-update').textContent = new Date().toLocaleString('pt-BR');
}

function updateCompletionRate(trainings) {
    const completed = trainings.filter(t => t.completed === 'sim' || t.completed === 'parcial').length;
    const total = 18; // 6 semanas × 3 treinos
    const rate = Math.round((completed / total) * 100);
    
    document.getElementById('completion-rate').textContent = `${rate}%`;
    document.getElementById('completion-count').textContent = `${completed} de ${total}`;
}

function updateWeeklyLoad(trainings) {
    const thisWeek = getCurrentWeekNumber();
    const weekTrainings = trainings.filter(t => getWeekFromDate(t.date) === thisWeek);
    const load = weekTrainings.reduce((sum, t) => sum + (t.srpe || 0), 0);
    
    document.getElementById('weekly-load').textContent = load;
    
    const status = load > 400 ? 'Carga alta - atenção!' : 
                   load > 300 ? 'Carga moderada' : 'Dentro do limite';
    document.getElementById('load-status').textContent = status;
}

function updateBestTimes(tests) {
    const best5k = tests['5k'] ? tests['5k'].time : '30:00';
    const pace5k = tests['5k'] ? calculatePace(tests['5k'].time, 5) : '6:00/km';
    
    document.getElementById('best-5k').textContent = best5k;
    document.getElementById('best-5k-pace').textContent = pace5k;
}

function updateNextTraining() {
    const today = new Date();
    const nextTraining = findNextTraining(today);
    
    if (nextTraining) {
        const card = document.getElementById('next-training');
        card.querySelector('.training-date').textContent = formatDate(nextTraining.date);
        card.querySelector('.training-type').textContent = nextTraining.objetivo;
        card.querySelector('.training-details').textContent = nextTraining.estrutura;
        card.querySelector('.training-meta').innerHTML = `
            <span>⏱️ ${nextTraining.duracao}min</span>
            <span>📏 ${nextTraining.distancia}km</span>
            <span>💪 ${nextTraining.zona}</span>
        `;
    }
}

function updateAlerts(trainings) {
    const container = document.getElementById('alerts-container');
    const alerts = generateAlerts(trainings);
    
    container.innerHTML = '';
    
    if (alerts.length === 0) {
        container.innerHTML = `
            <div class="alert info">
                <div class="alert-icon">✅</div>
                <div class="alert-content">
                    <strong>Tudo certo!</strong> Nenhum alerta no momento.
                </div>
            </div>
        `;
    } else {
        alerts.forEach(alert => {
            container.innerHTML += `
                <div class="alert ${alert.type}">
                    <div class="alert-icon">${alert.icon}</div>
                    <div class="alert-content">
                        <strong>${alert.title}</strong> ${alert.message}
                    </div>
                </div>
            `;
        });
    }
}

function generateAlerts(trainings) {
    const alerts = [];
    
    // Verificar RPE alto consecutivo
    const recentTrainings = trainings.slice(-3);
    const highRPE = recentTrainings.filter(t => t.rpe >= 8);
    if (highRPE.length >= 2) {
        alerts.push({
            type: 'warning',
            icon: '⚠️',
            title: 'RPE Alto Detectado',
            message: 'Você tem treinos com RPE ≥ 8 em dias consecutivos. Considere reduzir a intensidade.'
        });
    }
    
    // Verificar dor
    const painfulTrainings = recentTrainings.filter(t => t.pain && t.pain >= 6);
    if (painfulTrainings.length > 0) {
        alerts.push({
            type: 'danger',
            icon: '🚨',
            title: 'Dor Elevada',
            message: 'Você reportou dor ≥ 6/10. Considere avaliação médica antes de continuar.'
        });
    }
    
    // Verificar progressão de carga
    const thisWeek = getCurrentWeekNumber();
    const lastWeek = thisWeek - 1;
    
    if (lastWeek > 0) {
        const thisWeekLoad = getWeeklyLoad(trainings, thisWeek);
        const lastWeekLoad = getWeeklyLoad(trainings, lastWeek);
        
        if (thisWeekLoad > lastWeekLoad * 1.2) {
            alerts.push({
                type: 'warning',
                icon: '📈',
                title: 'Progressão Rápida',
                message: 'Sua carga semanal aumentou mais de 20%. Monitore os sinais do corpo.'
            });
        }
    }
    
    return alerts;
}

// Gerar plano de 6 semanas
function generatePlan() {
    const planGrid = document.getElementById('plan-grid');
    planGrid.innerHTML = '';
    
    appData.plano_6_semanas.forEach(week => {
        const weekEl = createWeekElement(week);
        planGrid.appendChild(weekEl);
    });
}

function createWeekElement(week) {
    const weekDiv = document.createElement('div');
    weekDiv.className = 'week-section';
    
    const endDate = addDays(new Date(week.data_inicio), 6);
    
    weekDiv.innerHTML = `
        <div class="week-header">
            <div class="week-title">Semana ${week.semana}</div>
            <div class="week-period">${formatDateBR(week.data_inicio)} - ${formatDateBR(endDate.toISOString().split('T')[0])}</div>
        </div>
        <div class="week-trainings">
            ${Object.entries(week.treinos).map(([day, training]) => 
                createTrainingElement(day, training, week.semana)
            ).join('')}
        </div>
    `;
    
    return weekDiv;
}

function createTrainingElement(day, training, week) {
    const dayNames = {
        terca: 'Terça-feira',
        quarta: 'Quarta-feira', 
        domingo: 'Domingo'
    };
    
    const typeClass = training.tipo.replace(/[^a-z0-9]/gi, '-').toLowerCase();
    
    return `
        <div class="training-item ${typeClass}">
            <div class="training-day">${dayNames[day]}</div>
            <div class="training-objective">
                ${training.objetivo}
                ${training.teste ? ' 🏆' : ''}
            </div>
            <div class="training-structure">${training.estrutura}</div>
            <div class="training-specs">
                <span>⏱️ ${training.duracao}min</span>
                <span>📏 ${training.distancia}km</span>
                <span>💪 ${training.zona}</span>
            </div>
        </div>
    `;
}

// Salvar treino
function saveTraining(e) {
    e.preventDefault();
    
    if (!currentAthlete) return;
    
    const formData = new FormData(e.target);
    const trainingRecord = {
        id: Date.now(),
        athlete: currentAthlete,
        date: document.getElementById('training-date').value,
        type: document.getElementById('training-type').value,
        duration: parseInt(document.getElementById('training-duration').value),
        distance: parseFloat(document.getElementById('training-distance').value),
        pace: document.getElementById('average-pace').value,
        rpe: parseInt(document.getElementById('rpe-input').value),
        avgHR: document.getElementById('avg-hr').value ? parseInt(document.getElementById('avg-hr').value) : null,
        maxHR: document.getElementById('max-hr').value ? parseInt(document.getElementById('max-hr').value) : null,
        completed: document.getElementById('completed').value,
        pain: parseInt(document.getElementById('pain-level').value),
        painLocation: document.getElementById('pain-location').value,
        sleepHours: document.getElementById('sleep-hours').value ? parseFloat(document.getElementById('sleep-hours').value) : null,
        notes: document.getElementById('training-notes').value,
        srpe: parseInt(document.getElementById('training-duration').value) * parseInt(document.getElementById('rpe-input').value),
        timestamp: new Date().toISOString()
    };
    
    if (!trainingData[currentAthlete]) {
        trainingData[currentAthlete] = [];
    }
    
    trainingData[currentAthlete].push(trainingRecord);
    saveData();
    
    // Resetar formulário
    e.target.reset();
    document.getElementById('training-date').value = new Date().toISOString().split('T')[0];
    document.getElementById('average-pace').value = '';
    document.getElementById('srpe-value').textContent = '0';
    
    // Mostrar confirmação
    showAlert('Treino salvo com sucesso!', 'success');
    
    // Atualizar dashboard
    updateDashboard();
}

// Calcular pace e sRPE
function calculatePaceAndSRPE() {
    const duration = document.getElementById('training-duration').value;
    const distance = document.getElementById('training-distance').value;
    const rpe = document.getElementById('rpe-input').value;
    
    if (duration && distance) {
        const paceMinutes = duration / distance;
        const mins = Math.floor(paceMinutes);
        const secs = Math.round((paceMinutes - mins) * 60);
        document.getElementById('average-pace').value = `${mins}:${secs.toString().padStart(2, '0')}/km`;
    }
    
    if (duration && rpe) {
        document.getElementById('srpe-value').textContent = duration * rpe;
    }
}

// Sincronizar RPE
function syncRPE(e) {
    const value = e.target.value;
    document.getElementById('rpe-slider').value = value;
    document.getElementById('rpe-input').value = value;
    calculatePaceAndSRPE();
}

// Limpar formulário de treino
function clearTrainingForm() {
    document.getElementById('training-form').reset();
    document.getElementById('training-date').value = new Date().toISOString().split('T')[0];
    document.getElementById('average-pace').value = '';
    document.getElementById('srpe-value').textContent = '0';
}

// Salvar medidas corporais
function saveBodyMeasurement(e) {
    e.preventDefault();
    
    if (!currentAthlete) return;
    
    const measurement = {
        id: Date.now(),
        athlete: currentAthlete,
        date: document.getElementById('measurement-date').value,
        weight: parseFloat(document.getElementById('body-weight').value),
        waist: document.getElementById('waist').value ? parseFloat(document.getElementById('waist').value) : null,
        hip: document.getElementById('hip').value ? parseFloat(document.getElementById('hip').value) : null,
        chest: document.getElementById('chest').value ? parseFloat(document.getElementById('chest').value) : null,
        thigh: document.getElementById('thigh').value ? parseFloat(document.getElementById('thigh').value) : null,
        notes: document.getElementById('body-notes').value,
        timestamp: new Date().toISOString()
    };
    
    if (!bodyMeasurements[currentAthlete]) {
        bodyMeasurements[currentAthlete] = [];
    }
    
    bodyMeasurements[currentAthlete].push(measurement);
    saveData();
    
    clearBodyForm();
    showAlert('Medidas salvas com sucesso!', 'success');
}

function clearBodyForm() {
    document.getElementById('body-form').reset();
    document.getElementById('measurement-date').value = new Date().toISOString().split('T')[0];
}

// Testes e Simulados
function updateTestsDisplay() {
    const athleteTests = testResults[currentAthlete] || {};
    
    // Atualizar cards de teste
    ['3k', '5k', '7k'].forEach(distance => {
        const result = athleteTests[distance];
        if (result) {
            document.getElementById(`result-${distance}`).textContent = result.time;
            document.getElementById(`pace-${distance}`).textContent = calculatePace(result.time, parseInt(distance));
        }
    });
}

let currentTestType = null;

function openTestModal(testType) {
    currentTestType = testType;
    const modal = document.getElementById('test-modal');
    const title = document.getElementById('modal-title');
    
    const titles = {
        '3k': 'Registrar Teste 3km',
        '5k': 'Registrar Simulado 5km', 
        '7k': 'Registrar Simulado 7km - META!'
    };
    
    title.textContent = titles[testType];
    modal.style.display = 'block';
}

function closeTestModal() {
    document.getElementById('test-modal').style.display = 'none';
    document.getElementById('test-form').reset();
    currentTestType = null;
}

function saveTestResult(e) {
    e.preventDefault();
    
    if (!currentAthlete || !currentTestType) return;
    
    const testResult = {
        type: currentTestType,
        time: document.getElementById('test-time').value,
        avgHR: document.getElementById('test-hr-avg').value ? parseInt(document.getElementById('test-hr-avg').value) : null,
        maxHR: document.getElementById('test-hr-max').value ? parseInt(document.getElementById('test-hr-max').value) : null,
        rpe: parseInt(document.getElementById('test-rpe').value),
        conditions: document.getElementById('test-conditions').value,
        notes: document.getElementById('test-notes').value,
        pace: calculatePace(document.getElementById('test-time').value, parseInt(currentTestType)),
        date: new Date().toISOString().split('T')[0],
        timestamp: new Date().toISOString()
    };
    
    if (!testResults[currentAthlete]) {
        testResults[currentAthlete] = {};
    }
    
    testResults[currentAthlete][currentTestType] = testResult;
    saveData();
    
    closeTestModal();
    updateTestsDisplay();
    updateDashboard();
    
    showAlert(`Resultado do ${currentTestType} salvo com sucesso!`, 'success');
    
    // Sugerir atualização de zonas
    if (confirm('Deseja atualizar suas zonas de treino baseadas neste resultado?')) {
        updateZonesFromTest(currentTestType, testResult);
    }
}

// Atualizar zonas
function updateZones() {
    if (!currentAthlete) return;
    
    const zones = appData.zonas[currentAthlete];
    
    Object.entries(zones).forEach(([zone, data]) => {
        document.getElementById(`${zone}-pace`).textContent = data.pace;
        document.getElementById(`${zone}-hr`).textContent = data.fc;
    });
}

function updateZonesFromTest(testType, result) {
    // Lógica simplificada de recalibração de zonas
    // Em uma implementação real, usaria fórmulas de VDOT
    
    const paceSeconds = timeToSeconds(result.time);
    const distance = parseInt(testType);
    const pacePerKm = paceSeconds / distance;
    
    // Estimativas básicas baseadas no resultado do teste
    const newZones = {
        z1: secondsToTime(pacePerKm * 1.3),
        z2: secondsToTime(pacePerKm * 1.15), 
        z3: secondsToTime(pacePerKm * 1.05),
        z4: secondsToTime(pacePerKm * 0.95),
        z5: secondsToTime(pacePerKm * 0.85)
    };
    
    // Atualizar interface
    Object.entries(newZones).forEach(([zone, pace]) => {
        document.getElementById(`${zone}-pace`).textContent = pace;
        appData.zonas[currentAthlete][zone].pace = pace;
    });
    
    showAlert('Zonas de treino atualizadas com base no teste!', 'success');
}

// Utilitários
function calculatePace(timeStr, distance) {
    const totalSeconds = timeToSeconds(timeStr);
    const paceSeconds = totalSeconds / distance;
    return secondsToTime(paceSeconds) + '/km';
}

function timeToSeconds(timeStr) {
    const [mins, secs] = timeStr.split(':').map(Number);
    return mins * 60 + secs;
}

function secondsToTime(seconds) {
    const mins = Math.floor(seconds / 60);
    const secs = Math.round(seconds % 60);
    return `${mins}:${secs.toString().padStart(2, '0')}`;
}

function formatDate(dateStr) {
    return new Date(dateStr).toLocaleDateString('pt-BR', {
        weekday: 'long',
        day: '2-digit',
        month: '2-digit',
        year: 'numeric'
    });
}

function formatDateBR(dateStr) {
    return new Date(dateStr).toLocaleDateString('pt-BR');
}

function addDays(date, days) {
    const result = new Date(date);
    result.setDate(result.getDate() + days);
    return result;
}

function getCurrentWeekNumber() {
    const startDate = new Date('2025-10-07');
    const today = new Date();
    const diffTime = today - startDate;
    return Math.ceil(diffTime / (1000 * 60 * 60 * 24 * 7));
}

function getWeekFromDate(dateStr) {
    const startDate = new Date('2025-10-07');
    const date = new Date(dateStr);
    const diffTime = date - startDate;
    return Math.ceil(diffTime / (1000 * 60 * 60 * 24 * 7));
}

function getWeeklyLoad(trainings, weekNum) {
    return trainings
        .filter(t => getWeekFromDate(t.date) === weekNum)
        .reduce((sum, t) => sum + (t.srpe || 0), 0);
}

function findNextTraining(fromDate) {
    const today = fromDate.toISOString().split('T')[0];
    
    for (let week of appData.plano_6_semanas) {
        const weekStart = new Date(week.data_inicio);
        
        // Terça
        const tuesday = new Date(weekStart);
        if (tuesday.toISOString().split('T')[0] >= today) {
            return { date: tuesday, ...week.treinos.terca };
        }
        
        // Quarta
        const wednesday = addDays(weekStart, 1);
        if (wednesday.toISOString().split('T')[0] >= today) {
            return { date: wednesday, ...week.treinos.quarta };
        }
        
        // Domingo
        const sunday = addDays(weekStart, 5);
        if (sunday.toISOString().split('T')[0] >= today) {
            return { date: sunday, ...week.treinos.domingo };
        }
    }
    
    return null;
}

function showAlert(message, type = 'info') {
    const alert = document.createElement('div');
    alert.className = `alert ${type} show-alert`;
    alert.innerHTML = `
        <div class="alert-icon">${type === 'success' ? '✅' : 'ℹ️'}</div>
        <div class="alert-content">${message}</div>
    `;
    
    alert.style.position = 'fixed';
    alert.style.top = '20px';
    alert.style.right = '20px';
    alert.style.zIndex = '9999';
    alert.style.minWidth = '300px';
    alert.style.animation = 'slideInRight 0.3s ease';
    
    document.body.appendChild(alert);
    
    setTimeout(() => {
        alert.style.animation = 'slideOutRight 0.3s ease';
        setTimeout(() => alert.remove(), 300);
    }, 3000);
}

// Estilos dinâmicos para alertas
const alertStyles = document.createElement('style');
alertStyles.textContent = `
    @keyframes slideInRight {
        from { transform: translateX(100%); opacity: 0; }
        to { transform: translateX(0); opacity: 1; }
    }
    @keyframes slideOutRight {
        from { transform: translateX(0); opacity: 1; }
        to { transform: translateX(100%); opacity: 0; }
    }
`;
document.head.appendChild(alertStyles);'''

# Salvar o arquivo JavaScript
with open('planilha-corrida-7km/app.js', 'w', encoding='utf-8') as f:
    f.write(js_content)

print("✅ app.js criado com sucesso!")
print("Tamanho do arquivo:", len(js_content), "caracteres")