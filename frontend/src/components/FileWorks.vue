<template>
  <div class="file-works">
    <h2>UPLOAD</h2>
    <form class="upload">
      <input type="file" name="uploadFile" accept=".json" required />
      <br/><br/>
      <input type="submit" />
    </form>
    <div>
      <h2>ODDS</h2>
      <h4 id="file-details"></h4>
    </div>
  </div>
</template>

<script>
export default {
  name: 'FileWorks',
  props: {
    msg: String
  }, 
  data(){
    return {
      filename: '',
    };
  }
}
document.addEventListener("DOMContentLoaded", () =>
{
const uploadForm = document.querySelector('.upload')

uploadForm.addEventListener('submit', ev => {
    ev.preventDefault();
    let file = ev.target.uploadFile.files[0]   
    let formData = new FormData();
    formData.append('rebel_filename', file)
    console.log(formData)
    fetch('http://localhost:8000/uploadfile/', {
        method: 'POST',
        body: formData
    }).then(result => result.text()).then(r => {
        //console.log(r)
        document.querySelector('#file-details')
        .innerText = r
        //window.location.search = null
        //window.location.reload();
    });

});
});
</script>
