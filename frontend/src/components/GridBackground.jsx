import './GridBackground.css';

export default function GridBackground() {
  return (
    <div className="grid-bg">
      <div className="grid-bg__dots" />
      <div className="grid-bg__scanline" />
      <div className="grid-bg__vignette" />
    </div>
  );
}
