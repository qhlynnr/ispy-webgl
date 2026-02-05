import { defineConfig } from 'vite';
import { viteStaticCopy } from 'vite-plugin-static-copy';

export default defineConfig({
  publicDir: false,
  plugins: [
    viteStaticCopy({
      targets: [
        { src: 'geometry', dest: '.' },
        { src: 'data', dest: '.' },
        { src: 'fonts/helvetiker_regular.typeface.json', dest: 'fonts' },
      ]
    })
  ]
});
