import { useState, useEffect } from 'react';
import './StatusBar.css';

export default function StatusBar() {
  const [time, setTime] = useState(new Date());

  useEffect(() => {
    const t = setInterval(() => setTime(new Date()), 1000);
    return () => clearInterval(t);
  }, []);

  const formatted = time.toLocaleTimeString('es-AR', {
    hour: '2-digit',
    minute: '2-digit',
    second: '2-digit',
  });

  return (
    <footer className="status-bar">
      <div className="status-bar__inner">
        <div className="status-bar__left">
          <span className="status-bar__indicator" />
          <span className="status-bar__text">SISTEMA ACTIVO</span>
        </div>
        <div className="status-bar__center">
          <span className="status-bar__text">
            UADER · FCyT · Ingeniería en Sistemas · TP Inteligencia Artificial
          </span>
        </div>
        <div className="status-bar__right">
          <span className="status-bar__time">{formatted}</span>
        </div>
      </div>
    </footer>
  );
}
