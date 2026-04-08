import { useEffect, useRef } from 'react';
import { Bot, User, FileText } from 'lucide-react';
import { markdownToHtml } from '../hooks/renderMarkdown';
import { useTypewriter } from '../hooks/useTypewriter';
import './ChatMessages.css';

function TypingIndicator() {
  return (
    <div className="chat-msg chat-msg--assistant">
      <div className="chat-msg__avatar">
        <Bot size={14} />
      </div>
      <div className="chat-msg__content">
        <span className="chat-msg__label">Ragy</span>
        <div className="chat-msg__bubble chat-msg__bubble--typing">
          <div className="typing-dots">
            <span className="typing-dots__dot" />
            <span className="typing-dots__dot" />
            <span className="typing-dots__dot" />
          </div>
        </div>
      </div>
    </div>
  );
}

function AssistantBubble({ msg, isLatest }) {
  const { displayed, done } = useTypewriter(msg.text, isLatest);

  return (
    <div className="chat-msg__bubble">
      <div
        className="chat-msg__markdown"
        dangerouslySetInnerHTML={{ __html: markdownToHtml(displayed) }}
      />
      {!done && <span className="chat-msg__cursor" />}
      {done && msg.sources && msg.sources.length > 0 && (
        <div className="chat-msg__sources">
          <span className="chat-msg__sources-label">
            <FileText size={11} />
            Fuentes
          </span>
          {msg.sources.length === 1 ? (
             <span className="chat-msg__source-pill" title={msg.sources[0]}>{msg.sources[0]}</span>
          ) : (
             <div className="chat-msg__source-dropdown" tabIndex={0}>
               <span className="chat-msg__source-pill chat-msg__source-pill--toggle">
                 Varias Fuentes ({msg.sources.length})
               </span>
               <div className="chat-msg__source-dropdown-content">
                  {msg.sources.map((src) => (
                    <span key={src} className="chat-msg__source-dropdown-item">{src}</span>
                  ))}
               </div>
             </div>
          )}
        </div>
      )}
    </div>
  );
}

export default function ChatMessages({ messages, isLoading }) {
  const containerRef = useRef(null);

  useEffect(() => {
    const el = containerRef.current;
    if (!el) return;
    el.scrollTo({ top: el.scrollHeight, behavior: 'smooth' });
  }, [messages.length, isLoading]);

  useEffect(() => {
    const el = containerRef.current;
    if (!el) return;

    const observer = new MutationObserver(() => {
      const { scrollTop, scrollHeight, clientHeight } = el;
      const distFromBottom = scrollHeight - scrollTop - clientHeight;
      if (distFromBottom < 120) {
        el.scrollTop = scrollHeight;
      }
    });

    observer.observe(el, {
      childList: true,
      subtree: true,
      characterData: true,
    });

    return () => observer.disconnect();
  }, []);

  if (messages.length === 0 && !isLoading) return null;

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
      {isLoading && <TypingIndicator />}
    </div>
  );
}
