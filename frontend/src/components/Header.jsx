import { Terminal, RotateCcw } from 'lucide-react';
import './Header.css';

export default function Header({ hasMessages, onClear }) {
  return (
    <header className="header">
      <div className="header__inner">
        <div className="header__brand">
          <div className="header__logo-group">
            <div className="header__logo header__logo--uader">
              <span className="header__logo-letter">U</span>
            </div>
            <div className="header__logo header__logo--fcyt">
              <span className="header__logo-text">FCyT</span>
            </div>
          </div>
          <div className="header__titles">
            <span className="header__title">UADER</span>
            <span className="header__sep">/</span>
            <span className="header__subtitle">FCyT</span>
          </div>
        </div>
        <nav className="header__nav">
          {hasMessages && (
            <button className="header__clear" onClick={onClear}>
              <RotateCcw size={13} />
              <span>Nuevo chat</span>
            </button>
          )}
          <div className="header__badge">
            <Terminal size={12} />
            <span>Ragy</span>
            <span className="header__badge-dot" />
          </div>
        </nav>
      </div>
      <div className="header__glow-line" />
    </header>
  );
}
