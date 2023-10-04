import { fileURLToPath, URL } from 'node:url'

import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [
    vue(),
  ],
  server: {
    port: 3000,
    proxy: {
      '/api': {
        // target: `http://10.2.112.21:8080`,
        // target: loadEnv(mode, process.cwd()).VITE_APP_BASE_DOMIAN,
        target: 'http://127.0.0.1:5000',
        changeOrigin: true,
        // rewrite: (apiPath) => apiPath.replace(/^\/api/, ''),
        cookieDomainRewrite: 'localhost'
      }
    }
  },
  resolve: {
    alias: {
      '@': fileURLToPath(new URL('./src', import.meta.url))
    }
  }
})
