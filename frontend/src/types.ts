export interface Task {
  id: number
  name: string
  description: string | null
  user_id: number | null
  complete: boolean
}
