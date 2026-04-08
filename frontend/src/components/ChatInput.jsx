import { useState } from 'react';
import { Send, Loader2, Sparkles } from 'lucide-react';
import './ChatInput.css';

export default function ChatInput({ onSend, isLoading }) {
  const [value, setValue] = useState('');
  const [focused, setFocused] = useState(false);

  const handleSubmit = (e) => {
    e.preventDefault();
    if (!value.trim() || isLoading) return;
    onSend(value.trim());
    setValue('');
  };

  return (
    <form className="chat-input" onSubmit={handleSubmit}>
      <div className={`chat-input__wrapper ${focused ? 'chat-input__wrapper--focused' : ''}`}>
        <div className="chat-input__glow" />
        <div className="chat-input__prefix">
          <Sparkles size={14} />
        </div>
        <input
          type="text"
          className="chat-input__field"
          placeholder="Hacé tu consulta sobre la carrera..."
          value={value}
          onChange={(e) => setValue(e.target.value)}
          onFocus={() => setFocused(true)}
          onBlur={() => setFocused(false)}
          disabled={isLoading}
        />
        <div className="chat-input__actions">
          <span className="chat-input__hint">Enter ↵</span>
          <button
            type="submit"
            className={`chat-input__btn ${value.trim() ? 'chat-input__btn--active' : ''}`}
            disabled={!value.trim() || isLoading}
            aria-label="Enviar mensaje"
          >
            {isLoading ? (
              <Loader2 size={16} className="chat-input__spinner" />
            ) : (
              <Send size={16} />
            )}
          </button>
        </div>
      </div>
    </form>
  );
}
