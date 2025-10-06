# CSS completo para a aplicação
css_content = '''/* Reset e Base */
* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

body {
    font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, sans-serif;
    line-height: 1.6;
    color: #333;
    background-color: #f8fafc;
}

.container {
    max-width: 1200px;
    margin: 0 auto;
    padding: 0 20px;
}

/* Botões */
.btn {
    display: inline-flex;
    align-items: center;
    justify-content: center;
    padding: 12px 24px;
    border: none;
    border-radius: 8px;
    font-size: 16px;
    font-weight: 600;
    text-decoration: none;
    cursor: pointer;
    transition: all 0.2s ease;
    min-height: 48px;
}

.btn--primary {
    background: #4472c4;
    color: white;
}

.btn--primary:hover {
    background: #3559a3;
    transform: translateY(-1px);
    box-shadow: 0 4px 12px rgba(68, 114, 196, 0.3);
}

.btn--secondary {
    background: #64748b;
    color: white;
}

.btn--secondary:hover {
    background: #475569;
}

.btn--outline {
    background: transparent;
    color: #4472c4;
    border: 2px solid #4472c4;
}

.btn--outline:hover {
    background: #4472c4;
    color: white;
}

/* Seleção de Atletas */
.athlete-selection {
    min-height: 100vh;
    display: flex;
    align-items: center;
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    color: white;
}

.app-header {
    text-align: center;
    margin-bottom: 48px;
}

.app-header h1 {
    font-size: 2.5rem;
    margin-bottom: 16px;
    font-weight: 700;
}

.subtitle {
    font-size: 1.5rem;
    margin-bottom: 8px;
    opacity: 0.9;
}

.period {
    font-size: 1.1rem;
    opacity: 0.8;
}

.athletes-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(350px, 1fr));
    gap: 32px;
    margin-top: 48px;
}

.athlete-card {
    background: rgba(255, 255, 255, 0.95);
    color: #333;
    padding: 32px;
    border-radius: 16px;
    text-align: center;
    box-shadow: 0 8px 32px rgba(0, 0, 0, 0.1);
    backdrop-filter: blur(10px);
    transition: transform 0.3s ease, box-shadow 0.3s ease;
    cursor: pointer;
}

.athlete-card:hover {
    transform: translateY(-4px);
    box-shadow: 0 12px 40px rgba(0, 0, 0, 0.15);
}

.athlete-avatar {
    margin-bottom: 24px;
}

.avatar-circle {
    width: 80px;
    height: 80px;
    background: linear-gradient(135deg, #4472c4, #667eea);
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    margin: 0 auto;
    color: white;
    font-size: 32px;
    font-weight: bold;
}

.athlete-card h2 {
    font-size: 1.8rem;
    margin-bottom: 24px;
    color: #1e293b;
}

.athlete-info {
    margin-bottom: 24px;
    text-align: left;
}

.info-row {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 8px 0;
    border-bottom: 1px solid #e2e8f0;
}

.info-row:last-child {
    border-bottom: none;
}

.label {
    font-weight: 600;
    color: #64748b;
}

.value {
    font-weight: 600;
    color: #1e293b;
}

.progress-info {
    margin: 24px 0;
}

.progress-bar {
    width: 100%;
    height: 8px;
    background: #e2e8f0;
    border-radius: 4px;
    overflow: hidden;
    margin-bottom: 8px;
}

.progress-fill {
    height: 100%;
    background: linear-gradient(90deg, #4472c4, #667eea);
    border-radius: 4px;
    transition: width 0.5s ease;
}

.progress-text {
    font-size: 14px;
    color: #64748b;
    font-weight: 500;
}

/* Dashboard Principal */
.main-dashboard {
    min-height: 100vh;
}

.top-nav {
    background: white;
    border-bottom: 1px solid #e2e8f0;
    padding: 16px 0;
    position: sticky;
    top: 0;
    z-index: 100;
}

.nav-content {
    display: flex;
    align-items: center;
    gap: 24px;
    max-width: 1200px;
    margin: 0 auto;
    padding: 0 20px;
}

.back-btn {
    background: none;
    border: none;
    color: #4472c4;
    font-size: 16px;
    cursor: pointer;
    display: flex;
    align-items: center;
    gap: 8px;
    padding: 8px 12px;
    border-radius: 6px;
    transition: background 0.2s ease;
}

.back-btn:hover {
    background: #f1f5f9;
}

.current-athlete {
    display: flex;
    flex-direction: column;
}

.athlete-name {
    font-size: 18px;
    font-weight: 700;
    color: #1e293b;
}

.current-week {
    font-size: 14px;
    color: #64748b;
}

.nav-links {
    display: flex;
    gap: 8px;
    margin-left: auto;
}

.nav-link {
    padding: 8px 16px;
    background: none;
    border: none;
    color: #64748b;
    font-size: 14px;
    font-weight: 500;
    cursor: pointer;
    border-radius: 6px;
    transition: all 0.2s ease;
}

.nav-link:hover {
    background: #f1f5f9;
    color: #4472c4;
}

.nav-link.active {
    background: #4472c4;
    color: white;
}

/* Seções */
.section {
    display: none;
    padding: 32px 0;
}

.section.active {
    display: block;
}

.section-header {
    margin-bottom: 32px;
    text-align: center;
}

.section-header h2 {
    font-size: 2rem;
    color: #1e293b;
    margin-bottom: 8px;
}

.dashboard-header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 32px;
}

.dashboard-header h2 {
    font-size: 2rem;
    color: #1e293b;
}

.last-update {
    color: #64748b;
    font-size: 14px;
}

.form-subtitle {
    color: #64748b;
    font-size: 16px;
}

.plan-period {
    color: #4472c4;
    font-size: 18px;
    font-weight: 600;
}

/* KPI Grid */
.kpi-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
    gap: 24px;
    margin-bottom: 48px;
}

.kpi-card {
    background: white;
    padding: 24px;
    border-radius: 12px;
    box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
    border: 1px solid #e2e8f0;
}

.kpi-card.primary {
    background: linear-gradient(135deg, #4472c4, #667eea);
    color: white;
    border: none;
}

.kpi-header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 16px;
}

.kpi-header h3 {
    font-size: 14px;
    font-weight: 600;
    text-transform: uppercase;
    letter-spacing: 0.5px;
    opacity: 0.8;
}

.kpi-icon {
    font-size: 24px;
}

.kpi-value {
    font-size: 2.5rem;
    font-weight: 700;
    margin-bottom: 4px;
}

.kpi-subtitle {
    font-size: 14px;
    opacity: 0.8;
    margin-bottom: 16px;
}

.kpi-change {
    font-size: 12px;
    font-weight: 600;
    opacity: 0.9;
}

.kpi-progress {
    margin-top: 16px;
}

.kpi-progress .progress-bar {
    background: rgba(255, 255, 255, 0.2);
}

.kpi-progress .progress-fill {
    background: rgba(255, 255, 255, 0.9);
}

.kpi-progress span {
    font-size: 12px;
    opacity: 0.9;
}

/* Charts */
.charts-grid {
    display: grid;
    grid-template-columns: 2fr 1fr;
    gap: 24px;
    margin-bottom: 32px;
}

.chart-card {
    background: white;
    padding: 24px;
    border-radius: 12px;
    box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
    border: 1px solid #e2e8f0;
}

.chart-card h3 {
    margin-bottom: 16px;
    color: #1e293b;
}

.chart-placeholder {
    height: 200px;
    display: flex;
    align-items: center;
    justify-content: center;
    background: #f8fafc;
    border-radius: 8px;
    color: #64748b;
}

.chart-empty {
    text-align: center;
    font-size: 16px;
}

.next-training h3 {
    margin-bottom: 16px;
    color: #1e293b;
}

.training-card {
    background: #f8fafc;
    padding: 20px;
    border-radius: 8px;
    border-left: 4px solid #4472c4;
}

.training-date {
    font-size: 14px;
    color: #4472c4;
    font-weight: 600;
    margin-bottom: 8px;
}

.training-type {
    font-size: 18px;
    font-weight: 700;
    color: #1e293b;
    margin-bottom: 12px;
}

.training-details {
    font-size: 14px;
    color: #64748b;
    margin-bottom: 16px;
    line-height: 1.5;
}

.training-meta {
    display: flex;
    gap: 16px;
    font-size: 12px;
    color: #64748b;
    font-weight: 600;
}

/* Alertas */
.alerts-section h3 {
    margin-bottom: 16px;
    color: #1e293b;
}

.alerts-container {
    display: flex;
    flex-direction: column;
    gap: 12px;
}

.alert {
    display: flex;
    align-items: flex-start;
    gap: 12px;
    padding: 16px;
    border-radius: 8px;
    border: 1px solid;
}

.alert.info {
    background: #eff6ff;
    border-color: #3b82f6;
    color: #1e40af;
}

.alert.warning {
    background: #fffbeb;
    border-color: #f59e0b;
    color: #92400e;
}

.alert.danger {
    background: #fef2f2;
    border-color: #ef4444;
    color: #dc2626;
}

.alert-icon {
    font-size: 20px;
    flex-shrink: 0;
}

.alert-content strong {
    display: block;
    margin-bottom: 4px;
}

/* Plano Grid */
.plan-grid {
    display: grid;
    gap: 32px;
}

.week-section {
    background: white;
    padding: 24px;
    border-radius: 12px;
    box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
    border: 1px solid #e2e8f0;
}

.week-header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 24px;
    padding-bottom: 16px;
    border-bottom: 1px solid #e2e8f0;
}

.week-title {
    font-size: 1.5rem;
    font-weight: 700;
    color: #1e293b;
}

.week-period {
    color: #64748b;
    font-size: 14px;
}

.week-trainings {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
    gap: 16px;
}

.training-item {
    background: #f8fafc;
    padding: 20px;
    border-radius: 8px;
    border-left: 4px solid;
}

.training-item.tempo-limiar {
    border-left-color: #4472c4;
}

.training-item.tecnica {
    border-left-color: #10b981;
}

.training-item.longao {
    border-left-color: #f59e0b;
}

.training-item.vo2 {
    border-left-color: #ef4444;
}

.training-item.simulado {
    border-left-color: #8b5cf6;
    background: linear-gradient(135deg, #faf5ff, #f3e8ff);
}

.training-day {
    font-size: 12px;
    color: #64748b;
    font-weight: 600;
    text-transform: uppercase;
    letter-spacing: 0.5px;
    margin-bottom: 8px;
}

.training-objective {
    font-size: 16px;
    font-weight: 700;
    color: #1e293b;
    margin-bottom: 12px;
}

.training-structure {
    font-size: 14px;
    color: #64748b;
    margin-bottom: 16px;
    line-height: 1.5;
}

.training-specs {
    display: flex;
    gap: 16px;
    font-size: 12px;
    color: #64748b;
    font-weight: 600;
}

/* Formulários */
.training-form,
.body-form {
    background: white;
    padding: 32px;
    border-radius: 12px;
    box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
    border: 1px solid #e2e8f0;
}

.form-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
    gap: 24px;
    margin-bottom: 32px;
}

.form-group {
    display: flex;
    flex-direction: column;
}

.form-group.full-width {
    grid-column: 1 / -1;
}

.form-group label {
    font-weight: 600;
    color: #374151;
    margin-bottom: 8px;
    font-size: 14px;
}

.form-group input,
.form-group select,
.form-group textarea {
    padding: 12px 16px;
    border: 1px solid #d1d5db;
    border-radius: 8px;
    font-size: 16px;
    transition: border-color 0.2s ease, box-shadow 0.2s ease;
}

.form-group input:focus,
.form-group select:focus,
.form-group textarea:focus {
    outline: none;
    border-color: #4472c4;
    box-shadow: 0 0 0 3px rgba(68, 114, 196, 0.1);
}

.form-group input:read-only {
    background: #f9fafb;
    color: #6b7280;
}

/* RPE Container */
.rpe-container {
    display: flex;
    flex-direction: column;
    gap: 8px;
}

.rpe-labels {
    display: flex;
    justify-content: space-between;
    font-size: 12px;
    color: #64748b;
    margin-top: 4px;
}

#rpe-slider {
    width: 100%;
    margin: 8px 0;
}

#rpe-input {
    width: 80px;
}

/* Form Actions */
.form-actions {
    display: flex;
    gap: 16px;
    justify-content: center;
}

.srpe-display {
    text-align: center;
    padding: 16px;
    background: #f0f9ff;
    border-radius: 8px;
    margin-top: 24px;
    color: #0369a1;
}

/* Testes Grid */
.tests-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(320px, 1fr));
    gap: 24px;
}

.test-card {
    background: white;
    padding: 24px;
    border-radius: 12px;
    box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
    border: 1px solid #e2e8f0;
    text-align: center;
}

.test-header {
    margin-bottom: 16px;
}

.test-header h3 {
    font-size: 1.5rem;
    color: #1e293b;
    margin-bottom: 8px;
}

.test-date {
    color: #4472c4;
    font-weight: 600;
    font-size: 14px;
}

.test-protocol {
    background: #f8fafc;
    padding: 16px;
    border-radius: 8px;
    font-size: 14px;
    color: #64748b;
    margin-bottom: 24px;
    line-height: 1.5;
}

.test-result {
    margin-bottom: 24px;
}

.result-time {
    font-size: 3rem;
    font-weight: 700;
    color: #1e293b;
    margin-bottom: 8px;
}

.result-pace {
    font-size: 1.2rem;
    color: #64748b;
}

/* Zonas Table */
.zones-table {
    background: white;
    border-radius: 12px;
    overflow: hidden;
    box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
    border: 1px solid #e2e8f0;
}

.zone-row {
    display: grid;
    grid-template-columns: 2fr 1fr 1fr 1fr 3fr;
    gap: 16px;
    padding: 16px 24px;
    align-items: center;
    border-bottom: 1px solid #e2e8f0;
}

.zone-row:last-child {
    border-bottom: none;
}

.zone-header {
    background: #f8fafc;
    font-weight: 700;
    color: #374151;
    font-size: 14px;
    text-transform: uppercase;
    letter-spacing: 0.5px;
}

.zone-row.z1 { border-left: 4px solid #10b981; }
.zone-row.z2 { border-left: 4px solid #3b82f6; }
.zone-row.z3 { border-left: 4px solid #f59e0b; }
.zone-row.z4 { border-left: 4px solid #ef4444; }
.zone-row.z5 { border-left: 4px solid #8b5cf6; }

.zone-name {
    font-weight: 600;
    color: #1e293b;
}

.zone-pace,
.zone-hr {
    font-weight: 600;
    font-family: 'Monaco', 'Menlo', monospace;
    color: #4472c4;
}

.zone-rpe {
    font-weight: 600;
    color: #64748b;
}

.zone-desc {
    color: #64748b;
    font-size: 14px;
}

/* Modal */
.modal {
    display: none;
    position: fixed;
    z-index: 1000;
    left: 0;
    top: 0;
    width: 100%;
    height: 100%;
    background-color: rgba(0, 0, 0, 0.5);
    backdrop-filter: blur(4px);
}

.modal-content {
    background: white;
    margin: 5% auto;
    padding: 0;
    border-radius: 12px;
    width: 90%;
    max-width: 500px;
    box-shadow: 0 20px 40px rgba(0, 0, 0, 0.2);
    animation: modalSlideIn 0.3s ease;
}

@keyframes modalSlideIn {
    from {
        transform: translateY(-50px);
        opacity: 0;
    }
    to {
        transform: translateY(0);
        opacity: 1;
    }
}

.modal-header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 24px;
    border-bottom: 1px solid #e2e8f0;
}

.modal-header h3 {
    color: #1e293b;
    font-size: 1.5rem;
}

.close-modal {
    background: none;
    border: none;
    font-size: 24px;
    cursor: pointer;
    color: #64748b;
    padding: 4px;
    border-radius: 4px;
    transition: background 0.2s ease;
}

.close-modal:hover {
    background: #f1f5f9;
}

.modal form {
    padding: 24px;
}

.modal-actions {
    display: flex;
    gap: 12px;
    justify-content: flex-end;
    margin-top: 24px;
}

/* Responsividade */
@media (max-width: 768px) {
    .container {
        padding: 0 16px;
    }
    
    .nav-content {
        flex-wrap: wrap;
        gap: 12px;
    }
    
    .nav-links {
        flex-wrap: wrap;
        margin-left: 0;
        width: 100%;
    }
    
    .kpi-grid {
        grid-template-columns: 1fr;
    }
    
    .charts-grid {
        grid-template-columns: 1fr;
    }
    
    .form-grid {
        grid-template-columns: 1fr;
    }
    
    .zone-row {
        grid-template-columns: 1fr;
        gap: 8px;
        text-align: left;
    }
    
    .athletes-grid {
        grid-template-columns: 1fr;
    }
    
    .app-header h1 {
        font-size: 2rem;
    }
    
    .subtitle {
        font-size: 1.2rem;
    }
    
    .week-trainings {
        grid-template-columns: 1fr;
    }
    
    .tests-grid {
        grid-template-columns: 1fr;
    }
}

/* Animações */
@keyframes fadeIn {
    from { opacity: 0; transform: translateY(20px); }
    to { opacity: 1; transform: translateY(0); }
}

.section.active {
    animation: fadeIn 0.3s ease;
}

.kpi-card:hover {
    transform: translateY(-2px);
    box-shadow: 0 4px 16px rgba(0, 0, 0, 0.15);
}

/* Scrollbar personalizada */
::-webkit-scrollbar {
    width: 8px;
}

::-webkit-scrollbar-track {
    background: #f1f1f1;
}

::-webkit-scrollbar-thumb {
    background: #4472c4;
    border-radius: 4px;
}

::-webkit-scrollbar-thumb:hover {
    background: #3559a3;
}'''

# Salvar o arquivo CSS
with open('planilha-corrida-7km/style.css', 'w', encoding='utf-8') as f:
    f.write(css_content)

print("✅ style.css criado com sucesso!")
print("Tamanho do arquivo:", len(css_content), "caracteres")