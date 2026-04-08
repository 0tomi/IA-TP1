import {
  BookOpen,
  Clock,
  GitBranch,
  FileText,
  BrainCircuit,
  Users,
  CalendarDays,
  Lightbulb,
  ClipboardEdit,
  Library,
  ListChecks,
  GraduationCap,
  HelpCircle,
} from 'lucide-react';

const iconMap = {
  BookOpen,
  Clock,
  GitBranch,
  FileText,
  BrainCircuit,
  Users,
  CalendarDays,
  Lightbulb,
  ClipboardEdit,
  Library,
  ListChecks,
  GraduationCap,
};

export default function QuestionIcon({ name, size = 18 }) {
  const Icon = iconMap[name] || HelpCircle;
  return <Icon size={size} />;
}
