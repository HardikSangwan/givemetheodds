<template>
  <div class="file-works">
    <h2>UPLOAD INTERCEPT</h2>
    <form class="upload">
      <input type="file" name="uploadFile" accept=".json" required />
      <input type="submit" value="Find Path"/>
    </form>
    <div>
      <h2 id="file-details">ODDS: </h2>
    </div>
  </div>
  <div id="bottom">
    <p>For feedback/issues, email the developer</p>
    <a href="mailto:hardik.sngn@gmail.com?subject=Giskard Interview Next Steps" target="_blank" rel="noopener"> <img alt="Mail logo" src="../assets/mail_logo.png" width="30" height="22" style="vertical-align: bottom;"> </a>
  </div>
</template>

<script>
export default {
  name: 'FileWorks'
}
document.addEventListener("DOMContentLoaded", () =>
{
const uploadForm = document.querySelector('.upload')

uploadForm.addEventListener('submit', ev => {
    ev.preventDefault();
    let file = ev.target.uploadFile.files[0]   
    let formData = new FormData();
    formData.append('rebel_filename', file)
    //console.log(formData)
    fetch('http://localhost:8000/uploadfile/', {
        method: 'POST',
        body: formData
    }).then(result => result.text()).then(r => {
        r = JSON.parse(r)
        document.querySelector('#file-details')
        .innerText = 'ODDS: ' + r.odds + ' %'
    });

});
});
</script>

<style>
li {
  display: inline;
  margin: 0px 10px 0 0;
  text-align:center;
}
#bottom
{
  margin-top: 75px
}
</style>
