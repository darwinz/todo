import type { Task } from '../types'
import TaskItem from './TaskItem'

interface Props {
  tasks: Task[]
  onToggle: (task: Task) => void
}

export default function TaskList({ tasks, onToggle }: Props) {
  if (tasks.length === 0) return <p className="empty">No tasks yet.</p>
  return (
    <ul className="task-list">
      {tasks.map((task) => (
        <TaskItem key={task.id} task={task} onToggle={onToggle} />
      ))}
    </ul>
  )
}
