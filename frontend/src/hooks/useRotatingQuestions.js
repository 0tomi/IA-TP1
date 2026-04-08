import { useState, useEffect, useCallback, useRef } from 'react';
import questions from '../data/predefinedQuestions.json';

function shuffleArray(arr) {
  const copy = [...arr];
  for (let i = copy.length - 1; i > 0; i--) {
    const j = Math.floor(Math.random() * (i + 1));
    [copy[i], copy[j]] = [copy[j], copy[i]];
  }
  return copy;
}

export function useRotatingQuestions(count = 3, intervalMs = 5000) {
  const [current, setCurrent] = useState([]);
  const [isTransitioning, setIsTransitioning] = useState(false);
  const prevIndicesRef = useRef(new Set());

  const pickQuestions = useCallback(() => {
    const available = questions.filter((_, i) => !prevIndicesRef.current.has(i));
    const pool = available.length >= count ? available : shuffleArray(questions);
    const picked = shuffleArray(pool).slice(0, count);
    prevIndicesRef.current = new Set(picked.map((q) => questions.indexOf(q)));
    return picked;
  }, [count]);

  useEffect(() => {
    setCurrent(pickQuestions());
  }, [pickQuestions]);

  useEffect(() => {
    const timer = setInterval(() => {
      setIsTransitioning(true);
      setTimeout(() => {
        setCurrent(pickQuestions());
        setIsTransitioning(false);
      }, 400);
    }, intervalMs);

    return () => clearInterval(timer);
  }, [intervalMs, pickQuestions]);

  return { questions: current, isTransitioning };
}
