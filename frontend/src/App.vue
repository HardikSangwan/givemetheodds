<template>
  <ul>
  <li>
    <div style="text-align: center;">
      <a href="https://giskard.ai" target="_blank" rel="noopener"><img alt="Giskard logo" src="./assets/logo.png" width = 450 height = 125 id ="log"></a>
      <h1>Interview Assessment: Pathfinder</h1>
    </div>
  </li>
  <li>
    <div id='upload'><FileWorks/></div>
  </li>
  </ul>
</template>

<script>
import FileWorks from './components/FileWorks.vue'

export default {
  name: 'App',
  components: {
    FileWorks
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #ecf5ff;
  background-color: transparent;
  margin-top: 0px;
}
a {
  color: #42b983;
}
</style>
