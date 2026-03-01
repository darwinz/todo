import { useState } from 'react'

interface Props {
  onAdd: (name: string) => void
}

export default function AddTaskForm({ onAdd }: Props) {
  const [name, setName] = useState('')

  function handleSubmit(e: React.FormEvent) {
    e.preventDefault()
    if (!name.trim()) return
    onAdd(name.trim())
    setName('')
  }

  return (
    <form onSubmit={handleSubmit} className="add-form">
      <input
        type="text"
        value={name}
        onChange={(e) => setName(e.target.value)}
        placeholder="New task name…"
      />
      <button type="submit" disabled={!name.trim()}>
        Add
      </button>
    </form>
  )
}
