import { FileText, Database, Cpu, CheckCircle2, AlertCircle } from 'lucide-react';
import './LoadingScreen.css';

const PHASE_CONFIG = {
  starting:     { icon: Cpu,          label: 'INICIANDO',   color: 'var(--accent-primary)' },
  saneamiento:  { icon: FileText,     label: 'PROCESANDO',  color: 'var(--accent-primary)' },
  embeddings:   { icon: Database,     label: 'EMBEDDINGS',  color: 'var(--accent-secondary)' },
  vectorstore:  { icon: Cpu,          label: 'INDEXANDO',   color: 'var(--accent-secondary)' },
  ready:        { icon: CheckCircle2, label: 'LISTO',       color: '#22c55e' },
  error:        { icon: AlertCircle,  label: 'ERROR',       color: '#ef4444' },
};

export default function LoadingScreen({ status }) {
  const phase = PHASE_CONFIG[status.phase] || PHASE_CONFIG.starting;
  const PhaseIcon = phase.icon;
  const progress = status.total_files > 0
    ? Math.round((status.files_processed / status.total_files) * 100)
    : 0;

  return (
    <div className="loading-screen">
      <div className="loading-screen__orbs">
        <div className="loading-screen__orb loading-screen__orb--1" />
        <div className="loading-screen__orb loading-screen__orb--2" />
      </div>

      <div className="loading-screen__card">
        {/* Animated ring */}
        <div className="loading-screen__ring-wrap">
          <div className="loading-screen__ring" />
          <div className="loading-screen__ring-icon">
            <PhaseIcon size={28} style={{ color: phase.color }} />
          </div>
        </div>

        {/* Title */}
        <h1 className="loading-screen__title">
          Ragy
        </h1>
        <p className="loading-screen__subtitle">
          Preparando la base de conocimiento
        </p>

        {/* Phase badge */}
        <div className="loading-screen__phase" style={{ borderColor: phase.color }}>
          <span className="loading-screen__phase-dot" style={{ background: phase.color }} />
          {phase.label}
        </div>

        {/* Progress bar */}
        {status.total_files > 0 && (
          <div className="loading-screen__progress-wrap">
            <div className="loading-screen__progress-bar">
              <div
                className="loading-screen__progress-fill"
                style={{ width: `${progress}%` }}
              />
            </div>
            <span className="loading-screen__progress-text">
              {status.files_processed} / {status.total_files} archivos
            </span>
          </div>
        )}

        {/* Current file */}
        {status.current_file && (
          <div className="loading-screen__file">
            <FileText size={13} />
            <span>{status.current_file}</span>
          </div>
        )}

        {/* Message */}
        <p className="loading-screen__message">
          {status.message || 'Conectando con el servidor...'}
        </p>

        {/* Animated dots for non-error states */}
        {status.status !== 'error' && (
          <div className="loading-screen__dots">
            <span /><span /><span />
          </div>
        )}
      </div>

      <footer className="loading-screen__footer">
        UADER · FCyT · Licenciatura en Sistemas de Información · TP Inteligencia Artificial
      </footer>
    </div>
  );
}
