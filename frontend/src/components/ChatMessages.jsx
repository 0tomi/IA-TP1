import { useEffect, useRef } from 'react';
import { Bot, User, FileText } from 'lucide-react';
import { useTypewriter } from '../hooks/useTypewriter';
import './ChatMessages.css';

function AssistantBubble({ msg, isLatest }) {
  const { displayed, done } = useTypewriter(msg.text, isLatest);

  return (
    <div className="chat-msg__bubble">
      <p>
        {displayed}
        {!done && <span className="chat-msg__cursor" />}
      </p>
      {done && msg.sources && msg.sources.length > 0 && (
        <div className="chat-msg__sources">
          <span className="chat-msg__sources-label">
            <FileText size={11} />
            Fuentes
          </span>
          {msg.sources.map((src) => (
            <span key={src} className="chat-msg__source-pill">{src}</span>
          ))}
        </div>
      )}
    </div>
  );
}

export default function ChatMessages({ messages }) {
  const containerRef = useRef(null);

  // Scroll al fondo inmediato cuando llega un mensaje nuevo
  useEffect(() => {
    const el = containerRef.current;
    if (!el) return;
    el.scrollTo({ top: el.scrollHeight, behavior: 'smooth' });
  }, [messages.length]);

  // MutationObserver: sigue el contenido mientras el typewriter escribe.
  // Solo scrollea si el usuario ya está cerca del fondo (< 120px de margen),
  // para no interrumpir si el usuario subió manualmente.
  useEffect(() => {
    const el = containerRef.current;
    if (!el) return;

    const observer = new MutationObserver(() => {
      const { scrollTop, scrollHeight, clientHeight } = el;
      const distFromBottom = scrollHeight - scrollTop - clientHeight;
      if (distFromBottom < 120) {
        el.scrollTop = scrollHeight; // sin smooth → cada frame ya es suave
      }
    });

    observer.observe(el, {
      childList: true,
      subtree: true,
      characterData: true,
    });

    return () => observer.disconnect();
  }, []);

  if (messages.length === 0) return null;

  return (
    <div className="chat-messages" ref={containerRef}>
      {messages.map((msg, i) => {
        const isLatest = i === messages.length - 1;
        return (
          <div key={msg.id} className={`chat-msg chat-msg--${msg.role}`}>
            <div className="chat-msg__avatar">
              {msg.role === 'user' ? <User size={14} /> : <Bot size={14} />}
            </div>
            <div className="chat-msg__content">
              {msg.role === 'assistant' && (
                <span className="chat-msg__label">Ragy</span>
              )}
              {msg.role === 'assistant' ? (
                <AssistantBubble msg={msg} isLatest={isLatest} />
              ) : (
                <div className="chat-msg__bubble">
                  <p>{msg.text}</p>
                </div>
              )}
            </div>
          </div>
        );
      })}
    </div>
  );
}
