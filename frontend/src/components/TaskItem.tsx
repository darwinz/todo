import type { Task } from '../types'

interface Props {
  task: Task
  onToggle: (task: Task) => void
}

export default function TaskItem({ task, onToggle }: Props) {
  return (
    <li className="task-item">
      <input
        type="checkbox"
        id={`task-${task.id}`}
        checked={task.complete}
        onChange={() => onToggle(task)}
      />
      <label
        htmlFor={`task-${task.id}`}
        className={task.complete ? 'complete' : undefined}
      >
        {task.name}
      </label>
    </li>
  )
}
