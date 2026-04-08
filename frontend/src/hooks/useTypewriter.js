import { useState, useEffect, useRef } from 'react';

/**
 * Simula el efecto de escritura palabra por palabra.
 * @param {string} text - Texto completo a mostrar
 * @param {boolean} active - Solo corre el efecto si es true
 * @param {number} speed - Milisegundos entre palabras (default 38ms)
 */
export function useTypewriter(text, active, speed = 38) {
  const [displayed, setDisplayed] = useState(active ? '' : text);
  const [done, setDone] = useState(!active);
  const indexRef = useRef(0);
  const rafRef = useRef(null);
  const lastTimeRef = useRef(null);

  useEffect(() => {
    if (!active) {
      setDisplayed(text);
      setDone(true);
      return;
    }

    setDisplayed('');
    setDone(false);
    indexRef.current = 0;
    lastTimeRef.current = null;

    // Dividimos en palabras conservando espacios
    const words = text.split(' ');

    const tick = (timestamp) => {
      if (!lastTimeRef.current) lastTimeRef.current = timestamp;
      const elapsed = timestamp - lastTimeRef.current;

      if (elapsed >= speed) {
        lastTimeRef.current = timestamp;
        indexRef.current += 1;
        const slice = words.slice(0, indexRef.current).join(' ');
        setDisplayed(slice);

        if (indexRef.current >= words.length) {
          setDone(true);
          return;
        }
      }

      rafRef.current = requestAnimationFrame(tick);
    };

    rafRef.current = requestAnimationFrame(tick);

    return () => {
      if (rafRef.current) cancelAnimationFrame(rafRef.current);
    };
  // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [text, active]);

  return { displayed, done };
}
