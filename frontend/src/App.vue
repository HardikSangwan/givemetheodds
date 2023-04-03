<template>
  <ul>
  <li>
    <div style="text-align: left;">
      <a href="https://giskard.ai" target="_blank" rel="noopener"><img alt="Giskard logo" src="./assets/logo.png" width = 450 height = 125 id ="log"></a>
      <h1>Interview Assessment: Pathfinder</h1>
      <h3>Getting Started</h3>
      <p>
        Upload the intercepted rebel file <br>
        Once the data has been received, possible paths will be generated <br>
        May the force be with you
      </p>
      <h3>Sources</h3>
      <div>
        <ul>
          <li><a href="https://giskard.ai" target="_blank" rel="noopener">giskard.ai</a></li>
        </ul>
      </div>
      <br><br><p>For feedback/issues, email the developer</p>
      <a href="mailto:hardik.sngn@gmail.com?subject=Giskard Interview Next Steps" target="_blank" rel="noopener"> <img alt="Mail logo" src="./assets/mail_logo.png" width="30" height="22" style="vertical-align: bottom;"> </a>
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
  background-color: #091623;
  margin-top: 0px;
  margin-left:10px;
}
img
{
  margin: 10px;
}
#logo
{
  float: left;    
  margin: 0 0 0 20px;
}
li {
  display: block;
  float: left;
  margin: 10px 10px 0 0;
}
#stream {
  margin: 50px 0px 0px 150px;
}
#upload {
  margin: 50px 0px 0px 150px;
  width: 320px;
}
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  color: #ecf5ff;
  background-color: transparent;
}
h1 {
  margin: 0px;
}
h3 {
  margin: 15px 0 0 0;
}
ul {
  list-style-type: none;
  padding: 0px;
}
a {
  color: #42b983;
}
button {
  margin: 10px 10px 10px 10px
}
</style>
