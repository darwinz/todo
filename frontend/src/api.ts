import type { Task } from './types'

async function request<T>(path: string, init?: RequestInit): Promise<T> {
  const res = await fetch(path, {
    headers: { 'Content-Type': 'application/json' },
    ...init,
  })
  if (!res.ok) {
    throw new Error(`${res.status} ${res.statusText}`)
  }
  if (res.status === 204) return undefined as T
  return res.json() as Promise<T>
}

export function getTasks(): Promise<Task[]> {
  return request<Task[]>('/tasks')
}

export function createTask(name: string): Promise<Task> {
  return request<Task>('/tasks', {
    method: 'POST',
    body: JSON.stringify({ name }),
  })
}

export function updateTask(id: number, patch: Partial<Task> & { name: string }): Promise<Task> {
  return request<Task>(`/tasks/${id}`, {
    method: 'PUT',
    body: JSON.stringify(patch),
  })
}

export function deleteTask(id: number): Promise<void> {
  return request<void>(`/tasks/${id}`, { method: 'DELETE' })
}
