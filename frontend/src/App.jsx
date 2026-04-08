import { useState, useCallback, useEffect, useRef } from 'react';
import Header from './components/Header';
import HeroIcon from './components/HeroIcon';
import ChatInput from './components/ChatInput';
import ChatMessages from './components/ChatMessages';
import SuggestedQuestions from './components/SuggestedQuestions';
import GridBackground from './components/GridBackground';
import StatusBar from './components/StatusBar';
import LoadingScreen from './components/LoadingScreen';
import { sendMessage, getStatus } from './services/api';
import './App.css';

let msgId = 0;

export default function App() {
  const [messages, setMessages] = useState([]);
  const [isLoading, setIsLoading] = useState(false);
  const [backendStatus, setBackendStatus] = useState({ status: 'loading', phase: 'starting', message: 'Conectando...' });
  const [backendReady, setBackendReady] = useState(false);
  const pollRef = useRef(null);
  const hasMessages = messages.length > 0;

  useEffect(() => {
    let cancelled = false;

    async function poll() {
      try {
        const data = await getStatus();
        if (cancelled) return;
        setBackendStatus(data);
        if (data.status === 'ready') {
          setBackendReady(true);
          return; // stop polling
        }
        if (data.status === 'error') return; // stop polling on error too
      } catch {
        // backend not up yet — keep trying
        if (cancelled) return;
      }
      pollRef.current = setTimeout(poll, 1500);
    }

    poll();
    return () => { cancelled = true; clearTimeout(pollRef.current); };
  }, []);

  const handleSend = useCallback(async (text) => {
    const userMsg = { id: ++msgId, role: 'user', text };
    setMessages((prev) => [...prev, userMsg]);
    setIsLoading(true);

    try {
      const data = await sendMessage(text);
      const botMsg = { id: ++msgId, role: 'assistant', text: data.response, sources: data.sources ?? [] };
      setMessages((prev) => [...prev, botMsg]);
    } catch {
      const errMsg = {
        id: ++msgId,
        role: 'assistant',
        text: 'Lo siento, hubo un error al procesar tu consulta. Por favor intentá de nuevo.',
        sources: [],
      };
      setMessages((prev) => [...prev, errMsg]);
    } finally {
      setIsLoading(false);
    }
  }, []);

  const handleClear = useCallback(() => {
    setMessages([]);
  }, []);

  return (
    <>
      {!backendReady ? (
        <LoadingScreen status={backendStatus} />
      ) : (
        <div className="app">
          <GridBackground />
          <Header hasMessages={hasMessages} onClear={handleClear} />

          <div className="app__orbs">
            <div className="app__orb app__orb--1" />
            <div className="app__orb app__orb--2" />
            <div className="app__orb app__orb--3" />
          </div>

          <main className={`app__main ${hasMessages ? 'app__main--chatting' : ''}`}>

            {/* Hero / título compacto */}
            <div className={`app__hero ${hasMessages ? 'app__hero--compact' : ''}`}>
              {!hasMessages && <HeroIcon />}
              <h1 className="app__title">
                {hasMessages
                  ? 'Ragy'
                  : (<>Hola, soy <span className="app__title-name">Ragy</span></>)
                }
              </h1>
              {!hasMessages && (
                <p className="app__description">
                  Tu asistente inteligente para alumnos de{' '}
                  <strong>4° año · Licenciatura en Sistemas de Información</strong>
                  <br />
                  <span className="app__desc-detail">
                    Preguntame sobre materias, horarios, correlatividades y todo lo que necesites.
                  </span>
                </p>
              )}
              {!hasMessages && (
                <div className="app__tag-row">
                  <span className="app__tag">UADER</span>
                  <span className="app__tag-dot" />
                  <span className="app__tag">Facultad de Ciencia y Tecnología</span>
                  <span className="app__tag-dot" />
                  <span className="app__tag app__tag--accent">RAG + IA</span>
                </div>
              )}
            </div>

            {/* Zona de chat: mensajes + input apilados, scroll interno */}
            {hasMessages ? (
              <div className="app__chat-area">
                <ChatMessages messages={messages} isLoading={isLoading} />
                <div className="app__input-area">
                  <ChatInput onSend={handleSend} isLoading={isLoading} />
                </div>
              </div>
            ) : (
              <div className="app__input-area">
                <ChatInput onSend={handleSend} isLoading={isLoading} />
                <SuggestedQuestions onSelect={handleSend} />
              </div>
            )}

          </main>

          <StatusBar />
        </div>
      )}
    </>
  );
}
