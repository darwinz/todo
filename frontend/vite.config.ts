import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'

export default defineConfig({
  plugins: [react()],
  server: {
    port: 5173,
    proxy: {
      '/tasks': {
        target: process.env.API_URL ?? 'http://localhost:5000',
        changeOrigin: true,
      },
    },
  },
})
