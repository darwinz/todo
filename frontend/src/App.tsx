import { useEffect, useState } from 'react'
import { getTasks, createTask, updateTask } from './api'
import type { Task } from './types'
import AddTaskForm from './components/AddTaskForm'
import TaskList from './components/TaskList'

export default function App() {
  const [tasks, setTasks] = useState<Task[]>([])
  const [loading, setLoading] = useState(true)
  const [error, setError] = useState<string | null>(null)

  useEffect(() => {
    getTasks()
      .then(setTasks)
      .catch((err: unknown) => setError(err instanceof Error ? err.message : String(err)))
      .finally(() => setLoading(false))
  }, [])

  async function handleAdd(name: string) {
    try {
      const task = await createTask(name)
      setTasks((prev) => [...prev, task])
    } catch (err: unknown) {
      setError(err instanceof Error ? err.message : String(err))
    }
  }

  async function handleToggle(task: Task) {
    try {
      const updated = await updateTask(task.id, { name: task.name, complete: !task.complete })
      setTasks((prev) => prev.map((t) => (t.id === updated.id ? updated : t)))
    } catch (err: unknown) {
      setError(err instanceof Error ? err.message : String(err))
    }
  }

  return (
    <div className="container">
      <h1>Tasks</h1>
      {error && <p className="error">{error}</p>}
      <AddTaskForm onAdd={handleAdd} />
      {loading ? <p>Loading…</p> : <TaskList tasks={tasks} onToggle={handleToggle} />}
    </div>
  )
}
