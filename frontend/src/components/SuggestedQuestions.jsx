import { useRotatingQuestions } from '../hooks/useRotatingQuestions';
import QuestionIcon from './QuestionIcon';
import predefinedQuestions from '../data/predefinedQuestions.json';
import './SuggestedQuestions.css';

const longestQuestionText = predefinedQuestions.reduce((prev, curr) => 
  curr.text.length > prev.text.length ? curr : prev
).text;

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
              <span className="suggested__text-wrapper">
                <span className="suggested__text-ghost" aria-hidden="true">
                  {longestQuestionText}
                </span>
                <span className="suggested__text">{q.text}</span>
              </span>
            </div>
          </button>
        ))}
      </div>
    </div>
  );
}
