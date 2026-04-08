/**
 * Convierte markdown básico a HTML. Cubre los patrones más comunes
 * que devuelve el LLM: bold, italic, listas, code, line breaks.
 */
export function markdownToHtml(text) {
  if (!text) return '';

  let html = text
    // Escapar HTML básico
    .replace(/&/g, '&amp;')
    .replace(/</g, '&lt;')
    .replace(/>/g, '&gt;');

  // Code blocks (```)
  html = html.replace(/```(\w*)\n([\s\S]*?)```/g, (_m, _lang, code) =>
    `<pre><code>${code.trim()}</code></pre>`
  );

  // Inline code (`)
  html = html.replace(/`([^`]+)`/g, '<code>$1</code>');

  // Bold + italic (***text***)
  html = html.replace(/\*\*\*(.+?)\*\*\*/g, '<strong><em>$1</em></strong>');

  // Bold (**text**)
  html = html.replace(/\*\*(.+?)\*\*/g, '<strong>$1</strong>');

  // Italic (*text*) — no matchea los * de listas
  html = html.replace(/(?<!\w)\*(?!\s)(.+?)(?<!\s)\*(?!\w)/g, '<em>$1</em>');

  // Headers (### h3, ## h2, # h1)
  html = html.replace(/^### (.+)$/gm, '<h3>$1</h3>');
  html = html.replace(/^## (.+)$/gm, '<h2>$1</h2>');
  html = html.replace(/^# (.+)$/gm, '<h1>$1</h1>');

  // Unordered lists (- item)
  html = html.replace(/^- (.+)$/gm, '<li>$1</li>');
  html = html.replace(/((?:<li>.*<\/li>\n?)+)/g, '<ul>$1</ul>');

  // Horizontal rule
  html = html.replace(/^---$/gm, '<hr/>');

  // Párrafos: doble \n separa bloques
  html = html
    .split('\n\n')
    .map((block) => {
      block = block.trim();
      if (!block) return '';
      if (/^<(h[1-3]|ul|ol|pre|hr)/.test(block)) return block;
      return `<p>${block.replace(/\n/g, '<br/>')}</p>`;
    })
    .join('');

  return html;
}
