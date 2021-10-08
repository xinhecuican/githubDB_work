<template>
  <div class="box" ref="box">
  
  </div>
</template>

<script>
import { Scene, WebGLRenderer, PerspectiveCamera, BoxGeometry, MeshBasicMaterial, Mesh } from 'three';

export default {
  name: 'HelloWorld',
  props: {},
  mounted() {
    this.render();
  },
  methods: {
    render() {
      const renderer = new WebGLRenderer();
      renderer.setSize(600, 400);
      renderer.setClearColor(0x000000);
      this.$refs.box.appendChild(renderer.domElement);

      const scene = new Scene();

      const camera = new PerspectiveCamera(30, 6 / 4, 0.1, 10000);
      camera.position.set(0, 0, 5);
      scene.add(camera);

      const geometry = new BoxGeometry();
      const meterial = new MeshBasicMaterial({ color: 0xff00 });
      const cube = new Mesh(geometry, meterial);
      scene.add(cube);

      function animate() {
        requestAnimationFrame(animate);
        cube.rotation.x += 0.01;
        cube.rotation.y += 0.01;
        renderer.render(scene, camera)
      }
      animate()
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.box {
  display: flex;
  justify-content: center;
  width: 100%;
  height: 100%;
}
</style>
