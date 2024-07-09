import { defineConfig } from 'vite'
import { svelte } from '@sveltejs/vite-plugin-svelte'
import fs from 'fs'
import path from 'path'

let httpsConfig = {};
const keyPath = process.env.CERT_KEY_PATH || 'certs/mydev.key';
const certPath = process.env.CERT_CERT_PATH || 'certs/mydev.crt';

// Conditionally load the certificate files
if (fs.existsSync(path.resolve(__dirname, keyPath)) && fs.existsSync(path.resolve(__dirname, certPath))) {
  httpsConfig = {
    key: fs.readFileSync(path.resolve(__dirname, keyPath)),
    cert: fs.readFileSync(path.resolve(__dirname, certPath))
  };
}

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [svelte()],
  server: {
    https: httpsConfig,
    port: 5173,
    host: true
  }
})
