import { useRotatingQuestions } from '../hooks/useRotatingQuestions';
import QuestionIcon from './QuestionIcon';
import './SuggestedQuestions.css';

export default function SuggestedQuestions({ onSelect }) {
  const { questions, isTransitioning } = useRotatingQuestions(3, 5000);

  return (
    <div className="suggested">
      <div className={`suggested__grid ${isTransitioning ? 'suggested__grid--exit' : 'suggested__grid--enter'}`}>
        {questions.map((q, i) => (
          <button
            key={q.id}
            className="suggested__card"
            onClick={() => onSelect(q.text)}
            style={{ animationDelay: `${i * 80}ms` }}
          >
            <div className="suggested__card-border" />
            <div className="suggested__card-inner">
              <span className="suggested__icon">
                <QuestionIcon name={q.icon} size={18} />
              </span>
              <span className="suggested__text">{q.text}</span>
            </div>
          </button>
        ))}
      </div>
    </div>
  );
}
