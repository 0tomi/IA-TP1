const API_BASE_URL = import.meta.env.VITE_API_URL || 'http://localhost:8000';

/**
 * Consulta el estado de inicialización del backend.
 * Devuelve { status, phase, current_file, files_processed, total_files, message }
 */
export async function getStatus() {
  const res = await fetch(`${API_BASE_URL}/api/status`);
  if (!res.ok) throw new Error(`Status check failed: ${res.status}`);
  return res.json();
}

// Respuestas hardcodeadas para desarrollo
const MOCK_RESPONSES = {
  default: "¡Buena pregunta! Estoy en proceso de conexión con el servidor. Cuando el backend esté listo, podré darte información precisa sobre las materias, horarios y todo lo relacionado con 4to año de Ingeniería en Sistemas en la UADER FCyT. 🎓",
  materias: "Las materias de 4to año de Ingeniería en Sistemas incluyen: Inteligencia Artificial, Redes de Datos, Ingeniería de Software II, Base de Datos II, entre otras. (Respuesta de ejemplo — datos reales próximamente).",
  horarios: "Los horarios del cuatrimestre actual están disponibles en la cartelera de la facultad y en el sistema SIU Guaraní. (Respuesta de ejemplo — datos reales próximamente).",
  correlatividades: "Las correlatividades se encuentran en el plan de estudios vigente. Te recomiendo consultarlo en la página oficial de la FCyT. (Respuesta de ejemplo — datos reales próximamente).",
  examenes: "Las fechas de exámenes finales se publican en el calendario académico de la UADER FCyT. (Respuesta de ejemplo — datos reales próximamente).",
};

const MOCK_SOURCES = {
  materias: ['Plan de Estudios 2021', 'Régimen Académico FCyT'],
  horarios: ['Calendario Académico 2025', 'Horarios 1er Cuatrimestre'],
  correlatividades: ['Plan de Estudios 2021'],
  examenes: ['Calendario Académico 2025', 'Reglamento de Exámenes'],
  default: [],
};

function getMockResponse(message) {
  const lower = message.toLowerCase();
  if (lower.includes('materia')) return { text: MOCK_RESPONSES.materias, sources: MOCK_SOURCES.materias };
  if (lower.includes('horario')) return { text: MOCK_RESPONSES.horarios, sources: MOCK_SOURCES.horarios };
  if (lower.includes('correlativ')) return { text: MOCK_RESPONSES.correlatividades, sources: MOCK_SOURCES.correlatividades };
  if (lower.includes('examen') || lower.includes('final')) return { text: MOCK_RESPONSES.examenes, sources: MOCK_SOURCES.examenes };
  return { text: MOCK_RESPONSES.default, sources: MOCK_SOURCES.default };
}

// Flag para usar mock o backend real
const USE_MOCK = import.meta.env.VITE_USE_MOCK !== 'false';

/**
 * Envía un mensaje al chatbot y obtiene la respuesta.
 * Cuando el backend esté listo, simplemente seteá VITE_USE_MOCK=false en .env
 */
export async function sendMessage(message) {
  if (USE_MOCK) {
    // Simular delay de red
    await new Promise((resolve) => setTimeout(resolve, 800 + Math.random() * 700));
    const mock = getMockResponse(message);
    return {
      response: mock.text,
      sources: mock.sources,
    };
  }

  const res = await fetch(`${API_BASE_URL}/api/chat`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ message }),
  });

  if (!res.ok) {
    throw new Error(`Error del servidor: ${res.status}`);
  }

  return res.json();
}
