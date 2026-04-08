import './HeroIcon.css';

export default function HeroIcon() {
  return (
    <div className="hero-icon">
      <div className="hero-icon__ring hero-icon__ring--outer" />
      <div className="hero-icon__ring hero-icon__ring--inner" />
      <div className="hero-icon__core">
        <svg
          className="hero-icon__svg"
          viewBox="0 0 48 48"
          fill="none"
          xmlns="http://www.w3.org/2000/svg"
        >
          {/* Neural brain / AI icon */}
          <path
            d="M24 4L8 13v22l16 9 16-9V13L24 4z"
            stroke="url(#heroGrad)"
            strokeWidth="1.5"
            fill="none"
            opacity="0.3"
          />
          <path
            d="M24 8L12 14.5v19L24 40l12-6.5v-19L24 8z"
            stroke="url(#heroGrad)"
            strokeWidth="1"
            fill="url(#heroGrad)"
            fillOpacity="0.05"
          />
          {/* Nodes */}
          <circle cx="24" cy="18" r="2.5" fill="url(#heroGrad)" />
          <circle cx="17" cy="26" r="2" fill="url(#heroGrad)" opacity="0.7" />
          <circle cx="31" cy="26" r="2" fill="url(#heroGrad)" opacity="0.7" />
          <circle cx="24" cy="33" r="2" fill="url(#heroGrad)" opacity="0.5" />
          {/* Connections */}
          <line x1="24" y1="20.5" x2="17" y2="24" stroke="url(#heroGrad)" strokeWidth="0.8" opacity="0.5" />
          <line x1="24" y1="20.5" x2="31" y2="24" stroke="url(#heroGrad)" strokeWidth="0.8" opacity="0.5" />
          <line x1="17" y1="28" x2="24" y2="31" stroke="url(#heroGrad)" strokeWidth="0.8" opacity="0.4" />
          <line x1="31" y1="28" x2="24" y2="31" stroke="url(#heroGrad)" strokeWidth="0.8" opacity="0.4" />
          {/* Sparkle */}
          <path d="M34 14l1 2.5 2.5 1-2.5 1L34 21l-1-2.5L30.5 17.5l2.5-1L34 14z" fill="#3898ec" opacity="0.6">
            <animate attributeName="opacity" values="0.6;1;0.6" dur="2s" repeatCount="indefinite" />
          </path>
          <defs>
            <linearGradient id="heroGrad" x1="8" y1="4" x2="40" y2="44">
              <stop stopColor="#3898ec" />
              <stop offset="1" stopColor="#0ea5e9" />
            </linearGradient>
          </defs>
        </svg>
      </div>
      {/* Floating particles */}
      <div className="hero-icon__particle hero-icon__particle--1" />
      <div className="hero-icon__particle hero-icon__particle--2" />
      <div className="hero-icon__particle hero-icon__particle--3" />
      <div className="hero-icon__particle hero-icon__particle--4" />
    </div>
  );
}
